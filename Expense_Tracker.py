# Expense Tracker Application
class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    @staticmethod
    def welcome_message():
        print("Welcome to the Expense Tracker Application!")

    @staticmethod
    def show_menu():
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Exit")

    @staticmethod
    def enter_expense():
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        description = input("Enter description: ")
        return amount, category, description

    def add_expense(self, amount, category, description):
        expense = {
            'amount': amount,
            'category': category,
            'description': description
        }
        self.expenses.append(expense)
        print(f"Expense added successfully!")

    def view_expenses(self):
        print("Your Expenses:")
        print(f"{'Amount':<10} {'Category':<15} {'Description':<30}")
        print("-" * 55)
        for expense in self.expenses:
            print(f"{expense['amount']:<10} {expense['category']:<15} {expense['description']:<30}")

    def total_expenses(self):
        total = sum(expense['amount'] for expense in self.expenses)
        print(f"Total Expenses: {total}")

# Example usage
if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.welcome_message()

    while True:
        tracker.show_menu()
        choice = input("Enter your choice: ")
        
        match choice:
            case '1':
                amount, category, description = tracker.enter_expense()
                tracker.add_expense(amount, category, description)
            case '2':
                tracker.view_expenses()
            case '3':
                tracker.total_expenses()
            case '4':
                print("Exiting the application. Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")