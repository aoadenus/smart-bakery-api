# Smart Bakery API

A REST API for bakery inventory and order management built with FastAPI and SQLite.

## Features

- **Inventory Management**: Track bakery products and stock levels
- **Order Processing**: Place orders with automatic stock deduction
- **Auto-generated Docs**: Interactive API documentation at `/docs`

## Database Schema

### Products Table
| Column | Type | Description |
|--------|------|-------------|
| product_id | INTEGER | Primary key, auto-increment |
| name | TEXT | Product name |
| price | REAL | Unit price |
| stock_quantity | INTEGER | Current stock level |

### Orders Table
| Column | Type | Description |
|--------|------|-------------|
| order_id | INTEGER | Primary key, auto-increment |
| product_id | INTEGER | Foreign key to products |
| quantity | INTEGER | Quantity ordered |
| total_price | REAL | Calculated total |

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome message |
| GET | `/inventory` | List all products with stock levels |
| POST | `/order` | Place an order (auto-deducts stock) |

### Example Order Request
```json
POST /order
{
  "product_id": 1,
  "quantity": 2
}
```

### Example Order Response
```json
{
  "status": "Success",
  "message": "Order placed for 2x Sourdough Loaf",
  "order_id": 1,
  "total_cost": 13.0,
  "remaining_stock": 18
}
```

## Quick Start

1. **Install dependencies**
   ```bash
   pip install fastapi uvicorn
   ```

2. **Run the server**
   ```bash
   uvicorn bakery_api:app --reload
   ```

3. **Open the interactive docs**
   
   Navigate to http://127.0.0.1:8000/docs

## Tech Stack

- **FastAPI** - Modern Python web framework
- **SQLite** - Lightweight database
- **Pydantic** - Data validation
- **Uvicorn** - ASGI server
