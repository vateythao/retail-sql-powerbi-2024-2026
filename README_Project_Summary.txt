# Retail SQL Server and Power BI Portfolio Project: 2024–2026

This project demonstrates a local data analytics workflow using SQL Server Express, SQL Server Management Studio, Excel/CSV files, Power Query, and Power BI Desktop. The project uses fake retail sales and inventory data from 2024 through 2026 to practice importing, cleaning, transforming, analyzing, and visualizing business data.

The SQL Server database was created as `RetailPortfolio_2024_2026`. Sales files from 2024, 2025, and 2026 were imported into yearly staging tables and then combined into one clean `DailySalesSummary` table. Product and inventory files from 2024, 2025, and 2026 were also imported into staging tables and combined into one clean `Products` table.

The project includes SQL views for daily sales, monthly sales, yearly sales, sales KPIs, and product data-quality analysis. A Calendar table was also created to support date-based reporting in Power BI.

The Power BI dashboard includes KPI cards for total gross sales, total net sales, total amount collected, and total taxes collected. It also includes visuals for net sales by year, monthly net sales trend, net sales by day of week, product price status, product category status, and a year slicer.

Key skills demonstrated include SQL Server database setup, CSV import, staging tables, SQL data cleaning, `UNION ALL`, SQL views, date tables, Power BI relationships, dashboard design, and portfolio project organization.
