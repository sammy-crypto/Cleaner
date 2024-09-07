import pandas as pd
import time
def remove_empty_rows(input_csv, output_csv, column_name):
    df = pd.read_csv(input_csv)
    if column_name not in df.columns:
        print(f"Column '{column_name}' not found in the CSV file.")
        return
    df_cleaned = df[df[column_name].notna() & df[column_name].astype(str).str.strip().astype(bool)]
    df_cleaned.to_csv(output_csv, index=False)

    print(f"Rows with empty '{column_name}' cells have been removed and saved to '{output_csv}'.")


input_csv = input('File Name: ')
output_csv = 'output.csv'
num = int(input('How many collumns: '))
column_name =  str(input("Collumn Name: "))
remove_empty_rows(input_csv, output_csv, column_name)
for i in range(num-1):
    column_name =  str(input("Collumn Name: "))
    remove_empty_rows(output_csv, output_csv, column_name)
    
time.sleep(3)
