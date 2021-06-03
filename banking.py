import datetime as dt




#timestamp=""
class Transaction:

    def __init__(self,amount,timestamp=None):
        self.amount=int(amount)
        self.timestamp=timestamp
        #self.timestamp=timestamp
        if timestamp==None:
            self.timestamp=dt.datetime.now()
        else:
            self.timestamp = timestamp

        #if self.timestamp==None:

    def __str__(self):
        return f'{self.timestamp}: {self.amount}'

    def __repr__(self):
        return f'Transaction({self.amount})'





class Account:
    """First Class Returns balance"""
    transactions=[]
    def __init__(self,amount):
        self.amount=amount


    	#A list of Transaction instances
    if not isinstance(amount, int):
        raise TypeError('Please provide a integer argument')

    def __repr__(self):
        return f'account.deposit(300)'




    def get_balance(self):
        account=Account
        if account.transactions==[]:
            return f'{0}'
        else:
            return f'{sum(account.transactions)}'
              #A method which returns the account balance
    def deposit(self): 	#A method which creates a deposit transaction

        account=Account
        converted_var_amount=abs(amount)
        if abs(amount):
            account.transactions.append(converted_var_amount)
        #def __repr__(self):
            trans2_deposit=account.transactions
            return trans2_deposit
            #dep_inst_tran = Transaction(amount)
            #return f'deposit({amount})'

        def __str__(self):
            dep_inst_tran = Transaction(amount)

            return f'{dep_inst_tran}:You deposited {amount}'
        def __repr__(self):
            return f'deposit({self.amount})'

    def withdraw(self,amount):#A method which creates a withdrawal transaction
        account=Account
        converted_var_amount=-abs(amount)
        if -abs(amount):
            withdraw_amount= sum(converted_var_amount)

            dep_inst_tran = Transaction(withdraw_amount)
            return f'{sum(account.transactions)+sum(withdraw_amount)}'

        else:
            return f'Must be positve number value'

        def __repr__(self):
            dep_inst_tran = Transaction(withdraw_amount)
            return f'withdraw({amount})'

        def __str__(self):
            dep_inst_tran = Transaction(withdraw_amount)
            return f'{dep_inst_tran}You withdrawn{amount}'








    #def __eq__(self,other):
    #    return self.amount == 'Transaction(100)'

    #def __str__(self):
        #return f'{self.amount}'

## MAIN PROGRAM ##

#transaction=Transaction(100,timestamp=None)



#if timestamp == None:
#    timestamp=dt.datetime.now()


'''def get_balance(self):
        def __init__(self,datetime):
            self.transactions=[]
        def __str__(self):
            return f'{self.timestamp}:{sum(self.transactions)}'
        def __repr__(self,datetime):
            return f''



    def timestamp(self,transaction,date_now):
        def __init__(self,transaction,date_now):
            self.transaction=transaction
            self.date_now=date_now
        def __str__(self):
            return f"{self.transaction}:{self.date_now}"


account=Account

transaction=Transaction
'''
