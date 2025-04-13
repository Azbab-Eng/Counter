from bank_account import *
print("\n**********Bank Account**********")

Dele = BankAccount("Dele",2000)
Tola = BankAccount("Tola",1000)
Dele.get_balance()
Dele.deposite(1000)
# Dele.withdraw(4000)
Dele.withdraw(1000)
Dele.transfer(1000,Tola)
Dele.transfer(1000,Tola)
Tola.transfer(1000,Dele)
Dele.transfer(1000,Tola)
Dele.transfer(1000,Tola)