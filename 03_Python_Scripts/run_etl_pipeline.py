import subprocess
import sys

years = [2024, 2025, 2026]

for year in years:
    print(f"\n========== PROCESSING {year} ==========")

    subprocess.run(
    [
        sys.executable,
        "03_Python_Scripts/data_quality_check.py",
        str(year)
    ],
    check=True
)

print("\n========== COMBINING SALES DATA ==========")

subprocess.run(
    [
        sys.executable,
        "03_Python_Scripts/combine_sales_data.py"
    ],
    check=True
)

print("\n========== LOADING DATA TO SQL SERVER ==========")

subprocess.run(
    [
        sys.executable,
        "03_Python_Scripts/load_sales_to_sql.py"
    ],
    check=True
    
)
print("\n========== RUNNING PYTHON EDA ==========")

subprocess.run(
    [
        sys.executable,
        "03_Python_Scripts/sales_eda_analysis.py"
    ],
    check=True
)
print("\nETL pipeline completed successfully!")