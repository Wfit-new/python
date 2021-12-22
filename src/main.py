class StarBox:
    def __init__(self):
        self.stock = 100
        self.sell = 0
    def new_order(self, quantity):
        if quantity < self.stock:
            self.stock = self.stock - quantity
            self.sell = self.sell + 3.5*quantity
            print("thanks for buying coffee")
        else:
            print("Sorry! We are out of coffee")
            self.restock()
    def restock(self):
        self.stock = self.stock + 100
        print("Restocked. Updated stock", self.stock)

coffeeBar = StarBox()
coffeeBar.new_order(30)
coffeeBar.new_order(30)
coffeeBar.new_order(30)
coffeeBar.new_order(30)
coffeeBar.new_order(30)