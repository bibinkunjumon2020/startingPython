class Bank:
    bank_name="HDFC Bank"
    balance=0
    def AccntMake(self,name,accnt_no,min_balance):
        self.name=name
        self.accnt_no=accnt_no
        self.min_balance=min_balance
        self.balance=min_balance
    def Withdraw(self,amt_with):
        if(self.balance-amt_with > self.min_balance):
            self.balance=self.balance-amt_with
            print("\n_____________________\n",self.bank_name, "\nAccnt.No : ", self.accnt_no, "\nCustomer Name : ", self.name,
                  "\nYour Account is Debited with Rs.", amt_with, "\nYour Accnt Balance = ", self.balance)
        else:
            print("\n_____________________\n",self.bank_name, "\nAccnt.No : ", self.accnt_no, "\nCustomer Name : ", self.name,self.bank_name,"\nYour Account balance is too low")
    def Deposit(self,amt_dep):
        self.balance = self.balance+amt_dep
        print("\n_____________________\n",self.bank_name,"\nAccnt.No : ",self.accnt_no,"\nCustomer Name : ",self.name,"\nYour Account is credited with Rs.",amt_dep,"\nYour Accnt Balance = ", self.balance)

cust1=Bank()
cust1.AccntMake("Bibin",1234,5000)

cust1.Deposit(4000)

cust1.Withdraw(2000)

cust1.Withdraw(10000)