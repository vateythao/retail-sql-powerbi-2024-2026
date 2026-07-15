USE RetailPortfolio_2024_2026;
GO

/*
Retail Portfolio 2024-2026
Create Calendar table for Power BI date reporting.
*/

DROP TABLE IF EXISTS Calendar;
GO

WITH DateRange AS (
    SELECT CAST('2024-01-01' AS DATE) AS CalendarDate

    UNION ALL

    SELECT DATEADD(DAY, 1, CalendarDate)
    FROM DateRange
    WHERE CalendarDate < '2026-12-31'
)
SELECT
    CalendarDate,
    YEAR(CalendarDate) AS CalendarYear,
    MONTH(CalendarDate) AS CalendarMonth,
    DATENAME(MONTH, CalendarDate) AS CalendarMonthName,
    DAY(CalendarDate) AS DayOfMonth,
    DATENAME(WEEKDAY, CalendarDate) AS DayName,
    DATEPART(WEEKDAY, CalendarDate) AS DayOfWeekNumber,
    DATEFROMPARTS(YEAR(CalendarDate), MONTH(CalendarDate), 1) AS MonthStartDate
INTO Calendar
FROM DateRange
OPTION (MAXRECURSION 0);
GO

SELECT TOP 20 *
FROM Calendar
ORDER BY CalendarDate;