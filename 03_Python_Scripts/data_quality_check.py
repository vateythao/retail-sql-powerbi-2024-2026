import pandas as pd
import sys

year = int(sys.argv[1]) if len(sys.argv) > 1 else 2026

file_path = fr"01_Raw_Data\Sales\sales_data_fake_{year}_year_workbook.xlsx"

# Row 11 contains the real column headers
df = pd.read_excel(file_path, header=11)

# Rename the first column to Metric
df = df.rename(columns={df.columns[0]: "Metric"})

df = df.dropna(how="all")

df = df.dropna(subset=["Total"])

valid_metrics = [
    "Gross sales",
    "Refunds",
    "Net sales",
    "Overpayments",
    "Taxes expected",
    "Taxes collected",
    "Tips",
    "Amount collected",
    "Unpaid balance"
]

df = df[df["Metric"].isin(valid_metrics)]

daily_df = df.drop(columns=["Total"])

daily_df = daily_df.melt(
    id_vars=["Metric"],
    var_name="SalesDate",
    value_name="Amount"
)

daily_df["Amount"] = (
    daily_df["Amount"]
    .astype(str)
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
)

daily_df["Amount"] = pd.to_numeric(
    daily_df["Amount"],
    errors="coerce"
)

daily_df["SalesDate"] = pd.to_datetime(
    daily_df["SalesDate"] + f"-{year}",
    format="%d-%b-%Y"
)
print()
print("SalesDate data type:")
print(daily_df["SalesDate"].dtype)

print()
print(daily_df.head(10).to_string(index=False))

print()
print("Reshaped daily sales data:")
print(daily_df.shape)

print()
print(daily_df.head(15).to_string(index=False))

print("Sales table loaded!")
print()

print("Rows and columns:")
print(df.shape)

print()

print("First 10 rows:")
print(df.iloc[:10, :8].to_string(index=False))

print()
print("Amount data type:")
print(daily_df["Amount"].dtype)

print()
print(daily_df.head(10).to_string(index=False))

print()
print("========== DATA QUALITY CHECK ==========")

print()
print("Total rows:")
print(len(daily_df))

print()
print("Missing values:")
print(daily_df.isnull().sum())

print()
print("Duplicate Metric + SalesDate rows:")
duplicates = daily_df.duplicated(
    subset=["Metric", "SalesDate"]
).sum()

print(duplicates)

print()
print("Date range:")
print("Start:", daily_df["SalesDate"].min())
print("End:", daily_df["SalesDate"].max())

output_file = fr"02_Clean_Data\sales_{year}_clean.csv"

daily_df.to_csv(output_file, index=False)

print()
print("Cleaned file saved successfully!")
print(output_file)

print()
print("Duplicate rows found:")

duplicate_rows = daily_df[
    daily_df.duplicated(
        subset=["Metric", "SalesDate"],
        keep=False
    )
]

print(
    duplicate_rows
    .sort_values(["SalesDate", "Metric"])
    .to_string(index=False)
)