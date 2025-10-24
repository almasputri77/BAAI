#
# Almas, 2025/10/19
# File: Sales_Performance_Analyzer.py
# Short description of the task
#


import pandas as pd

# 1. Input
df = pd.read_excel ('sales_data.xlsx')                  # Load the Excel

# 2. Process
total_bonus = 0                                         # Define base value
report= []                                              # List to store each employee’s result line

# (Loop through each product)
for index, row in df.iterrows():                        #df.iterrows()= loop through each row.
    name = row['Employee_Name']
    sales = row['Monthly_Sales']
    target = row['Sales_Target']

    # *Calculate if each employee met their target (Yes/No)
    # *Calculate bonus: 10% of sales if target met, 5% if not met
    if sales >= target:
        target_status = "Target MET"
        bonus = 0.10 * sales    # 10% bonus if met
    else:
        target_status = "Target NOT MET"
        bonus = 0.05 * sales    # 5% bonus if not met

    # (Add to total)
    total_bonus += bonus

    # (Save the formatted output)
    report.append(f"{name}: {target_status} | Sales: ${sales:,.0f} | Bonus: ${bonus:,.0f}")

# 3. Output
print("SALES PERFORMANCE REPORT")
print("=========================\n")

# Print each employee's performance info
for line in report:
    print(line)

# Print total bonuses
print(f"\nTotal Bonuses to Pay: ${total_bonus:,.0f}")