from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

# --- 1. DATABASE SETUP (SQL SCHEMA) ---
def init_db():
    conn = sqlite3.connect("bakery.db")
    cursor = conn.cursor()
    
    # Create Products Table (Inventory)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            stock_quantity INTEGER NOT NULL
        )
    ''')
    
    # Create Orders Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            order_id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER,
            quantity INTEGER NOT NULL,
            total_price REAL NOT NULL,
            FOREIGN KEY (product_id) REFERENCES products (product_id)
        )
    ''')
    
    # Insert initial sample data if the table is empty
    cursor.execute("SELECT COUNT(*) FROM products")
    if cursor.fetchone()[0] == 0:
        sample_products = [
            ("Sourdough Loaf", 6.50, 20),
            ("Chocolate Croissant", 4.00, 35),
            ("Blueberry Muffin", 3.50, 40),
            ("Baguette", 3.00, 25)
        ]
        cursor.executemany("INSERT INTO products (name, price, stock_quantity) VALUES (?, ?, ?)", sample_products)
    
    conn.commit()
    conn.close()

# Run database initialization
init_db()

# --- 2. FASTAPI APPLICATION ---
app = FastAPI(title="Smart Bakery API", description="A REST API for bakery inventory and order management")

# Pydantic model for incoming order requests
class OrderRequest(BaseModel):
    product_id: int
    quantity: int

@app.get("/")
def read_root():
    return {"message": "Welcome to the Smart Bakery API!"}

@app.get("/inventory")
def get_inventory():
    """Retrieve all bakery products and current stock levels."""
    conn = sqlite3.connect("bakery.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    items = cursor.fetchall()
    conn.close()
    
    # Format the SQL output into clean JSON
    inventory = [{"product_id": row[0], "name": row[1], "price": row[2], "stock": row[3]} for row in items]
    return {"inventory": inventory}

@app.post("/order")
def place_order(order: OrderRequest):
    """Place an order and automatically deduct from inventory."""
    conn = sqlite3.connect("bakery.db")
    cursor = conn.cursor()
    
    # Check if the product exists and has enough stock
    cursor.execute("SELECT name, price, stock_quantity FROM products WHERE product_id = ?", (order.product_id,))
    product = cursor.fetchone()
    
    if not product:
        conn.close()
        raise HTTPException(status_code=404, detail="Product not found")
        
    name, price, current_stock = product
    
    if current_stock < order.quantity:
        conn.close()
        raise HTTPException(status_code=400, detail=f"Insufficient stock for {name}. Only {current_stock} left.")
    
    # Calculate total price
    total_price = price * order.quantity
    new_stock = current_stock - order.quantity
    
    # 1. Deduct from inventory (Products Table)
    cursor.execute("UPDATE products SET stock_quantity = ? WHERE product_id = ?", (new_stock, order.product_id))
    
    # 2. Record the order (Orders Table)
    cursor.execute("INSERT INTO orders (product_id, quantity, total_price) VALUES (?, ?, ?)", 
                   (order.product_id, order.quantity, total_price))
    
    conn.commit()
    order_id = cursor.lastrowid
    conn.close()
    
    return {
        "status": "Success",
        "message": f"Order placed for {order.quantity}x {name}",
        "order_id": order_id,
        "total_cost": total_price,
        "remaining_stock": new_stock
    }
