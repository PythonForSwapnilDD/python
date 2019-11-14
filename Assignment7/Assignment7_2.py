class Bank():
    ROI=10.5;

    def __init__(self,custname,value):
      self.name=custname
      self.amount=value

    def Deposit(self,value):
        self.amount= self.amount + value

    def Widraw(self,value):
        self.amount= self.amount - value
    @classmethod
    def DisplayROI(cls):
        print(cls.ROI)
    @staticmethod
    def BankInfo():
        print("IT IS A NATIONALISED BANK OF INDIA")
        print("LOCATION IS PUNE")

def main():

    print("EMPLOYEES AND PAYMENT","\n")

    obj1 = Bank("AMAR",20000)
    print(obj1.name,obj1.amount)


    obj2 = Bank("ANJALI",30000)
    print(obj2.name,obj2.amount)

    obj3 = Bank("ANKIT",40000)
    print(obj3.name,obj3.amount)

    obj4 = Bank("AJAY",50000)
    print(obj4.name,obj4.amount)

    obj5 = Bank("AARTI",100000)
    print(obj5.name,obj5.amount,"\n")

    print("DEPOSITED MONEY:","\n")

    obj1.Deposit(2500)
    obj2.Deposit(3400)
    obj3.Deposit(2000)
    obj4.Deposit(5500)
    obj5.Deposit(2700)


    print(obj1.name,obj1.amount)
    print(obj2.name,obj2.amount)
    print(obj3.name,obj3.amount)
    print(obj4.name,obj4.amount)
    print(obj5.name,obj5.amount,"\n")

    print("WIDRAW MONEY:","\n")

    obj1.Widraw(1000)
    obj2.Widraw(2000)
    obj3.Widraw(3000)
    obj4.Widraw(4000)
    obj5.Widraw(5000)

    print(obj1.name,obj1.amount)
    print(obj2.name,obj2.amount)
    print(obj3.name,obj3.amount)
    print(obj4.name,obj4.amount)
    print(obj5.name,obj5.amount)

    Bank.DisplayROI()
    Bank.BankInfo()

if __name__ == "__main__":
    main()
