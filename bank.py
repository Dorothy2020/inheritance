from datetime import datetime


class BankAccount:
    pin="ggh2034"
    AccountNumber=5432454
    from datetime import datetime


    def __init__(self,phone_number, name):
        self.phone_number=phone_number
        self.name=name
        self.balance=0
        self.statement=[]
        
       
    def save(self):
        return f"I will add 300 in my {self.fixed}"
    def withdraw(self):
        return f"I will withdraw 100 in my {self.balance}"
    def show_balance(self):
        return f"Hello,{self.name} your balance is {self.balance}"
    def deposit(self,amount):
        try:
            10+amount
        except TypeError:
            
                return f"The amount must be in figures"

        if amount<=0:
           return "you can nnot deposit"
        else:

          
            self.balance+=amount
            now=datetime.now()
            transaction={"amount":amount,"time":now,"Narration" :"you deposited"}
            self.statement.append(transaction)
        return self.show_balance()


        
    def withdraw(self,amount):
        try:
            10+amount
        except TypeError:
            return f"The amount must be in figures"
            
    
        if amount> self.balance:
            return f"Your balance is {self.balance} you cannot withdraw {amount}"

        else:
            self.balance-=amount
            now=datetime.now()
            transaction={"amount":"amount","time":now,"Narration" :"you deposited"}
            self.statement.append(transaction)
            return self.show_balance()
            

    # def s(self,amount):
       
    def show_statement(self):
            for transaction in self.statement:
                amount=transaction["amount"]
                narration=transaction["narration"]
                time=transaction["time"]
                date=time.strftime("%d/%m/%y")
                print(f"{date}: {narration} {amount}")
            return 

        # return f"Hello {self.name} you are borrowed {amount} "
    
    def repay(self,amount):
        try:
            10+amount
        except TypeError:
            return f"The amount must be in figures"
        return f"Hello {self.name} I have repaid {amount} "
    def transfer(self,account,amount, total):

            self.account=account
            self.amount=amount
            try:
                amount>0
            except TypeError:
                return f"Amount should be less than the balance"
            fee=amount*0.05
            total=amount+fee
            if amount<0:
                    return f"Your balance is {self.balance} and you need atleast{total} for this transfer"
            elif total>self.balance:
                return f"The total amount is greater than the amount"
            
            else:
                account.deposit()
                self.balance=total
                return f"The amount is greater than the balance"

class MobileMoney(BankAccount):
       def __init__(self,name,service_provider,phone_number):
        BankAccount.__init__(name,phone_number)
        self.name=name
        self.service_provider=service_provider
    
def airtime(self,amount):
    try:
        10+amount
    except TypeError:
        return f"She bought 50 shillings of airtime"
    if amount<0:
        return f"{self.name}"
    elif self.balance<amount:
        return f"She bought 50 shillings of airtime from her Mpesa"
    else:
        self.balance-=amount
        return f"The {amount} balance is less"

        
        

    



    
        
    

