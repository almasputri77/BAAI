#
# Almas, 2025/10/20
# File: Inventory_Reorder_System.py
# Short description of the task
#

import pandas as pd

# 1. Input
df = pd.read_excel ('inventory.xlsx') 

# 2. Process
total_cost = 0                                          #define base value
reorder_list = []          
good_stock_list = []       

# (Loop through each product)
for index, row in df.iterrows():
    product_name = row['Product_Name']
    current_stock = row['Current_Stock']
    minimum_stock = row['Minimum_Stock']
    unit_price = row['Unit_Price']

# *Check if the current stock is below the minimum stock
# *If yes, calculate reorder quantity (minimum stock - current stock + 10 safety buffer)
# *Calculate total reorder cost

    if current_stock < minimum_stock:
        reorder_quantity = (minimum_stock - current_stock) + 10
        reorder_cost = reorder_quantity * unit_price
        total_cost = total_cost + reorder_cost

# (Save the reorder info in a list)
        reorder_list.append(f"{product_name}: Reorder {reorder_quantity} units | Cost: ${reorder_cost:,.0f}")  
    else:
        good_stock_list.append(product_name)                # (Save product names that are in good stock)
        

# 3. Output
print("INVENTORY REORDER REPORT")
print("=========================\n")

print("Products Needing Reorder:")
print("--------------------------")

# (Print all products that need reorder)
for item in reorder_list:
    print(item)

# (Print total reorder cost)
print("\nTotal Reorder Cost: $", f"{total_cost:,.0f}")

# (Print products that are in good stock)
if len(good_stock_list) > 0:
    print("Products in Good Stock:", ", ".join(good_stock_list))
else:
    print("No products with sufficient stock.")