# Main file
from data import expenses, income
import Budget

# functions
def menu():
    print("\n==============================")
    print("   PERSONAL BUDGET MANAGER")
    print("==============================")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Income")
    print("4. View Expenses")
    print("5. Show Balance")
    print("6. Category-wise Summary")
    print("7. Set Monthly Budget")
    print("8. Check Budget")
    print("9. Exit")
    print("==============================")

# functions
monthly_budget = 0
while True:
    menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        Budget.add_income(income)
    elif choice == "2":
        Budget.add_expense(expenses)
    elif choice == "3":
        Budget.show_income(income)
    elif choice == "4":
        Budget.show_expenses(expenses)
    elif choice == "5":
        Budget.calculate_balance(income, expenses)
    elif choice == "6":
        Budget.category_summary(expenses)
    elif choice == "7":
        monthly_budget = Budget.set_budget()
        print("Monthly budget saved.")
    elif choice == "8":
        Budget.check_budget(expenses, monthly_budget)
    elif choice == "9":
        print("Thank you for using Personal Budget Manager!")
        break
    else:
        print("Invalid choice. Please try again.")