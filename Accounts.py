import random
class Account (object):
    def __init__(self,user_id,Currency = "USD"):
        self.user_id = user_id
        self.Currency = Currency
        self.current_balance = self.__read_balance_from_database()
        print(f"Current Balance is:{self.current_balance}")
    def withdraw(self,Amount):
        self.current_balance = self.current_balance - float(Amount)
        print(f"New balance after Withdraw:{self.current_balance}")

    def Deposit (self,Amount):
        self.current_balance = self.current_balance - float(Amount)
        print(f"New balance after Deposit:{self.current_balance}")

    pass
    def generate_statement(self,start_date,end_date):
        pass
    def __read_balance_from_database(self):
       print(f"Getting balance from db for:{self.user_id}")
       return random.randint(100,1000)

account1 = Account(9871)

import pdb;pdb.set_trace()



