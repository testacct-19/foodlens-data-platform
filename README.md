# FoodLens Data Platform

An end-to-end data pipeline behind a food-waste tracking app. It shows how
household purchase, consumption and waste data can flow from raw events
to analytics-ready tables and a dashboard.

> 🚧 Work in progress (November 2026). See the status list below.

## Architecture

1. **Generate**: a Python generator creates daily JSON events for ~500
   households (purchases, consumption, waste), including deliberately
   bad rows to test data quality.
2. **Enrich**: product details are pulled from the Open Food Facts API.
3. **Load (RAW)**: raw JSON lands in Snowflake as `VARIANT`.
4. **Clean (STAGING)**: `FLATTEN` to parse JSON, `QUALIFY` to remove
   duplicates, `MERGE` for incremental loads.
5. **Model (MARTS)**: dbt builds a star schema: `fct_purchases`,
   `fct_waste`, `dim_product`, `dim_household` (SCD Type 2), `dim_date`.
6. **Orchestrate**: an Airflow DAG runs daily, with data-quality gates.
7. **Visualise**: a Streamlit dashboard.

## Tech stack

Python · Snowflake · SQL · dbt · Airflow · Docker · Streamlit · Git

## Project structure

| Folder | Contents |
|---|---|
| `python/` | Data generator and API extract scripts |
| `data/` | Local raw files |
| `sql/` | Snowflake RAW and STAGING SQL |
| `dbt/` | dbt models (marts) |
| `airflow/` | Daily DAG |
| `dashboard/` | Streamlit app |
| `tests/` | Data-quality tests |
| `docs/` | Design notes |

## Documentation

- [Business requirements](brd.md)
- [Source data model](data_model.md)
- [Engineering decisions](engineering_decisions.md)

## Status

- [x] Repo setup and cleanup
- [ ] Household data generator
- [ ] Open Food Facts extract
- [ ] Snowflake RAW and STAGING
- [ ] dbt marts
- [ ] Airflow DAG with data-quality gates
- [ ] Streamlit dashboard