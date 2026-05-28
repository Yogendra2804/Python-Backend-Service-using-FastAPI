# Python Backend Service using FastAPI

A FastAPI-based backend service for looking up card BIN/IIN information from a SQLite database, with both raw SQL and SQLAlchemy ORM approaches, plus JWT-protected endpoints.

---

# 🚀 Features

- FastAPI application with modular route files
- SQLite database integration
- Two data-access styles:
  - Raw SQL (`sqlite3`)
  - SQLAlchemy ORM
- JWT-based authentication for protected endpoints
- Structured logging support

---

# 🛠️ Tech Stack

- Python
- FastAPI
- SQLite
- SQLAlchemy
- python-jose (JWT)
- Uvicorn

---

# 📁 Project Structure

```bash
.
├── main.py                 # App entrypoint, includes routers
├── Find_CARDS.py           # Raw SQL endpoints
├── ORM_Find_CARDS.py       # ORM endpoints + token endpoint
├── CARDS_token.py          # JWT generation and verification
├── Modle.py                # Pydantic + SQLAlchemy models
├── engine.py               # DB engine and session config
├── Logging/
│   └── zlogger_config.py   # Logging setup
└── requirements.txt
```

---

# 🌐 API Overview

## Public Endpoints

### `GET /cards/raw?IIN=123456`

Fetch card details using raw SQL.

### `POST /cards`

Fetch card details from request body.

### `POST /allCards?name=visa`

Fetch BIN list by scheme/network.

---

## 🔐 Authentication Endpoint

### `POST /getToken?Mail=user@example.com`

Generate JWT access token.

---

## 🔒 Protected Endpoints

> Requires Bearer Token Authentication

### `GET /cards?iin=123456`

ORM-based card lookup.

### `POST /cards`

ORM-based card lookup from request body.

### `POST /allCards?name=visa`

ORM-based list endpoint.

---

## ⚠️ Important Note

Some route paths are shared between raw SQL and ORM modules.  
If both routers are active together, behavior depends on route registration order.

---

# ⚙️ Getting Started

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/Yogendra2804/Python-Backend-Service-using-FastAPI.git
cd Python-Backend-Service-using-FastAPI
```

---

## 2️⃣ Create and Activate Virtual Environment

```bash
python -m venv .venv
```

### Windows (PowerShell)

```powershell
.venv\Scripts\Activate.ps1
```

### Linux/macOS

```bash
source .venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Run the Server

```bash
uvicorn main:app --reload
```

Server starts at:

- API: `http://127.0.0.1:8000`
- Swagger Docs: `http://127.0.0.1:8000/docs`

---

# 🔑 Authentication Usage

1. Call `POST /getToken` with an email.
2. Copy the returned JWT token.
3. Open Swagger UI.
4. Click the **Authorize** button.
5. Enter:

```text
Bearer <your_token_here>
```

6. Access protected endpoints.

---

# 📦 Example Request Body

For endpoints expecting the `Value` model:

```json
{
  "IIN": 123456
}
```

---

# 📚 Current Learning Focus

This project is intentionally iterative and learning-driven.

Current areas include:

- API design with FastAPI
- Validation with Pydantic
- ORM vs Raw SQL tradeoffs
- Token-based authentication
- Logging and backend maintainability

---

# 🛣️ Roadmap

- [ ] Move secrets (JWT key, DB path) to environment variables
- [ ] Improve error handling with proper HTTP status codes
- [ ] Resolve route path overlaps between raw and ORM modules
- [ ] Add tests with pytest
- [ ] Add Docker support
- [ ] Add CI/CD pipeline

---

# 🤝 Contributing

Suggestions and improvements are welcome.

Feel free to open an issue or submit a pull request.

---

# 👨‍💻 Author

**Yogendra**

GitHub: [@Yogendra2804](https://github.com/Yogendra2804)

---
