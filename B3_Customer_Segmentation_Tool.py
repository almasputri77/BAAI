#
# Almas, 2025/10/23
# File: Customer_Segmentation_Tool.py
# Short description of the task
#

import pandas as pd

# 1. Input
df = pd.read_excel ('customers.xlsx') 

# 2. Process
# Prepare lists to store categorized customers
vip_customers = []
regular_customers = []
new_customers = []

total_vip_revenue = 0                   #define base value

# (Loop through each customer)
for index, row in df.iterrows():
    name = row['Customer_Name']
    total_purchases = row['Total_Purchases']
    num_orders = row['Number_of_Orders']

    # *Calculate average order value
    avg_order = total_purchases / num_orders

    # *Categorize customer:
    if total_purchases > 10000:
        category = "VIP"
        vip_customers.append(f"- {name} | Total: ${total_purchases:,.0f} | Orders: {num_orders} | Avg Order: ${avg_order:,.2f}")
        total_vip_revenue += total_purchases
    elif total_purchases >= 5000:
        category = "Regular"
        regular_customers.append(f"- {name} | Total: ${total_purchases:,.0f} | Orders: {num_orders} | Avg Order: ${avg_order:,.2f}")
    else:
        category = "New"
        new_customers.append(f"- {name} | Total: ${total_purchases:,.0f} | Orders: {num_orders} | Avg Order: ${avg_order:,.2f}")

# 3. Output
print("CUSTOMER SEGMENTATION REPORT")
print("=============================\n")

# Print VIP customers
print("VIP Customers:")
print("============================")
if vip_customers:
    for c in vip_customers:
        print(c)
else:
    print("No VIP customers found.")

# Print Regular customers
print("\nRegular Customers:")
if regular_customers:
    for c in regular_customers:
        print(c)
else:
    print("No Regular customers found.")

# Print New customers
print("\nNew Customers:")
if new_customers:
    for c in new_customers:
        print(c)
else:
    print("No New customers found.")

# Print Total VIP Revenue
print("\nTotal VIP Revenue: $", f"{total_vip_revenue:,.0f}")
