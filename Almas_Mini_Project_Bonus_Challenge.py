#
# Almas, 2025/10/15
# File: Mini_Project.py
# Mini Project_ Product Design Calculator
#

# 1. Input
# Product data
products = [
    {"name": "Laptop", "price": 1200, "category": "Electronics"},
    {"name": "Shirt", "price": 45, "category": "Clothing"},
    {"name": "Phone", "price": 800, "category": "Electronics"},
    {"name": "Shoes", "price": 120, "category": "Clothing"},
    {"name": "Tablet", "price": 350, "category": "Electronics"},
    {"name": "Jacket", "price": 95, "category": "Clothing"},
    {"name": "Book", "price": 25, "category": "Books"},
    {"name": "Headphones", "price": 150, "category": "Electronics"}
]

# 2. Process
# 1.) Initialize tracking variables
total_original = 0 
total_discount_amount = 0
total_final = 0

print("===PRODUCT DISCOUNT CALCULATOR===\n")

# 2.) Loop through products
for product in products:
    name = product["name"]
    price = product["price"]
    category = product["category"]

    # 3.) Determine discount
    if category == "Electronics":
        if price >= 1000:
            discount_rate = 0.20
        elif price >= 500:
            discount_rate = 0.15
        else:
            discount_rate = 0.10
    elif category == "Clothing":
        if price >= 100:
            discount_rate = 0.25
        else:
            discount_rate = 0.15
    elif category == "Books":
        discount_rate = 0.10
    else:
        discount_rate = 0.0

    # 3.) Calculate price
    discount_amount = price * discount_rate
    final_price = price - discount_amount

    total_original += price
    total_discount_amount += discount_amount
    total_final += final_price

    # 4.) Print product details
    print(f"Product: {name}")
    print(f"Category: {category}")                      #f = floating point (decimal number)
    print(f"Original Price: ${price:.2f}")              #2f = 2numbers after coma        
    print(f"Discount: {int(discount_rate * 100)}%")     #int change the float (decimal) to an integer
    print(f"Final Price: ${final_price:.2f}\n")         #\n = new line

# 5.) Generate summary
print("===SUMMARY===")
print(f"Total Products: {len(products)}")               #len = number of elements in a list (string)
print(f"Total Original Price: ${total_original:.2f}")  
print(f"Total Discount: ${total_discount_amount:.2f}")
print(f"Total Final Price: ${total_final:.2f}")


# BONUS CHALLENGES
print("\n===BONUS CHALLENGES===\n")
# Level 1
print("Level 1\n")

# 1) Find and display the product with the highest discount amount
highest_discount_product = None
total_discount_percentage = 0

for product in products:
    price = product["price"]
    category = product["category"]

    # Tentukan discount rate
    if category == "Electronics":
        if price >= 1000:
            discount_rate = 0.20
        elif price >= 500:
            discount_rate = 0.15
        else:
            discount_rate = 0.10
    elif category == "Clothing":
        if price >= 100:
            discount_rate = 0.25
        else:
            discount_rate = 0.15
    elif category == "Books":
        discount_rate = 0.10
    else:
        discount_rate = 0.0

    discount_amount = price * discount_rate
    total_discount_percentage += discount_rate

    if highest_discount_product is None or discount_amount > highest_discount_product["discount_amount"]:
        highest_discount_product = {"name": product["name"], "discount_amount": discount_amount}

print(f"Product with Highest Discount: {highest_discount_product['name']} (${highest_discount_product['discount_amount']:.2f})")

# 2) Calculate the average discount percentage across all products
average_discount_percentage = (total_discount_percentage / len(products)) * 100
print(f"Average Discount Percentage: {average_discount_percentage:.2f}%")

# 3. Output


