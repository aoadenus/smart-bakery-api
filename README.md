# Smart Bakery REST API 🥐

A backend REST API built to demonstrate how a relational database can power real-time business logic — not just store data. This project takes a SQL schema from concept to a fully deployed cloud service, handling inventory management and order processing end-to-end.

---

## Why I Built This

A lot of database projects stop at the schema. I wanted to go further and show how a well-designed relational database actually connects to a live application — where a customer placing an order automatically triggers inventory updates, validates stock levels, and returns a structured response in real time. That's the kind of systems thinking I'm developing through my coursework in CIS at the University of Houston, and this project is a direct application of it.

---

## What It Does

- **GET /inventory** — Returns all products and current stock levels from the database in JSON format
- **POST /order** — Accepts an order request, validates stock availability, calculates the total cost, deducts inventory, and logs the transaction
- **GET /** — API status check / welcome route
- **Interactive Docs** — Swagger UI auto-generated at `/docs` for live testing without any additional tools

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3 |
| Framework | FastAPI |
| Database | SQLite3 |
| Server | Uvicorn |
| Hosting | Render (cloud deployment) |
| Docs | Swagger UI (auto-generated) |

---

## Skills Demonstrated

- **Relational Database Design** — Designed a normalized schema with a `products` table (inventory) and an `orders` table (transaction log), connected via a foreign key relationship
- **SQL** — Used `CREATE TABLE`, `SELECT`, `INSERT`, `UPDATE` statements with parameterized queries to prevent SQL injection
- **Backend API Development** — Built RESTful endpoints using FastAPI with proper HTTP methods (GET, POST), status codes, and error handling
- **Data Validation** — Used Pydantic models to validate incoming request data before it touches the database
- **Business Logic Implementation** — Automated inventory deduction and stock validation as part of the order workflow
- **Cloud Deployment** — Deployed to Render with environment-aware configuration (`$PORT`) for production hosting
- **Version Control** — Managed source code with Git and GitHub, including a `.gitignore` to keep the database file out of version control
- **API Documentation** — Leveraged Swagger UI for interactive, self-documenting endpoints

---

## Database Schema

**`products`** — Inventory table

| Column | Type | Notes |
|---|---|---|
| product_id | INTEGER | Primary Key, Auto-increment |
| name | TEXT | Product name |
| price | REAL | Unit price |
| stock_quantity | INTEGER | Current inventory count |

**`orders`** — Transaction log

| Column | Type | Notes |
|---|---|---|
| order_id | INTEGER | Primary Key, Auto-increment |
| product_id | INTEGER | Foreign Key → products.product_id |
| quantity | INTEGER | Units ordered |
| total_price | REAL | Calculated at time of order |

---

## How to Run Locally

**1. Install dependencies**
```bash
pip install fastapi uvicorn
```

**2. Start the server**
```bash
uvicorn bakery_api:app --reload
```

**3. Open the interactive docs**

Navigate to `http://127.0.0.1:8000/docs` to test all endpoints in your browser.

---

## Live Demo

Deployed on Render — [https://smart-bakery-api.onrender.com/docs](https://smart-bakery-api.onrender.com/docs)

> Note: The free tier spins down after inactivity. First load may take ~30 seconds to wake up.

---

## About Me

**Adetutu (Tutu) Adenusi** — Computer Information Systems student at the University of Houston (May 2027), with a focus on enterprise systems, data analytics, and business-oriented technology solutions.

[LinkedIn](https://www.linkedin.com/in/adetutuadenusi) · [GitHub](https://github.com/aoadenus)
