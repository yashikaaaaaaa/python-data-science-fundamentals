sales = [
    ("Laptop", 2, 65000),
    ("Smartphone", 5, 30000),
    ("Headphones", 10, 2500),
    ("Keyboard", 8, 1800),
    ("Monitor", 4, 15000)
]

print("=" * 65)
print("                 SALES DATA ANALYZER")
print("=" * 65)

total_revenue = 0
total_units = 0

for product, quantity, price in sales:

    revenue = quantity * price

    total_units += quantity
    total_revenue += revenue

    print(
        f"{product:15} | "
        f"Units: {quantity:2} | "
        f"Revenue: ₹{revenue:,}"
    )

top_product = max(
    sales,
    key=lambda item: item[1] * item[2]
)

print("\n" + "-" * 65)
print(f"Total Units Sold    : {total_units}")
print(f"Total Revenue       : ₹{total_revenue:,}")
print(f"Top Revenue Product : {top_product[0]}")
print(f"Top Product Revenue : ₹{top_product[1] * top_product[2]:,}")
print("=" * 65)