# ETL Pipeline: RandomUser API → PostgreSQL
(Cloud-Ready, Conceptual AWS Architecture)

## Overview

This project implements an end-to-end ETL pipeline that extracts user data from a public REST API, transforms and normalizes nested JSON data using Python, and loads the processed data into a PostgreSQL database.

The project focuses on data ingestion, transformation, relational data modeling, and pipeline robustness, with a design that is cloud-ready and aligned with modern data engineering practices.

The project focuses on **data ingestion, transformation, and relational data modeling**, with an emphasis on production-oriented design.

---

## Architecture

Implemented ETL Flow
RandomUser API → Python ETL (Extract & Transform) → PostgreSQL

Conceptual Cloud-Ready Architecture (AWS)

The ETL pipeline is designed to be easily extended to a cloud-based architecture:

![AWS ETL Architecture](.\screenshots\cloud_etl_architecture.drawio.png)
RandomUser API
      ↓
Python ETL Script
      ↓
AWS S3 (Raw Data Zone)
      ↓
AWS Glue (Data Transformation) [Conceptual]
      ↓
AWS S3 (Processed Data Zone)
      ↓
AWS Athena (Ad-hoc SQL Analytics)

Note: Cloud components are presented conceptually to demonstrate architectural understanding; no actual AWS deployment is required.
---

## Technologies

- Python (requests, pandas, SQLAlchemy)
- PostgreSQL
- SQL
- Environment variables (.env)
- Logging

---

## ETL Process

### Extract
- Data is retrieved from the RandomUser public API.
- Nested JSON responses are flattened into a pandas DataFrame.

### Transform
- Selection and renaming of relevant attributes.
- Explicit data type casting (dates, integers, strings).
- Removal of duplicate records using a unique user identifier.
- Filtering of records with missing critical location attributes.

### Load
- Transformed data is loaded into PostgreSQL using SQLAlchemy.
- Batch inserts are used to optimize performance.
- Secure connection handling via environment variables.
- Basic logging implemented for load status and error tracking.

---

## Database Design

- Relational users table with a UUID primary key
- Explicit data types optimized for analytical queries
- Indexes on frequently filtered dimensions:
    - country
    - city
    - gender
    - age
    - nationality

---

## Orchestration & Logging

- ETL steps are orchestrated via a central main.py script.
- Logging is implemented to monitor pipeline execution and failures.
- Environment-based configuration ensures portability across environments.

---

## Scope

- Focus on ETL, data modeling, and pipeline design
- Visualization intentionally out of scope
- Data prepared for downstream analytics or BI consumption

---

## Key Skills Demonstrated

- API-based data ingestion
- Data transformation and normalization in Python
- Relational schema design in PostgreSQL
- Secure configuration via environment variables
- ETL orchestration and basic observability
- Conceptual cloud architecture (AWS S3, Glue, Athena)

---

## Future Extensions (Big Data & Cloud)

This project is designed for small to medium-sized datasets processed on a single machine.  
For large-scale data processing and enterprise environments, the following extensions are possible:

- The transformation layer could be migrated to **Apache Spark** to enable distributed processing and higher scalability.
- **Databricks** could be used as a unified analytics platform for collaborative development, job orchestration, and cloud-native data pipelines.
- **AWS S3** or **Azure Data Lake** could serve as a data lake layer instead of local storage.
- Workflow orchestration could be extended using tools such as **Apache Airflow** or **AWS Step Functions**.

---

## Validation

The loaded data and database schema were validated using pgAdmin.
