Personal Budget Manager
A simple command-line Personal Budget Manager written in Python. It allows users to record income and expenses, view financial records, calculate their remaining balance, summarize expenses by category, and manage a monthly budget.

Features
Add income with an amount and source.

Add expenses with an amount, category, and note.

View all recorded income and total income.

View all recorded expenses and total expenses.

Calculate the remaining balance.

View expenses grouped by category.

Set a monthly spending budget.

Check current spending against the monthly budget.

Simple interactive menu-driven interface.

Project Structure
.
├── main.py
├── Budget.py
├── data.py
└── README.md
main.py
The main program provides the interactive menu and calls the appropriate functions based on the user's choice. It supports options for adding/viewing income and expenses, checking the balance, viewing category summaries, and managing the monthly budget.

Budget.py
Contains the core budget-management functions, including:

add_income()

add_expense()

show_income()

show_expenses()

calculate_balance()

category_summary()

set_budget()

check_budget()

data.py
Stores the application's in-memory data lists:

income

expenses

budget

The current implementation starts with empty income and expense lists and a budget value of 0.

Requirements
Python 3.x

No external Python packages are required.

How to Run
Make sure Python 3 is installed.

Place main.py, Budget.py, and data.py in the same directory.

Open a terminal in the project directory.

Run:

python main.py
Usage
After starting the program, a menu is displayed:

1. Add Income
2. Add Expense
3. View Income
4. View Expenses
5. Show Balance
6. Category-wise Summary
7. Set Monthly Budget
8. Check Budget
9. Exit
Enter the number corresponding to the action you want to perform.

Example
To add income:

Enter your choice: 1
Enter income amount: 25000
Enter income source: Salary
Income added successfully.
To add an expense:

Enter your choice: 2
Enter expense amount: 500
Enter category: Food
Enter short note: Lunch
Expense added successfully.
You can then use the balance, category summary, and budget options to review your spending.

Data Storage
The current application stores income and expense records in Python lists while the program is running. The data is not persisted to a file or database, so records are lost when the program exits.

Budget Checking
The budget feature compares the total recorded expenses with the monthly budget:

If the budget is 0, the program reports that a budget has not been set.

If expenses exceed the budget, a warning is displayed.

Otherwise, the program reports that the budget is under control and shows the amount remaining.

Limitations
Data is stored only in memory.

There is no database or file-based persistence.

Input validation for invalid numbers or negative amounts is limited.

The application is currently command-line based.

There is no authentication or support for multiple users.

Future Improvements
Possible improvements include:

Save data using JSON, CSV, or SQLite.

Add input validation and error handling.

Prevent negative income, expenses, and budgets.

Add transaction deletion and editing.

Add date-based transaction tracking.

Generate monthly reports.

Add charts for spending categories.

Create a graphical user interface or web interface.

License
This project is provided for educational and personal use.