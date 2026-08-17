# Sync Ingestion API

An asynchronous, idempotent batch ingestion service built with **FastAPI**, **SQLAlchemy**, and **Pydantic**. Designed to ingest data payloads from edge devices while enforcing strict duplicate prevention using unique record identifiers.

---

## Features

* **Idempotent Ingestion:** Inspects incoming record UUIDs to reject duplicate payloads gracefully without failing entire batches.
* **Asynchronous Database Layer:** Built with `SQLAlchemy` (async extension) and `aiosqlite` for non-blocking I/O operations.
* **API Key Middleware:** Enforces simple header-based authentication via `X-API-Key`.
* **Request Validation:** Strict data modeling using `Pydantic v2` and `pydantic-settings`.

---

## Tech Stack

* **Framework:** FastAPI
* **ASGI Server:** Uvicorn
* **ORM:** SQLAlchemy 2.0 (AsyncIO)
* **Database:** SQLite (`aiosqlite`) / PostgreSQL compatible (`asyncpg`)
* **Validation:** Pydantic v2

---

## Project Structure

```text
sync-ingestion-api/
├── app/
│   ├── api/
│   │   ├── dependencies.py    # Authentication & route dependencies
│   │   └── v1/
│   │       └── sync.py        # Batch ingestion route handlers
│   ├── models/
│   │   └── sync_record.py     # SQLAlchemy ORM database models
│   ├── schemas/
│   │   └── payload.py         # Pydantic request/response schemas
│   ├── config.py              # Application settings
│   ├── database.py            # Async engine & session setup
│   └── main.py                # FastAPI entrypoint & app lifespan
├── requirements.txt
└── .gitignore