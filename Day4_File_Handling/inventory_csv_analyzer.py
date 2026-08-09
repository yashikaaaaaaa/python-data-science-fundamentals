import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "datasets"

DATA_DIR.mkdir(exist_ok=True)

FILE_PATH = DATA_DIR / "inventory.csv"

inventory = [
    ["Laptop", 65000, 12],
    ["Smartphone", 30000, 25],
    ["Headphones", 2500, 40],
    ["Keyboard", 1800, 15],
    ["Monitor", 15000, 10]
]

# Create inventory CSV
with open(FILE_PATH, "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    writer.writerow(["Product", "Price", "Quantity"])
    writer.writerows(inventory)

total_value = 0
low_stock = []

# Analyze inventory
with open(FILE_PATH, "r", encoding="utf-8") as file:

    reader = csv.DictReader(file)

    print("=" * 70)
    print("                 INVENTORY CSV ANALYZER")
    print("=" * 70)

    print("\nProduct Inventory")
    print("-" * 70)

    for row in reader:

        product = row["Product"]
        price = float(row["Price"])
        quantity = int(row["Quantity"])

        inventory_value = price * quantity

        total_value += inventory_value

        if quantity < 20:
            low_stock.append(product)

        print(
            f"{product:15} | "
            f"Stock: {quantity:2} | "
            f"Value: ₹{inventory_value:,.2f}"
        )

print("-" * 70)

print(f"Total Inventory Value : ₹{total_value:,.2f}")

if low_stock:
    print(
        "Low Stock Products    : "
        + ", ".join(low_stock)
    )
else:
    print("Low Stock Products    : None")

print(f"\nFile saved at: {FILE_PATH}")
print("=" * 70)