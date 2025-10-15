#
# Almas, 2025/10/15
# File: Mini_Project.py
# Short description of the task
#

# 1. Input
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
def get_discount_rate(category, price):
    """Determine the discount rate based on category and price."""
    if category == "Electronics":
        if price >= 1000:
            return 0.20 # 20% discount
        elif price >= 500:
            return 0.15 # 15% discount
        else:
            return 0.10  # 10% discount
    elif category == "Clothing":
        if price >= 100:
            return 0.25 # 25% discount
        else:
            return 0.15 # 15% discount
    elif category == "Books":
        return 0.10 # 10% flat rate
    else:
        return 0.0
    

# Variables for summary
total_products = 0
total_original_price = 0
total_discount_amount = 0
total_final_price = 0

# Variables for bonus
highest_discount_product = None
highest_discount_value = 0
total_discount_percentage = 0
category_count = {}
most_expensive_product = None
cheapest_product = None

print("=== PRODUCT DISCOUNT CALCULATOR ===\n")

# Process each product
for product in products:
    name = product["name"]
    price = product["price"]
    category = product["category"]

    discount_rate = get_discount_rate(category, price)
    discount_amount = price * discount_rate
    final_price = price - discount_amount

    # Update summary
    total_products += 1
    total_original_price += price
    total_discount_amount += discount_amount
    total_final_price += final_price
    total_discount_percentage += discount_rate * 100

    # Level 1: Track highest discount
    if discount_amount > highest_discount_value:
        highest_discount_value = discount_amount
        highest_discount_product = product

    # Level 2: Count products by category
    if category not in category_count:
        category_count[category] = 0
    category_count[category] += 1

    # Level 2: Track most expensive and cheapest product after discount
    if most_expensive_product is None or final_price > most_expensive_product["final_price"]:
        most_expensive_product = {"name": name, "final_price": final_price}
    if cheapest_product is None or final_price < cheapest_product["final_price"]:
        cheapest_product = {"name": name, "final_price": final_price}

    # Level 3: Clearance tag for discount >= 20%
    clearance_tag = " [CLEARANCE]" if discount_rate >= 0.20 else ""

    # Print product details
    print(f"Product: {name}{clearance_tag}")
    print(f"  Category: {category}")
    print(f"  Original Price: ${price:.2f}")
    print(f"  Discount: {int(discount_rate * 100)}%")
    print(f"  Final Price: ${final_price:.2f}\n")

# === SUMMARY SECTION ===
print("=== SUMMARY ===")
print(f"Total Products: {total_products}")
print(f"Total Original Price: ${total_original_price:.2f}")
print(f"Total Discount: ${total_discount_amount:.2f}")
print(f"Total Final Price: ${total_final_price:.2f}")

# === BONUS CHALLENGES ===
print("\n=== BONUS CHALLENGES ===")

# Level 1
print(f"Product with Highest Discount: {highest_discount_product['name']} (${highest_discount_value:.2f})")
average_discount_percentage = total_discount_percentage / total_products
print(f"Average Discount Percentage: {average_discount_percentage:.2f}%")

# Level 2
print("\nProduct Count by Category:")
for cat, count in category_count.items():
    print(f"  {cat}: {count}")

print(f"Most Expensive Product After Discount: {most_expensive_product['name']} (${most_expensive_product['final_price']:.2f})")
print(f"Cheapest Product After Discount: {cheapest_product['name']} (${cheapest_product['final_price']:.2f})")

# Level 3
print(f"\nTotal Savings for Customer: ${total_discount_amount:.2f}")


# 3. Output


