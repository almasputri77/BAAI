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
# Initialize tracking variables
total_original = 0
total_discount_amount = 0
total_final = 0

print("=== PRODUCT DISCOUNT CALCULATOR ===\n")

# Process each product
for product in products:
    name = product["name"]
    price = product["price"]
    category = product["category"]

    # Determine discount rate (NO FUNCTION)
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

    # Calculate discount and final price
    discount_amount = price * discount_rate
    final_price = price - discount_amount

    # Update totals
    total_original += price
    total_discount_amount += discount_amount
    total_final += final_price

    # Print product details
    print(f"Product: {name}")
    print(f"Category: {category}")
    print(f"Original Price: ${price:.2f}")
    print(f"Discount: {int(discount_rate * 100)}%")
    print(f"Final Price: ${final_price:.2f}\n")

# Print summary
print("=== SUMMARY ===")
print(f"Total Products: {len(products)}")
print(f"Total Original Price: ${total_original:.2f}")
print(f"Total Discount: ${total_discount_amount:.2f}")
print(f"Total Final Price: ${total_final:.2f}")


# 3. Output


