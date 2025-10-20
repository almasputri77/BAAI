#
# Almas, 2025/10/19
# File: Sales_Performance_Analyzer.py
# Short description of the task
#


import pandas as pd

# 1. Input
df = pd.read_excel ('sales_data.xlsx') 
status_list = []

# 2. Process
# Calculate if each employee met their target (Yes/No)          
for i in range(len(df)):
    if df.loc[i, 'Monthly_Sales'] >= df.loc[i, 'Sales_Target']:      #df.loc (row, column)
        df.loc[i, 'Target_Status'] = 'MET'
    else:
        df.loc[i, 'Target_Status'] = 'NOT MET'

# Calculate bonus: 10% of sales if target met, 5% if not met
for i in range(len(df)):
    sales = df.loc[i, 'Monthly_Sales']
    status = df.loc[i, 'Target_Status']
    if status == 'MET':
        df.loc[i, 'Bonus'] = sales * 0.10
    else:
        df.loc[i, 'Bonus'] = sales * 0.05

# 3. Output
print("SALES PERFORMANCE REPORT")
print("=========================")

total_bonus = 0
for i in range(len(df)):
    name = df.loc[i, 'Employee_Name']
    sales = df.loc[i, 'Monthly_Sales']
    status = df.loc[i, 'Target_Status']
    bonus = df.loc[i, 'Bonus']

    total_bonus += bonus

    print(f"{name}: Target {status} | Sales: ${sales:,.0f} | Bonus: ${bonus:,.0f}")

print()                                                                              #enter       
print(f"Total Bonuses to Pay: ${total_bonus:,.0f}")