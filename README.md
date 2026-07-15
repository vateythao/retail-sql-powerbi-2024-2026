# Retail SQL Server and Power BI Portfolio Project: 2024–2026

## Project Overview

This project demonstrates a full local data analytics workflow using SQL Server Express, SQL Server Management Studio, Excel/CSV files, Power Query, and Power BI Desktop.

The project uses fake retail sales and inventory data from 2024 through 2026. The goal was to practice importing data into SQL Server, creating staging tables, cleaning and combining yearly files, building SQL reporting views, and creating a Power BI dashboard for business analysis.

## Tools Used

* SQL Server Express
* SQL Server Management Studio
* Excel / CSV
* Power Query
* Power BI Desktop
* Windows local development environment

## Database

Database name:

```sql
RetailPortfolio_2024_2026
```

SQL Server connection:

```text
localhost\SQLEXPRESS
```

## Project Workflow

1. Created a local SQL Server database.
2. Organized raw and cleaned files into project folders.
3. Exported Excel workbook sheets into SQL-ready CSV files.
4. Imported 2024, 2025, and 2026 sales data into staging tables.
5. Combined yearly sales staging tables into one clean sales table.
6. Imported 2024, 2025, and 2026 product/inventory files into staging tables.
7. Combined yearly product staging tables into one clean product table.
8. Created SQL views for sales reporting and product data-quality reporting.
9. Created a Calendar table for Power BI date filtering.
10. Connected Power BI Desktop to SQL Server.
11. Built a dashboard with sales KPIs, trends, and product data-quality visuals.

## Main SQL Objects

### Staging Tables

```sql
stg_daily_sales_summary_2024
stg_daily_sales_summary_2025
stg_daily_sales_summary_2026

stg_products_2024
stg_products_2025
stg_products_2026
```

### Clean Tables

```sql
DailySalesSummary
Products
Calendar
```

### Reporting Views

```sql
vw_daily_sales_summary
vw_monthly_sales
vw_yearly_sales
vw_sales_kpi_daily
vw_product_catalog
```

## Dashboard Features

The Power BI dashboard includes:

* Total Gross Sales card
* Total Net Sales card
* Total Amount Collected card
* Total Taxes Collected card
* Net Sales by Year chart
* Monthly Net Sales Trend chart
* Net Sales by Day of Week chart
* Product Price Status chart
* Product Category Status chart
* Year slicer

## Skills Demonstrated

* SQL Server database setup
* CSV import into SQL Server
* Staging table workflow
* SQL data cleaning
* Combining multiple years of data with `UNION ALL`
* SQL views for reporting
* Data-quality checks
* Calendar/date table creation
* Power BI data modeling
* Power BI dashboard design
* Portfolio project organization

## Data Note

This project uses fake/sample retail data for learning and portfolio purposes.
