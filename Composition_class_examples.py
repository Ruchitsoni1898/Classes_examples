import random

class Databasehelper:
    def __init__(self,database_address,username,password):
        self.connection = "Connection Suceessfully"
    def write_to_db(self):
        print("Writing....")
    def read_from_db(self):
        print("read...")
class Authelper:
    pass


# example of Composition
class Account (Databasehelper):
    def __init__(self,user_id,database_address,username,password,Currency = "USD"):
        super().__init__(database_address,username,password)
        self.user_id = user_id
        self.Currency = Currency
        self.current_balance = self.__read_balance_from_database()
        print(f"Current Balance is:{self.current_balance}")
        self.db_helper = Databasehelper(database_address,username,password)
        self.auth = Authelper()
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
       self.db_helper.read_from_db()
       return random.randint(100,1000)
    def __write_balance_to_db(self):
       print("saving to db....")
       self.db_helper.write_to_db()

    myacct = Account(...)