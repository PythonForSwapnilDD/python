class Demo():

    value=10;

    def __init__(self,no1,no2):
        self.a=no1
        self.b=no2

    def fun(self):
        print(self.a)
        print(self.b)

    def gun(self):
        print(self.a)
        print(self.b)

def main():

    obj1=Demo(11,21)
    obj2=Demo(51,101)

    obj1.fun()
    obj2.fun()
    obj1.gun()
    obj2.gun()

if __name__ == "__main__":
    main()
