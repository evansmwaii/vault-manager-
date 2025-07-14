                                                                                                                                                                                                                                                                                                                          
import json

# Load saved data
def load_expenses():
    global expenses
    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
    except FileNotFoundError:
        expenses = []

# Save data to file
def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)

# Add a new expense or income
def add_entry():
    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category (e.g. food, rent, salary): ")
        description = input("Enter description: ")
        entry = {
            "amount": amount,
            "category": category,
            "description": description
        }
        expenses.append(entry)
        save_expenses()
        print("Entry added.")
    except ValueError:
        print("Please enter a valid number.")

# Show all entries
def view_entries():
    if not expenses:
        print("No entries yet.")
    else:
        for i, entry in enumerate(expenses, 1):
            sign = "+" if entry['amount'] >= 0 else "-"
            print(f"{i}. {sign}${abs(entry['amount'])} | {entry['category']} | {entry['description']}")

# Show balance
def show_balance():
    total = sum(entry['amount'] for entry in expenses)
    print(f"💰 Current Balance: ${total:.2f}")

# Menu loop
def show_menu():
    print("\nExpense Tracker")
    print("1. View entries")
    print("2. Add entry")
    print("3. Show balance")
    print("4. Exit")

# Load data and run
expenses = []
load_expenses()

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        view_entries()
    elif choice == "2":
        add_entry()
    elif choice == "3":
        show_balance()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")



