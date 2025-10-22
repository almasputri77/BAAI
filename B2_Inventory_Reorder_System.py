#
# Almas, 2025/10/20
# File: Inventory_Reorder_System.py
# Short description of the task
#

import pandas as pd

# 1. Input
df = pd.read_excel ('inventory.xlsx') 

# 2. Process
#Check if the current stock is below the minimum stock
for i in range(len(df)):

product_name = df.loc[i, 'Product_Name']
current_stock = df.loc[i, 'Current_Stock']
minimum_stock = df.loc[i, 'Minimum_Stock']   

if current_stock < minimum_stock:
    print(product_name, "needs reorder. Current stock:", current_stock, "| Minimum stock:", minimum_stock)
else:
    print(product_name, "is in good stock. Current stock:", current_stock, "| Minimum stock:", minimum_stock)

# 3. Output

3