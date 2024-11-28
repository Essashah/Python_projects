import matplotlib.pyplot as plt

# Class to represent a single expense
class Expense:
    def __init__(self, category, amount, date):
        self.category = category
        self.amount = amount
        self.date = date

# Expense Tracker class to manage multiple expenses
class ExpenseTracker:
    def __init__(self):
        self.expenses = []  # List to store expenses

    def add_expense(self):
        print("\n--- Add Expense ---")
        category = input("Enter category (e.g., Food, Rent, Utilities): ")
        amount = float(input("Enter amount: "))
        date = input("Enter date (YYYY-MM-DD): ")
        new_expense = Expense(category, amount, date)
        self.expenses.append(new_expense)
        print(f"Expense added: {category} - ${amount} on {date}")

    def view_expenses(self):
        if not self.expenses:
            print("\nNo expenses recorded yet!")
            return
        print("\n--- All Expenses ---")
        for i, expense in enumerate(self.expenses, start=1):
            print(f"{i}. {expense.category} - ${expense.amount} on {expense.date}")

    def visualize_expenses(self):
        if not self.expenses:
            print("\nNo expenses to visualize!")
            return

        print("\n--- Expense Visualization ---")
        print("1. Bar Chart")
        print("2. Pie Chart")
        choice = input("Choose an option (1-2): ")

        # Organize data by category
        category_totals = {}
        for expense in self.expenses:
            if expense.category in category_totals:
                category_totals[expense.category] += expense.amount
            else:
                category_totals[expense.category] = expense.amount

        categories = list(category_totals.keys())
        amounts = list(category_totals.values())

        if choice == "1":
            # Bar Chart
            plt.bar(categories, amounts, color='skyblue')
            plt.xlabel("Category")
            plt.ylabel("Total Amount")
            plt.title("Expenses by Category")
            plt.show()
        elif choice == "2":
            # Pie Chart
            plt.pie(amounts, labels=categories, autopct="%1.1f%%", startangle=90)
            plt.title("Expenses by Category")
            plt.show()
        else:
            print("Invalid choice!")

    def exit_program(self):
        print("\nExiting the Expense Tracker. Goodbye!")
        exit()

# Main menu function
def main_menu():
    tracker = ExpenseTracker()  # Create an instance of ExpenseTracker

    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Visualize Expenses")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            tracker.add_expense()
        elif choice == "2":
            tracker.view_expenses()
        elif choice == "3":
            tracker.visualize_expenses()
        elif choice == "4":
            tracker.exit_program()
        else:
            print("Invalid choice! Please choose a valid option.")

# Run the program
if __name__ == "__main__":
    main_menu()
