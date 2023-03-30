class Kettle:

    def __init__(self, name, model, price, status):
        self.name = name
        self.model = model
        self.price = price
        self.status = status

    def showDetails(self):
        print(f"Kettle Name: {self.name}\nKettle Model: {self.model}\nKettle Price: {self.price}")
        print("===="*5)

    def switchOn(self):
        self.status = True

    def switchOff(self):
        self.status = False

        
k1 = Kettle("Philips", "B1", 1500, False)    
# k1.showDetails()
k2 = Kettle("Bosch", "B2", 2000, False)
# k2.showDetails()

# It will print all the kettle detils
l1 = [k1, k2]
for eachKettle in l1:
    eachKettle.showDetails()
    
print(k1.status)
k1.switchOn()
print(k1.status)
