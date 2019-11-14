class Number:

    def __init__(self,value):
        self.value=value


    def ChkPrime(self):
        n=self.value
        if (n <= 1):
            return False
        if (n <= 3):
            return True

            # This is checked so that we can skip
            # middle five numbers in below loop
        if (n % 2 == 0 or n % 3 == 0):
            return False

        i = 5
        while (i * i <= n):
            if (n % i == 0 or n % (i + 2) == 0):
                return False
            i = i + 6

        return True

    def ChkPerfect(self):
        n = self.value
        sum1 = 0
        for i in range(1, n):
            if (n % i == 0):
                sum1 = sum1 + i
        if (sum1 == n):
            return True
        else:
            return False
    def SumFactors(self):
        n = self.value
        sum1 = 0
        for i in range(1, n):
            if (n % i == 0):
                sum1 = sum1 + i
        return sum1

    def Factors(self):
        x=self.value
        lst=[]

        for i in range(1, x + 1):
            if x % i == 0:
                lst.append(i)
        return lst


def main():
    lst=[]
    num = int(input("ENTER NUMBER"))

    Obj1 =Number(num)

    print("NUMBER IS PRIME:{0}".format(Obj1.ChkPrime()))
    print("NUMBER IS PERFECT:{0}".format(Obj1.ChkPerfect()))
    print("SUM OF NUMBER OF FACTOR IS :{0}".format(Obj1.SumFactors()))
    lst=Obj1.Factors()
    print("FACTOR ARE :{0}".format(lst))

    num = int(input("ENTER NUMBER"))

    Obj2 =Number(num)
    
    print("NUMBER IS PRIME:{0}".format(Obj1.ChkPrime()))
    print("NUMBER IS PERFECT:{0}".format(Obj1.ChkPerfect()))
    print("SUM OF NUMBER OF FACTOR IS :{0}".format(Obj1.SumFactors()))
    lst = Obj2.Factors()
    print("FACTOR ARE :{0}".format(lst))





if __name__=="__main__":
    main()
