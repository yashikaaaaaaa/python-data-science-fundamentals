import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "datasets"

DATA_DIR.mkdir(exist_ok=True)

FILE_PATH = DATA_DIR / "expenses.csv"

expenses = [
    ["Food", 2500],
    ["Transport", 1200],
    ["Shopping", 4500],
    ["Bills", 3200],
    ["Entertainment", 1800],
    ["Food", 1700]
]

# Create expense CSV
with open(FILE_PATH, "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    writer.writerow(["Category", "Amount"])
    writer.writerows(expenses)

category_totals = {}
total_expense = 0

# Analyze expenses
with open(FILE_PATH, "r", encoding="utf-8") as file:

    reader = csv.DictReader(file)

    for row in reader:

        category = row["Category"]
        amount = float(row["Amount"])

        total_expense += amount

        if category not in category_totals:
            category_totals[category] = 0

        category_totals[category] += amount

highest_category = max(
    category_totals,
    key=category_totals.get
)

print("=" * 65)
print("                 EXPENSE ANALYZER")
print("=" * 65)

print("\nCategory-wise Expenses")
print("-" * 65)

for category, amount in category_totals.items():

    print(
        f"{category:18} : ₹{amount:,.2f}"
    )

print("-" * 65)
print(f"Total Expense       : ₹{total_expense:,.2f}")
print(f"Highest Category    : {highest_category}")
print(
    f"Highest Amount      : "
    f"₹{category_totals[highest_category]:,.2f}"
)

print(f"\nFile saved at: {FILE_PATH}")
print("=" * 65)