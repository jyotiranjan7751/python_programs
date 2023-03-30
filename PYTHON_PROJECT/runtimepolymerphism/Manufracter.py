class Manufracture:

    def sellLaptop(self):
        print("We manufacture all laptops")

class Dell(Manufracture):

    def sellLaptop(self):
        print("We sell Dell loptops")

class Hp(Manufracture):

    def sellLaptop(self):
        print("We sell Hp loptops")

class Lenovo(Manufracture):

    def sellLaptop(self):
        print("We sell Lenovo laptops")
        
class Flipkart:
    def sellEverything(self,m):
        m.sellLaptop()
f=Flipkart()      
d1=Dell()
f.sellEverything(d1)
hp1=Hp()
f.sellEverything(hp1)
lv=Lenovo()
f.sellEverything(lv)
