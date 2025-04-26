import pandas as pd

# Read the CSV file
df = pd.read_csv('korean_russian_namelist.csv')

# Create a writer object for Excel
writer = pd.ExcelWriter('korean_russian_namelist.xlsx', engine='xlsxwriter')

# Convert the dataframe to an Excel file
df.to_excel(writer, index=False, sheet_name='Namelist')

# Close the Pandas Excel writer and output the Excel file
writer.close()

print("Excel file created successfully!")
