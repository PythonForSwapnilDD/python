class BookStore:

    NOB= 3;

    def __init__(self,name,auther):
        self.name=name
        self.author=auther
        BookStore.NOB+=1


    def Display(self):
        print("BOOK IS:{0} \n".format(self.name,self.author,self.NOB))
        print("AUTHOR IS:{1} \n".format(self.name, self.author, self.NOB))
        print("NOB:{2} \n".format(self.name, self.author, self.NOB))


def main():

    Obj1 = BookStore('DATA STRUCTURE AND ALGORITHEM','KURUMUNCHI')
    Obj1.Display()
    Obj2 = BookStore('C PROGRAMMING', 'DENNIS RITCHE')
    Obj2.Display()
    Obj3 = BookStore('PYTHON BOOK', 'DAVE KULHMAN')
    Obj3.Display()

if __name__ == "__main__":
    main()
