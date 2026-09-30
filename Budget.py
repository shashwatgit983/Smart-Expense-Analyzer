# Budget Management System
def add_income(income_list):
    amount = float(input("Enter income amount: "))
    source = input("Enter income source: ")

    income_list.append({
        "amount": amount,
        "source": source})
    print("Income added successfully.")

# FUNCTIONS FOR EXPENSES, BALANCE, CATEGORY SUMMARY, AND BUDGET MANAGEMENT
def add_expense(expense_list):
    amount = float(input("Enter expense amount: "))
    category = input("Enter category: ")
    note = input("Enter short note: ")

    expense_list.append({
        "amount": amount,
        "category": category,
        "note": note})
    print("Expense added successfully.")
# Functions for showing income, expenses, calculating balance, category summary, setting budget, and checking budget
def show_income(income_list):
    if len(income_list) == 0:
        print("No income records found.")
        return
    print("\n----- INCOME -----")
    total = 0
    for i in range(len(income_list)):
        print(i + 1, ".", income_list[i]["source"],
              "-", income_list[i]["amount"])

        total += income_list[i]["amount"]
    print("Total Income:", total)

def show_expenses(expense_list):
    if len(expense_list) == 0:
        print("No expense records found.")
        return
    print("\n----- EXPENSES -----")
    total = 0
    for i in range(len(expense_list)):
        print(i + 1, ".", expense_list[i]["category"],
              "-", expense_list[i]["amount"],
              "-", expense_list[i]["note"])
        total += expense_list[i]["amount"]
    print("Total Expenses:", total)

def calculate_balance(income_list, expense_list):
    total_income = 0
    total_expense = 0
    for item in income_list:
        total_income += item["amount"]
    for item in expense_list:
        total_expense += item["amount"]
    balance = total_income - total_expense
    print("\n----- BALANCE -----")
    print("Total Income:", total_income)
    print("Total Expenses:", total_expense)
    print("Remaining Balance:", balance)

def category_summary(expense_list):
    if len(expense_list) == 0:
        print("No expenses available.")
        return
    categories = {}
    for item in expense_list:
        category = item["category"]
        if category in categories:
            categories[category] += item["amount"]
        else:
            categories[category] = item["amount"]
    print("\n----- CATEGORY SUMMARY -----")
    for category in categories:
        print(category, ":", categories[category])

def set_budget():
    amount = float(input("Enter your monthly budget: "))
    return amount

def check_budget(expense_list, budget):
    total = 0
    for item in expense_list:
        total += item["amount"]
    print("\n----- BUDGET STATUS -----")
    print("Budget:", budget)
    print("Spent:", total)
    if budget == 0:
        print("Budget has not been set.")
    elif total > budget:
        print("Warning: You have exceeded your budget!")
    else:
        print("Budget is under control.")
        print("Amount left:", budget - total)