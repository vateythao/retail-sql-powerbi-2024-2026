import pandas as pd
import matplotlib.pyplot as plt

file_path = r"02_Clean_Data\sales_2024_2026_combined.csv"

df = pd.read_csv(file_path)
df["SalesDate"] = pd.to_datetime(df["SalesDate"])
df["Year"] = df["SalesDate"].dt.year
df["Month"] = df["SalesDate"].dt.month_name()

print("Sales data loaded successfully!")
print("Rows:", len(df))
print("Columns:", list(df.columns))

print()
print(df.head())
print("Date range:")
print("Start:", df["SalesDate"].min())
print("End:", df["SalesDate"].max())
print("Years in dataset:")
print(sorted(df["Year"].unique()))
print("Months in dataset:")
print(df["Month"].unique())
gross_sales = df[df["Metric"] == "Gross sales"]

yearly_gross_sales = (
    gross_sales
    .groupby("Year")["Amount"]
    .sum()
    .reset_index()
)

print()
print("Yearly Gross Sales:")
print(yearly_gross_sales.to_string(index=False))

yearly_gross_sales["YoY_Growth_Percent"] = (
    yearly_gross_sales["Amount"]
    .pct_change() * 100
)

print()
print("Year-over-Year Gross Sales Growth:")
print(yearly_gross_sales.to_string(index=False))

yearly_gross_sales["YoY_Growth_Percent"] = (
    yearly_gross_sales["YoY_Growth_Percent"]
    .round(2)
)

print()
print("Rounded Year-over-Year Growth:")
print(yearly_gross_sales.to_string(index=False))

plt.figure(figsize=(8, 5))

plt.bar(
    yearly_gross_sales["Year"].astype(str),
    yearly_gross_sales["Amount"]
)

plt.title("Yearly Gross Sales: 2024-2026")
plt.xlabel("Year")
plt.ylabel("Gross Sales ($)")

plt.tight_layout()

plt.savefig(
    r"05_Screenshots\09_python_yearly_gross_sales.png",
    dpi=300
)

plt.close()

monthly_gross_sales = (
    gross_sales
    .groupby(["Year", "Month"])["Amount"]
    .sum()
    .reset_index()
)

month_order = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

monthly_gross_sales["Month"] = pd.Categorical(
    monthly_gross_sales["Month"],
    categories=month_order,
    ordered=True
)

monthly_gross_sales = monthly_gross_sales.sort_values(
    ["Year", "Month"]
)

print()
print("Monthly Gross Sales:")
print(monthly_gross_sales.to_string(index=False))

plt.figure(figsize=(10, 6))

for year in sorted(monthly_gross_sales["Year"].unique()):
    year_data = monthly_gross_sales[
        monthly_gross_sales["Year"] == year
    ]

    plt.plot(
        year_data["Month"],
        year_data["Amount"],
        marker="o",
        label=str(year)
    )

plt.title("Monthly Gross Sales Trend: 2024-2026")
plt.xlabel("Month")
plt.ylabel("Gross Sales ($)")
plt.xticks(rotation=45)
plt.legend(title="Year")
plt.tight_layout()

plt.savefig(
    r"05_Screenshots\10_python_monthly_gross_sales_trend.png",
    dpi=300
)

plt.close()

top_months = (
    monthly_gross_sales
    .sort_values("Amount", ascending=False)
    .head(5)
)

print()
print("Top 5 Gross Sales Months:")
print(top_months.to_string(index=False))

top_months_chart = top_months.copy()

top_months_chart["Period"] = (
    top_months_chart["Month"].astype(str)
    + " "
    + top_months_chart["Year"].astype(str)
)

plt.figure(figsize=(9, 5))

plt.barh(
    top_months_chart["Period"],
    top_months_chart["Amount"]
)

plt.title("Top 5 Gross Sales Months")
plt.xlabel("Gross Sales ($)")
plt.ylabel("Month")

plt.gca().invert_yaxis()

plt.tight_layout()

plt.savefig(
    r"05_Screenshots\11_python_top_5_sales_months.png",
    dpi=300
)

plt.close()

gross_sales["DayOfWeek"] = gross_sales["SalesDate"].dt.day_name()

day_order = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

daily_pattern = (
    gross_sales
    .groupby("DayOfWeek")["Amount"]
    .mean()
    .reindex(day_order)
    .reset_index()
)

print()
print("Average Gross Sales by Day of Week:")
print(daily_pattern.to_string(index=False))

plt.figure(figsize=(9, 5))

plt.bar(
    daily_pattern["DayOfWeek"],
    daily_pattern["Amount"]
)

plt.title("Average Gross Sales by Day of Week")
plt.xlabel("Day of Week")
plt.ylabel("Average Gross Sales ($)")
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    r"05_Screenshots\12_python_sales_by_day_of_week.png",
    dpi=300
)

plt.close()