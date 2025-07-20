from utils import (
    add_expense,
    read_all_expenses,
    calculate_total,
    filter_by_date,
    filter_by_category,
    format_expense
)

def handle_add_expense():
    date = input('Sanani kiritng: ')
    category = input('Kategoriya: ')
    amount = input('Summani kiriting: ')
    add_expense(date,category,amount)
    print("Xarajot qo'shildi !")

def handle_view_all():
    expenses = read_all_expenses()
    if not  expenses:
        print("Xarajatlar yo'q")
    else:
        print('Barcha xarajatlaringiz:')    
        for exp in expenses:
            print(format_expense(exp))

def handle_total():
    expenses = read_all_expenses()
    total = calculate_total(expenses)
    print("Umumiy xarajat - {total} so'm")

def handle_filter_by_date():
    search_date = input('Qaysi sana: ')
    expenses = read_all_expenses()
    filtered = filter_by_date(expenses,search_date)
    if not filtered:
        print("No'malum sana ")
    else:
        print(f'{search_date} uchun xarajatlar')
        for exp in expenses:
            print(format_expense(exp))     


def handle_filter_by_category():
    search_category = input('Kategoriyani kiriting: ')
    expenses = read_all_expenses()
    filtered = filter_by_category(expenses,search_category)
    if not filtered:
        print('Bu kategoriya xarajati topilmadi')
    else:
        print(f'{search_category} uchun xarajatlar')
        for exp in expenses:
            print(format_expense(exp))    

def main():
    while True:
        print("\n📋 Expense Tracker")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Expenses")
        print("4. Filter by Date")
        print("5. Filter by Category")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            handle_add_expense()
        elif choice == "2":
            handle_view_all()
        elif choice == "3":
            handle_total()
        elif choice == "4":
            handle_filter_by_date()
        elif choice == "5":
            handle_filter_by_category()
        elif choice == "6":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()