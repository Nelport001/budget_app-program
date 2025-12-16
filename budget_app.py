from datetime import date
VALID_TYPE = {"income", "expense"}
MIN_AMOUNT = 0.01
class Transaction:
    def __init__(self, amount, category, transaction_date, type_):
                if amount < MIN_AMOUNT:
                        raise ValueError("amount must be positive")
                if type_ not in VALID_TYPE:
                        raise ValueError("Type must be income or expense")
                if not category.strip():
                        raise ValueError("Category can't be empty")
                self.amount = float(amount)
                self.category = category.strip()
                self.date = transaction_date
                self.type = type_
    def __str__(self):
            return f"{self.date} | {self.type.upper()} | {self.category.title()} | ${self.amount}"

def add_transactions(transactions):
        while True:
            trans_date = input("Date: ")
            transaction_type = input("Type (income/expense): ")
            transaction_category = input("Category: ")
            transaction_amount = float(input("Amount: "))
            t = Transaction(transaction_amount, transaction_category, trans_date, transaction_type)
            transactions.append(t)
            # for trans in transactions:
            #     print(trans)
            break
def total_income(transactions):
        total = 0.0
        for t in transactions:
            if t.type == "income":
                total += t.amount
        return total
def total_expense(transactions):
        total = 0.0
        for t in transactions:
            if t.type == "expense":
                total += t.amount
        return total
      
def all_transactions(transactions):
      for trans in transactions:
            print(trans)

def cash_flow(transactions):
      return total_income(transactions) - total_expense(transactions)
      

def main():
    transactions = []
    while True:
        choice = input("\n1) Add transaction 2) All transactions 3) Finish: ").strip()
        if choice == '2':
            all_transactions(transactions)
        elif choice == '1':
            add_transactions(transactions)
        elif choice == '3':
              break
    print("---SUMMARY---")
    print("Total income: ", total_income(transactions))
    print("Total expenses", total_expense(transactions))
    print("Cash flow", cash_flow(transactions))
          

main()

