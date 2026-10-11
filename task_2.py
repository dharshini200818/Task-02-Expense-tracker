import csv
from datetime import datetime
f = "expenses.csv"
t = "totals.csv"
Header = ["date", "category", "amount"]
def validate_date(date):
          try:
                    datetime.strptime(date, "%d-%m-%Y")
                    return True
          except ValueError:
                    return False
def validate_amount(amount):
          return amount > 0
def get_expense():
          while True:
                    date = input("Enter date (DD-MM-YYYY): ").strip()
                    if validate_date(date):
                              break
                    print("Invalid date. Please use DD-MM-YYYY format.")
          while True:
                    category = input("Enter category: ").strip()
                    if category:
                              break
                    print("Category cannot be empty.")
          while True:
                    try:
                              amount = float(input("Enter amount: "))
                              if validate_amount(amount):
                                        break
                              print("Amount must be greater than zero.")
                    except ValueError:
                              print("Please enter a valid number.")

          expense = {"date": date,"category": category,"amount": amount}
          return expense
def save_expense(expense):
          with open(f, "a", newline="", encoding="utf-8") as file:
                    writer = csv.DictWriter(file, fieldnames=Header)
                    writer.writerow(expense)
def calculate_totals():
          totals = {}
          with open(f, "r", newline="", encoding="utf-8") as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                              category = row["category"]
                              amount = float(row["amount"])
                              if category in totals:
                                        totals[category] += amount
                              else:
                                        totals[category] = amount
          return totals

def save_category_totals(totals):
          with open(t, "w", newline="", encoding="utf-8") as file:
                    fields = ["category", "total_amount"]
                    writer = csv.DictWriter(file, fieldnames=fields)
                    writer.writeheader()
                    for category, total in totals.items():
                              writer.writerow({
                                        "category": category,
                                        "total_amount": round(total, 2)
                              })
def main():
          while True:
                    expense = get_expense()
                    save_expense(expense)
                    print("Expense saved successfully!")
                    choice = input("Add another expense? (y/n): ").strip().lower()
                    if choice != "y":
                              break
          totals = calculate_totals()
          save_category_totals(totals)
          if totals:
                    for category, total in totals.items():
                              print(f"{category}: {total:.2f}")
          else:
                    print("No expenses recorded.")

if __name__ == "__main__":
          main()
