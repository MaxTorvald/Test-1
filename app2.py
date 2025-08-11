#Today I'll create an Expense tracker CLI python application.
import argparse
import json
import os
import datetime
import streamlit as st
import sys

# Function to load expenses from a JSON file

def load_expenses(file_path):
    if not os.path.exists(file_path):
        return []
    with open(file_path, 'r') as file:
        return json.load(file)
    
# Function to save expenses to a JSON file

def save_expenses(file_path, expenses):
    with open(file_path, 'w') as file:
        json.dump(expenses,file, indent=4)

# Function to add a new expense

def add_expense(file_path, amount, category, description):
    expenses = load_expenses(file_path)
    new_expense = {
        "amount": amount,
        "category": category,
        "description": description,
        "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    expenses.append(new_expense)
    save_expenses(file_path, expenses)

# Function to view all expenses

def view_expenses(file_path):
    expenses = load_expenses(file_path)
    if not expenses:
        print("No expenses recorded.")
        return
    for expense in expenses:
        print(f"Date: {expense['date']}, Amoun: {expense['amount']}, Category: {expense['category']}, Description: {expense['description']}")
        if 'streamlit' in sys.modules:
            st.write(f"Date: {expense['date']}, Amount: {expense['amount']}, Category: {expense['category']}, Description: {expense['description']}")

# Function to insert a new expense

def insert_expense(file_path):
    st.title("Expense Tracker")
    st.subheader("Add a New Expense")
    amount = st.number_input("Amount (in USD)", min_value=0.01, format="%.2f")
    category = st.text_input("Category")
    description = st.text_input("Description")
    if st.button("Add Expense"):
        add_expense(file_path, amount, category, description)
        st.success("Expense added successfully!")
        if st.button("View All Expenses"):
            view_expenses(file_path)
            print("Expenses viewed successfully!")
        else:
            st.warning("No expenses to view yet.")
    else:
        st.warning("Please fill in all fields to add an expense.")

# Function to delete an expense

def delete_exepnse(file_path):
    st.title("Expense Tracker")
    st.subheader("Delete an Expense")
    expenses = load_expenses(file_path)
    if not expenses:
        st.warning("No expenses to delete.")
        return
    expense_to_delete = st.selection("Select an expense to delete", options=[f"{expense['date']} - {expense['amount']} - {expense['category']}" for expense in expenses])
    if st.button("Delete Expense"):
        if expense_to_delete:
            expenses.remove(expense_to_delete)
            save_expenses(file_path, expenses)
            st.success("Expense deleted successfully!")
        else:
            st.warning("Please select an expense to delete.")

# Main function to handle command line arguments and run the application

def main():
    parser = argparse.ArgumentParser(description="Expense Tracker CLI Application")
    parser.add_argument('--file', type=str, default='expenses.json', help='Path to the expenses JSON file')
    parser.add_argument('--add', action='store_true', help='Add a new expense')
    parser.add_argument('--view', action='store_true', help='View all expenses')
    parser.add_argument('--delete', action='store_true', help='Delete an expense')
    
    args = parser.parse_args()
    
    if args.add:
        insert_expense(args.file)
    elif args.view:
        view_expenses(args.file)
    elif args.delete:
        delete_exepnse(args.file)
    else:
        print("No action specified. Use --add, --view, or --delete.")

# Run the main function if this script is executed directly and without any problems

if __name__ == "__main__":
    if 'streamlit' in sys.modules:
        st.set_page_config(page_title="Expense Tracker", layout="wide")
        main()
    else:
        main()
        print("This script is intended to be run with streamlit. Please run it using 'streamlit run script_name.py'.")
        sys.exit(1)
        print("Expense Tracker CLI application")