import os

FILENAME = "expenses.csv"

def add_expense(date, category, amount):
    with open('expenses.csv','a') as f:
        f.write(f'{date},{category},{amount}\n')



def read_all_expenses():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as file:
        lines = file.readlines()
        expenses = []
        for line in lines:
            parts = line.strip().split(",")
            if len(parts) == 3:
                date, category, amount = parts
                expenses.append({
                    "date": date,
                    "category": category,
                    "amount": float(amount)
                })
        return expenses

def calculate_total(expenses):
    total = 0
    for exp in expenses:
        total += exp["amount"]
    return total

def filter_by_date(expenses, search_date):
    result = []
    for exp in expenses:
        if exp['date'] == search_date:
            result.append(exp)
    
    return result        

def filter_by_category(expenses, search_category):
    result = []
    for exp in expenses:
        if exp['category'] == search_category:
            result.append(exp)
    
    return result
        

def format_expense(row):
    return f"{row['date']} | {row['category']} | {row['amount']} so'm"