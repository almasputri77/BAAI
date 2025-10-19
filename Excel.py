#
# Almas, 2025/10/08
# File: Excel.py
# Short description of the task
#

import pandas as pd

# 1. Input
df = pd.read_excel ('Financial_Sample1.xlsx') 

# 2. Process
sum = df.select_dtypes(include='number').sum()
sums = df.select_dtypes(include="number").sum()

# Optionally give a label for the row (e.g.'Total')
sums['Name'] = "Total" #Add value for the non- numeric.colomn

# Append the total of row to DataFrame
df_with_total = pd.concat ([df,pd.DataFrame([sums])], ignore_index=True)

# 3. Output
print(df_with_total)
df_with_total.to_excel('output.xlsx', Index=False)

