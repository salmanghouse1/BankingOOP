class Account:
    """First Class Returns balance"""
    def get_balance(self,date_today):
        def __init__(self):
            self.balance=int(0)
            self.transactions=[]
            self.datetime=date_today
        def __str__(self):
            return f'{self.datetime}:{self.balance}'
