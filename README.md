# ETL-Batch-Pipeline-for-E-commerce-Sales

Summary: \
An end-to-end batch ETL pipeline built on the Medallion Architecture (Bronze → Silver → Gold), designed to ingest, clean, transform, and aggregate e-commerce sales data at scale using PySpark and Delta Lake on Databricks.

Problem Statement : \
E-commerce platforms generate high-volume transactional data across orders, customers, products, and payments. This raw data is often messy, duplicated, and unstructured — making it unusable for direct business reporting. This project simulates a real-world data engineering pipeline that ingests such data in batch, applies layered transformations, and produces clean, aggregated, business-ready tables for analytics and dashboarding.

Tech Stack :\
Ingestion source: Kaggle dataset, \
Database: Unity Catalog, \
Transformstions: Databricks Notebooks(Pyspark), \
DataType: Delta Tables, \
Dashboard: Databricks Dashboard. \
