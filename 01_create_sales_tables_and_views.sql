USE RetailPortfolio_2024_2026;
GO

/*
Retail Portfolio 2024-2026
Create combined sales table and reporting views.
*/


/*
Step 1: Combine yearly staging sales tables into one clean sales table.
*/

DROP TABLE IF EXISTS DailySalesSummary;
GO

SELECT
    CAST(sales_date AS DATE) AS SalesDate,
    metric_name AS MetricName,
    CAST(amount AS DECIMAL(12, 2)) AS Amount,
    2024 AS SalesYear
INTO DailySalesSummary
FROM stg_daily_sales_summary_2024

UNION ALL

SELECT
    CAST(sales_date AS DATE) AS SalesDate,
    metric_name AS MetricName,
    CAST(amount AS DECIMAL(12, 2)) AS Amount,
    2025 AS SalesYear
FROM stg_daily_sales_summary_2025

UNION ALL

SELECT
    CAST(sales_date AS DATE) AS SalesDate,
    metric_name AS MetricName,
    CAST(amount AS DECIMAL(12, 2)) AS Amount,
    2026 AS SalesYear
FROM stg_daily_sales_summary_2026;
GO


/*
Step 2: Create daily sales reporting view.
*/

CREATE OR ALTER VIEW vw_daily_sales_summary AS
SELECT
    SalesDate,
    SalesYear,

    SUM(CASE WHEN MetricName = 'Gross sales' THEN Amount ELSE 0 END) AS GrossSales,
    SUM(CASE WHEN MetricName = 'Net sales' THEN Amount ELSE 0 END) AS NetSales,
    SUM(CASE WHEN MetricName = 'Refunds' THEN Amount ELSE 0 END) AS Refunds,
    SUM(CASE WHEN MetricName = 'Taxes expected' THEN Amount ELSE 0 END) AS TaxesExpected,
    SUM(CASE WHEN MetricName = 'Taxes collected' THEN Amount ELSE 0 END) AS TaxesCollected,
    SUM(CASE WHEN MetricName = 'Tips' THEN Amount ELSE 0 END) AS Tips,
    SUM(CASE WHEN MetricName = 'Amount collected' THEN Amount ELSE 0 END) AS AmountCollected,
    SUM(CASE WHEN MetricName = 'Overpayments' THEN Amount ELSE 0 END) AS Overpayments,
    SUM(CASE WHEN MetricName = 'Unpaid balance' THEN Amount ELSE 0 END) AS UnpaidBalance
FROM DailySalesSummary
GROUP BY
    SalesDate,
    SalesYear;
GO


/*
Step 3: Create monthly sales reporting view.
*/

CREATE OR ALTER VIEW vw_monthly_sales AS
SELECT
    YEAR(SalesDate) AS SalesYear,
    MONTH(SalesDate) AS SalesMonth,
    DATENAME(MONTH, SalesDate) AS SalesMonthName,
    DATEFROMPARTS(YEAR(SalesDate), MONTH(SalesDate), 1) AS MonthStartDate,

    SUM(GrossSales) AS TotalGrossSales,
    SUM(NetSales) AS TotalNetSales,
    SUM(Refunds) AS TotalRefunds,
    SUM(TaxesCollected) AS TotalTaxesCollected,
    SUM(Tips) AS TotalTips,
    SUM(AmountCollected) AS TotalAmountCollected,
    SUM(UnpaidBalance) AS TotalUnpaidBalance,

    COUNT(*) AS NumberOfSalesDays
FROM vw_daily_sales_summary
GROUP BY
    YEAR(SalesDate),
    MONTH(SalesDate),
    DATENAME(MONTH, SalesDate),
    DATEFROMPARTS(YEAR(SalesDate), MONTH(SalesDate), 1);
GO


/*
Step 4: Create yearly sales reporting view.
*/

CREATE OR ALTER VIEW vw_yearly_sales AS
SELECT
    SalesYear,

    SUM(GrossSales) AS TotalGrossSales,
    SUM(NetSales) AS TotalNetSales,
    SUM(Refunds) AS TotalRefunds,
    SUM(TaxesCollected) AS TotalTaxesCollected,
    SUM(Tips) AS TotalTips,
    SUM(AmountCollected) AS TotalAmountCollected,
    SUM(UnpaidBalance) AS TotalUnpaidBalance,

    COUNT(*) AS NumberOfSalesDays
FROM vw_daily_sales_summary
GROUP BY SalesYear;
GO


/*
Step 5: Create daily sales KPI view.
*/

CREATE OR ALTER VIEW vw_sales_kpi_daily AS
SELECT
    SalesDate,
    SalesYear,
    MONTH(SalesDate) AS SalesMonth,
    DATENAME(MONTH, SalesDate) AS SalesMonthName,
    DATENAME(WEEKDAY, SalesDate) AS DayName,

    GrossSales,
    NetSales,
    Refunds,
    TaxesExpected,
    TaxesCollected,
    Tips,
    AmountCollected,
    Overpayments,
    UnpaidBalance,

    TaxesCollected - TaxesExpected AS TaxDifference,

    CASE 
        WHEN NetSales > 0 
        THEN AmountCollected / NetSales
        ELSE NULL
    END AS CollectionToNetSalesRatio
FROM vw_daily_sales_summary;
GO


/*
Step 6: Preview yearly result.
*/

SELECT *
FROM vw_yearly_sales
ORDER BY SalesYear;