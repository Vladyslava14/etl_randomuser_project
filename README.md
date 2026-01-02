# etl_randomuser_project
# ETL Pipeline: RandomUser API → PostgreSQL

## Overview

This project implements a **end-to-end ETL pipeline** that extracts user data from a public REST API, transforms and normalizes nested JSON data using Python, and loads the cleaned data into a PostgreSQL database.

The project focuses on **data ingestion, transformation, and relational data modeling**, with an emphasis on production-oriented design.

---

## Architecture

RandomUser API → Python (Extract, Transform) → PostgreSQL

---

## Technologies

- Python (requests, pandas, SQLAlchemy)
- PostgreSQL
- SQL
- Logging

---

## ETL Process

### Extract
- Data is retrieved from the RandomUser public API.
- Nested JSON responses are flattened into a pandas DataFrame.

### Transform
- Relevant fields are selected and renamed.
- Data types are explicitly cast (dates, integers, floats).
- Duplicates are removed using a unique user identifier.
- Records with missing key location fields are filtered out.

### Load
- Transformed data is appended to a pre-defined PostgreSQL table.
- Inserts are optimized using batch operations.
- Database schema and constraints are managed at the SQL level.

---

## Database Design

- Relational `users` table with a UUID primary key
- Explicit data types for analytical queries
- Indexes on commonly filtered dimensions (country, city, gender, age, nationality)

---

## Orchestration & Logging

- ETL steps are orchestrated via a central `main.py` script.
- Basic logging is implemented to track pipeline execution and failures.

---

## Scope

- Focused on ETL and data modeling
- Visualization intentionally out of scope
- Data is prepared for downstream analytics or BI tools

---

## Key Skills Demonstrated

- API-based data ingestion
- Data transformation and cleaning in Python
- Relational schema design in PostgreSQL
- ETL orchestration and observability

## Validation

The loaded data and schema were validated using pgAdmin.
