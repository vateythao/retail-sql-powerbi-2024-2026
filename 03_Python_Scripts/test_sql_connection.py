import os
import pyodbc

server = os.getenv("SQL_SERVER", r"localhost\SQLEXPRESS")
database = os.getenv("SQL_DATABASE", "RetailPortfolio_2024_2026")

connection_string = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    f"SERVER={server};"
    f"DATABASE={database};"
    "Trusted_Connection=yes;"
)

connection = pyodbc.connect(connection_string)

print("Connected to SQL Server successfully!")

cursor = connection.cursor()

cursor.execute("SELECT @@SERVERNAME, DB_NAME()")

row = cursor.fetchone()

print("Server:", row[0])
print("Database:", row[1])
cursor.execute("""
SELECT OBJECT_ID('dbo.python_sales_clean') AS TableObjectID
""")

table_id = cursor.fetchone()[0]

print("python_sales_clean Object ID:", table_id)

cursor.execute("""
SELECT
    s.name AS SchemaName,
    t.name AS TableName
FROM sys.tables t
JOIN sys.schemas s
    ON t.schema_id = s.schema_id
WHERE t.name LIKE '%sales%'
   OR t.name LIKE '%python%'
ORDER BY t.name
""")

print()
print("Tables visible to Python:")

for table in cursor.fetchall():
    print(table[0], table[1])

connection.close()