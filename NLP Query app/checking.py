import pandas as pd

path = r"C:\Users\kjabh\OneDrive\Desktop\Aircraft Schedule optimize\NLP Query app\Flight_Data.xlsx"
sheets = pd.read_excel(path, sheet_name=None)
print("Sheets found:", sheets.keys())
for name, df in sheets.items():
    print(f"Sheet: {name}, shape: {df.shape}")
    print(df.head())
