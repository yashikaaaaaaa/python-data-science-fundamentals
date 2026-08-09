inventory = {
    "Laptop": {
        "price": 65000,
        "stock": 12
    },
    "Smartphone": {
        "price": 30000,
        "stock": 25
    },
    "Headphones": {
        "price": 2500,
        "stock": 40
    },
    "Keyboard": {
        "price": 1800,
        "stock": 15
    }
}

print("=" * 60)
print("             INVENTORY MANAGEMENT SYSTEM")
print("=" * 60)

for product, details in inventory.items():
    print(
        f"{product:15} "
        f"Price: ₹{details['price']:>6} | "
        f"Stock: {details['stock']}"
    )

total_value = sum(
    details["price"] * details["stock"]
    for details in inventory.values()
)

low_stock = [
    product
    for product, details in inventory.items()
    if details["stock"] < 20
]

print("\n" + "-" * 60)
print(f"Total Inventory Value : ₹{total_value:,}")
print(f"Low Stock Products    : {', '.join(low_stock)}")
print("=" * 60)