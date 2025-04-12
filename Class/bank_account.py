class BankEcception(Exception):
    pass

class BankAccount:
    def __init__(self,accountName,initialAmount):
        self.name = accountName
        self.amount = initialAmount
        print(f"\n{self.name} Create new Account\nAmount = #{self.amount}")

    def get_balance(self):
        print(f"\n*******{self.name} Current Balance*******")
        print(f"\nAccount Name : {self.name}\nAmount = #{self.amount}")

    def deposite(self,amount):
        self.amount += amount
        print("\n*******Deposite in progress******🚀\n Deposite completed ✅")
        self.get_balance()

    def checkEligible(self,amount):
        if self.amount >= amount:
            return True
        raise BankEcception(f"\nSorry the Transaction cant be proccess due to current Balance #{self.amount}")
        
    def withdraw(self,amount):
        try:
            self.checkEligible(amount)
            self.amount -= amount
            print(f"\nTransaction in progress .....🚀")
            self.get_balance()
            print("Withdraw Completed ...✅")
        except BankEcception as error:
            print(f"\nCheck your current Balance, Withdraw cant be process ❌" , error)

    def transfer(self,amount,account):
        try:
            self.checkEligible(amount)
            self.withdraw(amount)
            account.deposite(amount)
            self.get_balance()
        except BankEcception as error:
            print(error)    
        finally:
            print("Thanks for using our Service")







    




