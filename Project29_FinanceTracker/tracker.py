import sqlite3
import matplotlib.pyplot as plt
from datetime import datetime

class FinanceTracker:
    def __init__(self):
        # 1. Connect to (or create) the database
        self.conn = sqlite3.connect("finances.db")
        self.cursor = self.conn.cursor()
        self.setup_db()

    def setup_db(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS transactions 
                            (id INTEGER PRIMARY KEY, date TEXT, category TEXT, 
                             description TEXT, amount REAL, type TEXT)''')
        self.conn.commit()

    def add_transaction(self, category, desc, amount, t_type):
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute("INSERT INTO transactions (date, category, description, amount, type) VALUES (?, ?, ?, ?, ?)",
                            (date, category, desc, amount, t_type))
        self.conn.commit()
        print(f"✅ Recorded {t_type}: GHS {amount} for {desc}")

    def get_summary(self):
        self.cursor.execute("SELECT type, SUM(amount) FROM transactions GROUP BY type")
        summary = dict(self.cursor.fetchall())
        income = summary.get('Income', 0)
        expense = summary.get('Expense', 0)
        balance = income - expense
        
        print("\n" + "="*30)
        print(f"💰 TOTAL INCOME:  GHS {income:,.2f}")
        print(f"💸 TOTAL EXPENSE: GHS {expense:,.2f}")
        print(f"🏛️ NET BALANCE:   GHS {balance:,.2f}")
        print("="*30)

    def generate_chart(self):
        self.cursor.execute("SELECT category, SUM(amount) FROM transactions WHERE type='Expense' GROUP BY category")
        data = self.cursor.fetchall()
        
        if not data:
            print("No expenses to chart!")
            return

        categories = [row[0] for row in data]
        amounts = [row[1] for row in data]

        plt.figure(figsize=(8, 6))
        plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=140)
        plt.title("Spending Breakdown by Category")
        plt.show()

if __name__ == "__main__":
    tracker = FinanceTracker()
    
    while True:
        print("\n1. Add Income\n2. Add Expense\n3. View Summary\n4. Show Spending Chart\n5. Exit")
        choice = input("Select Action: ")

        if choice in ['1', '2']:
            t_type = "Income" if choice == '1' else "Expense"
            cat = input("Category (e.g., Food, Laptop Sale, Church): ")
            desc = input("Description: ")
            amt = float(input("Amount (GHS): "))
            tracker.add_transaction(cat, desc, amt, t_type)
        elif choice == '3':
            tracker.get_summary()
        elif choice == '4':
            tracker.generate_chart()
        elif choice == '5':
            break