import pandas as pd

sales_2024 = pd.read_csv(r"02_Clean_Data\sales_2024_clean.csv")
sales_2025 = pd.read_csv(r"02_Clean_Data\sales_2025_clean.csv")
sales_2026 = pd.read_csv(r"02_Clean_Data\sales_2026_clean.csv")

print("2024 rows:", len(sales_2024))
print("2025 rows:", len(sales_2025))
print("2026 rows:", len(sales_2026))

combined_sales = pd.concat(
    [sales_2024, sales_2025, sales_2026],
    ignore_index=True
)

print()
print("Combined rows:", len(combined_sales))

print()
print(combined_sales.head(10).to_string(index=False))

output_file = r"02_Clean_Data\sales_2024_2026_combined.csv"

combined_sales.to_csv(output_file, index=False)

print()
print("Combined file saved successfully!")
print(output_file)

print()
print("========== COMBINED DATA QUALITY CHECK ==========")

print("Total rows:", len(combined_sales))

print()
print("Missing values:")
print(combined_sales.isnull().sum())

print()
print("Duplicate Metric + SalesDate rows:")
print(
    combined_sales.duplicated(
        subset=["Metric", "SalesDate"]
    ).sum()
)

print()
print("Date range:")
print("Start:", combined_sales["SalesDate"].min())
print("End:", combined_sales["SalesDate"].max())