import pandas as pd
import os

# Dataset folder location
dataset_folder = r"C:\Users\hp\Desktop\Bluestock_MF_Capstone\Datasets"

# Output folder
output_folder = r"C:\Users\hp\Desktop\Bluestock_MF_Capstone\Day 2\Processed_Data"

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

files = [
    "01_fund_master.csv",
    "02_nav_history.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "07_scheme_performance.csv",
    "08_investor_transactions.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

for file in files:
    try:
        file_path = os.path.join(dataset_folder, file)

        print(f"\nProcessing: {file}")

        df = pd.read_csv(file_path)

        # Remove duplicate rows
        df = df.drop_duplicates()

        # Remove completely empty rows
        df = df.dropna(how="all")

        output_file = os.path.join(
            output_folder,
            f"cleaned_{file}"
        )

        df.to_csv(output_file, index=False)

        print(f"Saved: {output_file}")
        print(f"Rows: {len(df)}")

    except Exception as e:
        print(f"Error processing {file}: {e}")

print("\nData Cleaning Completed Successfully!")