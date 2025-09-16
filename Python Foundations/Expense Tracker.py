# Function to add an expense (amount + category) to the expenses list
def add_expense(expenses, amount, category):
    # Append a dictionary with amount and category into the expenses list
    expenses.append({'amount': amount, 'category': category})
    

# Function to print all expenses
def print_expenses(expenses):
    # Loop through each expense dictionary in the list/iterator
    for expense in expenses:
        # Print out amount and category of each expense using f-string
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')
    

# Function to calculate total of all expenses
def total_expenses(expenses):
    # Use map() to extract only the 'amount' values, then sum() to total them
    return sum(map(lambda expense: expense['amount'], expenses))
    

# Function to filter expenses by a given category
def filter_expenses_by_category(expenses, category):
    # Return an iterator of only those expenses where the category matches
    return filter(lambda expense: expense['category'] == category, expenses)
    

# Main function to run the program (menu-driven interface)
def main():
    # List to hold all expense entries
    expenses = []
    
    # Infinite loop to keep showing the menu until user exits
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
       
        # Take user input for menu choice
        choice = input('Enter your choice: ')

        # If user chooses option 1 -> add an expense
        if choice == '1':
            # Input for amount (converted to float)
            amount = float(input('Enter amount: '))
            # Input for category (string)
            category = input('Enter category: ')
            # Call add_expense() to append the new expense
            add_expense(expenses, amount, category)

        # If user chooses option 2 -> show all expenses
        elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)
    
        # If user chooses option 3 -> show total of all expenses
        elif choice == '3':
            print('\nTotal Expenses: ', total_expenses(expenses))
    
        # If user chooses option 4 -> filter by category
        elif choice == '4':
            # Ask for category to filter
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            # Get filtered expenses (iterator)
            expenses_from_category = filter_expenses_by_category(expenses, category)
            # Print only the filtered expenses
            print_expenses(expenses_from_category)
    
        # If user chooses option 5 -> exit the program
        elif choice == '5':
            print('Exiting the program.')
            break

# Call the main() function to start the program
main()
