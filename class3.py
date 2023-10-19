class Shirt:
    def __init__(self,sid=22,sname="DENIM",stype="Formal",price=800,size="small"):
        self.sid=sid
        self.sname=sname
        self.stype=stype
        self.price=price
        self.size=size

    def Show(self):
        print("SHIRT ID     :",self.sid)
        print("SHIRT NAME   :",self.sname)
        print("SHIRT TYPE   :",self.stype)
        print("SHIRT PRICE  :",self.price)
        print("SHIRT SIZE   :",self.size)    
    def __del__(self):
        print("object destroyed")
s1=Shirt()
s1.Show()
s2=Shirt(13,"SILK","CASUAL",1200,"LARGE")
s2.Show()
s3=Shirt(14,"VELVET","CASUAL",3200,"EXTRA LARGE")
s3.Show()
            


