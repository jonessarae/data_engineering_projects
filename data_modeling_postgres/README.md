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

## Database Schema

Diagram of a star schema used for designing the Postgres database. 

The key symbol in each table represents the primary key.

![schema](postgres.png)

## File Directory

## Example Queries


```
%sql SELECT count(start_time), DATE_PART('hour', start_time) FROM songplays GROUP BY DATE_PART('hour', start_time) ORDER BY count DESC;
```
