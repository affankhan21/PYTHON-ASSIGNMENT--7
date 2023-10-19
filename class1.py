class Book:
    def __init__(self,bid=101,bname="THE LINUX PROGRAMMING INTERFACE",price=750,author="MICHAEL KERISK"):

        self.bid=bid
        self.bname=bname
        self.price=price
        self.author=author
    def ShowBook(self):
        print("BOOK ID     : ",self.bid) 
        print("BOOK NAME   : ",self.bname)
        print("BOOK PRICE  : ",self.price)
        print("BOOK AUTHOR : ",self.author)
    def __del__(self):
        print("OBJECT DESTROYED !")
B1=Book()
B1.ShowBook()
B2=Book(102,"LET US C",450,"YASHWANT KANETKAR")    
B2.ShowBook()
B3=Book(103,"PROGRAMMING IN C",500,"AJAY MITTAL")  
B3.ShowBook()  
