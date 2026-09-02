import subprocess
import sys
import logging
from pathlib import Path


# --------------------------------------------------
# Logging setup
# --------------------------------------------------

log_dir = Path("06_Logs")
log_dir.mkdir(exist_ok=True)

logging.basicConfig(
    filename=log_dir / "etl_pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)


# --------------------------------------------------
# ETL Pipeline
# --------------------------------------------------

years = [2024, 2025, 2026]

try:
    print("\n========== STARTING ETL PIPELINE ==========")
    logging.info("ETL pipeline started")

    # Step 1: Process yearly sales files
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

        logging.info(f"{year} processing completed")

    # Step 2: Combine cleaned yearly data
    print("\n========== COMBINING SALES DATA ==========")

    subprocess.run(
        [
            sys.executable,
            "03_Python_Scripts/combine_sales_data.py"
        ],
        check=True
    )

    logging.info("Sales data combination completed")

    # Step 3: Load cleaned data into SQL Server
    print("\n========== LOADING DATA TO SQL SERVER ==========")

    subprocess.run(
        [
            sys.executable,
            "03_Python_Scripts/load_sales_to_sql.py"
        ],
        check=True
    )

    logging.info("SQL Server load completed")

    # Step 4: Run automated data tests
    print("\n========== RUNNING AUTOMATED TESTS ==========")

    subprocess.run(
        [
            sys.executable,
            "03_Python_Scripts/test_sales_data.py"
        ],
        check=True
    )

    logging.info("Automated data tests completed")

    # Step 5: Run Python exploratory data analysis
    print("\n========== RUNNING PYTHON EDA ==========")

    subprocess.run(
        [
            sys.executable,
            "03_Python_Scripts/sales_eda_analysis.py"
        ],
        check=True
    )

    logging.info("Python EDA completed")

    # Pipeline completed
    logging.info("ETL pipeline completed successfully")

    print("\n========================================")
    print("ETL PIPELINE COMPLETED SUCCESSFULLY!")
    print("========================================")


except subprocess.CalledProcessError as error:
    logging.exception(
        f"ETL pipeline failed while running a Python script: {error}"
    )

    print("\n========================================")
    print("ETL PIPELINE FAILED!")
    print("Check 06_Logs/etl_pipeline.log for details.")
    print("========================================")

    raise


except Exception as error:
    logging.exception(
        f"Unexpected ETL pipeline error: {error}"
    )

    print("\n========================================")
    print("UNEXPECTED PIPELINE ERROR!")
    print("Check 06_Logs/etl_pipeline.log for details.")
    print("========================================")

    raise