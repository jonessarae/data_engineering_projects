# Project: Data Modeling with Postgres

## Table of Contents

* [Purpose](#Schema-definition)
* [How to run](#How-to-run)
* [Database Schema](#Database-schema)
* [File Directory](#File-Directory)
* [Example queries](#Example-queries)

## Purpose

Create a Postgres database with tables designed to optimize queries on song play analysis and build an ETL pipeline using Python for startup Sparkify.

## How to Run

Before running this project, the following software and packages (with the versions used) must be installed:

* PostgreSQL 9.5.19
* Python 3.6.3
* pandas 0.23.3
* psycopg2 2.7.4

Run the following commands in the terminal:

1. Create tables for Postgres database.
```
python create_tables.py
```

2. Execute ETL pipeline to process and insert JSON data to tables.
```
python etl.py
```

## Database Schema

Diagram of a star schema used for designing the Postgres database. 

The key symbol in each table represents the primary key.

![schema](postgres.png)

## File Directory

* create_tables.py
* etl.py
* sql_queries.py
* etl.ipynb
* test.ipynb

## Example Queries

Query to determine the hours users are most active. 

```
SELECT count(start_time), DATE_PART('hour', start_time) FROM songplays GROUP BY DATE_PART('hour', start_time) ORDER BY count DESC;
```

Query to determine how many songs played fall under "free" or "paid". 
```
SELECT level, count(level) FROM songplays GROUP BY level ORDER BY count DESC;
```
