class Arithmatic:

    def __init__(self):
        self.value1=0
        self.value2=0
    def Accept(self):
        print("ENTER 1ST NO:")
        self.value1=int(input())
        print("ENTER 2ND NO:")
        self.value2 = int(input())
    def Addition(self):
        return self.value1+self.value2
    def Subtraction(self):
        return self.value1-self.value2
    def Multiplication(self):
        return self.value1*self.value2
    def Division(self):
        return self.value1 / self.value2



def main():
    Obj1 = Arithmatic()
    Obj2 = Arithmatic()

    Obj1.Accept()
    print("ADDITION IS:{0} \n ".format(Obj1.Addition()))
    print("SUBSTRACTION IS:{0} \n ".format(Obj1.Subtraction()))
    print("MULTIPLICATION IS:{0} \n ".format(Obj1.Multiplication()))
    print("DIVISION IS:{0} \n ".format(Obj1.Division()))

    Obj2.Accept()
    print("ADDITION IS:{0} \n ".format(Obj2.Addition()))
    print("SUBSTRACTION IS:{0} \n ".format(Obj2.Subtraction()))
    print("MULTIPLICATION IS:{0} \n ".format(Obj2.Multiplication()))
    print("DIVISION IS:{0} \n ".format(Obj2.Division()))


if __name__=="__main__":
    main()
