import csv
import os

FILE_NAME = "expenses.csv"
expenses = []

def initialize_file():
    """Create CSV file with headers if it does not exist"""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])

def add_expense():
    print("\nAdd Current Expense")
    date = input("Enter Date (YYYY-MM-DD): ")
    category = input("Enter Item Category: ")
    
    try:
        amount = float(input("Enter Amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    description = input("Description: ")

    expense = [date, category, amount, description]
    expenses.append(expense)

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(expense)

    print("Expense Added Successfully")

def menu():
    while True:
        print("\n--- Expense Tracker Menu ---")
        print("1. Add Expense")
        print("2. Exit")

        option = input("Select an option: ")

        if option == "1":
            add_expense()
        elif option == "2":
            print("Exiting program...")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    initialize_file()
    menu()
