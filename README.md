# End-to-end Valorant Esports Data Engineering Pipeline

An end-to-end data engineering project for collecting, validating,
transforming, and modeling Valorant esports match data using a
Bronze-Silver-Gold architecture.

## Overview

This project is an end-to-end data engineering pipeline built around
Valorant esports data.

The project started as a web scraping and data analysis project and
has evolved into a structured data pipeline covering:

- Data extraction from esports websites
- Raw data ingestion
- Data validation and cleaning
- Dimensional modeling
- Data transformation using SQL and dbt
- Data quality testing
- BigQuery data warehousing
- Analytical-ready Gold models

The pipeline follows a Medallion Architecture consisting of Bronze,
Silver, and Gold layers.

## Project Objectives

The main objectives of this project are:

1. Collect Valorant esports match data through automated scraping.
2. Preserve raw data as a source of truth.
3. Normalize and clean data through layered transformations.
4. Build a dimensional data model for analytical workloads.
5. Implement automated data quality checks.
6. Use dbt to manage SQL transformations, testing, documentation,
   and model dependencies.
7. Build a scalable foundation for future orchestration and
   batch data processing.

## Data Pipeline

### Bronze

The Bronze layer stores raw scraped data with minimal transformation.
It acts as the source of truth and preserves the original structure
and values from the source.

### Staging

The Staging layer performs lightweight normalization and type
conversion, including:

- Datatype conversion
- Standardization
- Basic parsing
- Handling malformed source values

### Silver

The Silver layer contains cleaned and conformed datasets.

Transformations include:

- Data cleaning
- Domain validation
- Dimension construction
- Identifier mapping
- Foreign key preparation
- Standardized business entities

### Gold

The Gold layer contains analytical-ready fact models and derived
metrics.

Examples include:

- Match-level facts
- Game-level facts
- Map veto facts
- Team-game performance
- Derived performance metrics

## Data Warehouse Design

The warehouse follows a dimensional modeling approach.

### Fact Tables

Examples:

- `fact_matches` — one row per match
- `fact_games` — one row per game
- `fact_map_vetos` — map veto events at match/team level

### Dimension Tables

Examples:

- `dims_teams` — one row per team
- `dims_players` — one row per player
- `dims_maps` — one row per map
- `dims_agents` — one row per agent
- `dims_tours` — one row per tournament

## Data Transformation

Transformations are implemented primarily using SQL and managed through
dbt.

Examples of transformations include:

- Type conversion
- Domain validation
- Dimension lookups
- Foreign key mapping
- Derived metrics
- Aggregations
- Window functions
- Business logic

## Data Quality

Data quality checks are implemented using dbt tests.
Data quality rules are defined based on the expected domain,
structure, and business logic of each model.

Invalid source values are handled during transformation when
appropriate, while data tests are used to verify that the resulting
models satisfy their expected constraints.

Current checks include:

- `not_null`
- `unique`
- `relationships`
- `accepted_range`
- `accepted_values`
- `unique_combination_of_columns`

## dbt Implementation

dbt is used to manage:

- SQL transformations
- Model dependencies
- Data quality tests
- Model documentation
- Source definitions
- Data lineage
- Model materialization

Models use:

- `source()` for external/raw source tables
- `ref()` for dependencies between dbt models

## Data Lineage & Mapping

Column-level transformations are documented separately, including:

- Source field
- Target field
- Source/target model
- Transformation logic
- Transformation category

Examples:

| Source Model | Source Field | Target Model | Target Field | Transformation | Description |
|---|---|---|---|---|---|
| valorant-project-2026.bronze.tours | tour_id | stg_tours | tour_id | STR conversion | Tournament unique identifier |
| valorant-project-2026.bronze.tours | tour_name | stg_tours | tour_name | STR conversion | Official name of the tournament |

See [`docs/data_mapping.md`](docs/data_mapping.md) for the detailed
column-level mapping.

## Tech Stack

### Data Collection
- Python
- BeautifulSoup
- Requests

### Data Processing
- Python
- Pandas
- SQL

### Data Warehouse
- Google BigQuery
- Google Cloud Storage

### Transformation & Data Quality
- dbt
- dbt-bigquery
- dbt-utils

### Development
- Git
- GitHub

## Current Progress

### Completed

- [x] Valorant esports data scraping
- [x] Bronze raw data ingestion
- [x] BigQuery warehouse setup
- [x] Staging transformations
- [x] Silver data models
- [x] Dimension tables
- [x] Gold fact tables
- [x] Analytical views
- [x] Partitioning strategy evaluation
- [x] Data quality testing
- [x] dbt project setup
- [x] dbt source and model documentation
- [x] Generic and singular data tests
- [x] Data mapping documentation

### In Progress

- [ ] Improve handling of incomplete source data
- [ ] Refine transformation and domain validation rules
- [ ] Improve incremental processing
- [ ] Expand data coverage

### Planned

- [ ] Airflow orchestration
- [ ] Dockerized pipeline
- [ ] Automated batch ingestion
- [ ] Incremental dbt models
- [ ] Monitoring and pipeline observability

## Future Improvements

The next stage of the project will focus on operationalizing the
pipeline:

1. Containerize the pipeline using Docker.
2. Introduce Airflow for workflow orchestration.
3. Implement incremental ingestion and transformation.
4. Automate scheduled scraping.
5. Improve monitoring and failure handling.
6. Expand data coverage and historical backfill.
7. Integrate downstream analytical and machine learning workloads.