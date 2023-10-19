class Product:

    def __init__(self,pid=11,pname="PEN",price=20,quantity=2):
     self.pid=pid
     self.pname=pname
     self.price=price
     self.quantity=quantity

    def Show(self):
        print("PRODUCT ID       :",self.pid)
        print("PRODUCT NAME     :",self.pname)
        print("PRODUCT PRICE    :",self.price)
        print("PRODUCT QUANTITY :",self.quantity)

    def __del__(self):
        print("object destoyed")
P1=Product()
P1.Show()
P2=Product(12,"BOOK",45,6)
P2.Show()
P3=Product(13,"PENCIL",15,3) 
P3.Show()

