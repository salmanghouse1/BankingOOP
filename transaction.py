class Transaction:
    def timestamp(self,transaction,date_now):
        def __init__(self,transaction,date_now):
            self.transaction=transaction
            self.date_now=date_now
        def __str__(self):
            return f"{self.transaction}:{self.date_now}"




















def deposit(self,amount):
    #append to transactions and use sum
    def __init__(self,amount):
        self.amount=amount

    def __repr__(self,amount):
        self.transactions.append(self.amount)
    def __str__(self,amount):
        return f'{self.balance} \n {sum(self.transactions)}'

def withdraw(self,amount):
    def __init__(self,amount):
        self.amount=amount
    def __str__(self):
        return f'{self.amount-self.balance} \n {self.transactions.pop(self.amount)}'
