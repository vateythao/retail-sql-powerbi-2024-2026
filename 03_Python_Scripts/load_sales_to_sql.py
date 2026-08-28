import os
import pandas as pd
import pyodbc

server = os.getenv("SQL_SERVER", r"localhost\SQLEXPRESS")
database = os.getenv("SQL_DATABASE", "RetailPortfolio_2024_2026")

file_path = r"02_Clean_Data\sales_2024_2026_combined.csv"

df = pd.read_csv(file_path)

connection_string = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    f"SERVER={server};"
    f"DATABASE={database};"
    "Trusted_Connection=yes;"
)

connection = pyodbc.connect(connection_string)

print("Connected to SQL Server successfully!")

# Convert SalesDate to a real Python date
df["SalesDate"] = pd.to_datetime(df["SalesDate"]).dt.date

cursor = connection.cursor()

cursor.execute("TRUNCATE TABLE dbo.python_sales_clean")
connection.commit()

print("Existing SQL data cleared.")

cursor.fast_executemany = True

insert_query = """
INSERT INTO dbo.python_sales_clean (Metric, SalesDate, Amount)
VALUES (?, ?, ?)
"""

data_to_insert = list(
    df[["Metric", "SalesDate", "Amount"]]
    .itertuples(index=False, name=None)
)

cursor.executemany(insert_query, data_to_insert)

connection.commit()

print("Rows inserted successfully!")
print("Rows inserted:", len(data_to_insert))

cursor.close()
connection.close()

print("Combined sales file loaded.")
print("Rows:", len(df))
print(df.head())