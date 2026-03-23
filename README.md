# 🥐 Smart Bakery REST API

> A backend REST API demonstrating how a relational database powers real-time business logic — from schema design to cloud deployment.

[![Live API Docs](https://img.shields.io/badge/▶_Live_API_Docs-Render_(Swagger_UI)-46E3B7?style=for-the-badge)](https://smart-bakery-api.onrender.com/docs)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github)](https://github.com/aoadenus/smart-bakery-api)

> ℹ️ Render free tier spins down after inactivity. First load may take ~30 seconds to wake.

---

## Overview

Most database projects stop at the schema. This one goes further. The Smart Bakery API connects a normalized relational database to a live, deployed REST API — where placing an order automatically validates stock, deducts inventory, calculates the total, and logs the transaction in real time.

It was built to demonstrate end-to-end systems thinking: from database design through API development to cloud deployment. Swagger UI is auto-generated at `/docs`, so every endpoint can be tested live without any additional tooling.

---

## Features

- `GET /inventory` — Returns all products and current stock levels in JSON format
- `POST /order` — Validates stock, deducts inventory, calculates cost, and logs the transaction in one operation
- `GET /` — API health check and welcome route
- 📄 Interactive Swagger UI documentation auto-generated at `/docs`
- ✅ Pydantic models for request validation before any data touches the database
- 🔐 Parameterized SQL queries to prevent injection attacks
- ☁️ Deployed on Render with `$PORT` environment variable for production hosting

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3 |
| Framework | FastAPI |
| Database | SQLite3 |
| Server | Uvicorn |
| Validation | Pydantic |
| API Docs | Swagger UI (auto-generated) |
| Hosting | Render |

---

## What I Learned

- Designing a normalized relational schema (products + orders) with a foreign key relationship and understanding the tradeoffs
- How FastAPI's type system and Pydantic integration enforce data contracts before touching the database
- Writing parameterized SQL queries and why they matter for security
- Deploying a Python API to a cloud host and handling environment-aware configuration for production vs. local
- The difference between building a schema and building a system — business logic lives in the API layer, not just the database

---

## Contact

**Adetutu (Tutu) Adenusi**
📧 aoadenus@cougarnet.uh.edu · 📞 (713) 724-2642
🔗 [linkedin.com/in/adetutuadenusi](https://www.linkedin.com/in/adetutuadenusi)
💻 [github.com/aoadenus](https://github.com/aoadenus)
