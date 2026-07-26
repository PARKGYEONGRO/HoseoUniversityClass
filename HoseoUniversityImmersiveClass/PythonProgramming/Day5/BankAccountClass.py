class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f'{amount:,}원 입금 -> 잔액: {self.balance:,}원')
    def withdraw(self, amount):
        if amount > self.balance:
            print('잔액부족')
        else:
            self.balnce -= amount
            print(f'{amount:,}원 출금 -> 잔액 {self.balance:,}원')

BankAccounts = [
    BankAccount('홍길동'),
    BankAccount('김철수', 2000),
    BankAccount('신짱구', 4000)
]

total = sum(acc.balance for acc in BankAccounts)
print(f'은행 전체 예치 금액 {total:,}원')

BankAccounts[0].deposit(5000)
total = sum(acc.balance for acc in BankAccounts)
print(f'은행 전체 예치 금액 {total:,}원')