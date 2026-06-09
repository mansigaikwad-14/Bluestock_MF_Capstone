import pandas as pd
import sqlite3
import os

db_path = r"C:\Users\hp\Desktop\Bluestock_MF_Capstone\Day 2\bluestock_mf.db"

conn = sqlite3.connect(db_path)

processed_folder = r"C:\Users\hp\Desktop\Bluestock_MF_Capstone\Day 2\Processed_Data"

for file in os.listdir(processed_folder):

    if file.endswith(".csv"):

        file_path = os.path.join(processed_folder, file)

        table_name = file.replace(".csv", "")

        df = pd.read_csv(file_path)

        df.to_sql(
            table_name,
            conn,
            if_exists="replace",
            index=False
        )

        print(f"Loaded table: {table_name}")

conn.close()

print("Database created successfully!")