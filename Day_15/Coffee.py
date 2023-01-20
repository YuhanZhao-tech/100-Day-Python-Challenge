#
class CoffeeMachine():
    _stock = {'water': 1500, 'coffee': 500, 'milk': 3000}
    
    def __init__(self):
        pass
    
    
    def check_stock(self, water, coffee, milk) -> bool:
        """Returns True if out of stock"""
        return water >= self._stock['water'] or coffee >= self._stock['coffee'] or milk >= self._stock['milk']
    
    def use(self, water=0, coffee=0, milk=0) -> None:
        self._stock['water'] -= water
        self._stock['coffee'] -= coffee
        self._stock['milk'] -= milk
        
        
    def make(self):
        while True:
            options = {'1': Espresso, '2': Latte, '3': Cappuccino}
            coffee = options[input("Hi, Would you like to have a cup of coffee? enter '1' for Espresso, '2' for Latte, '3' for Cappuccino: ")]
            order = coffee(int(input("How many cups would you like?: ")))
            if self.check_stock(*order.calculate_use()):
                print("Out of stock!")
                return
            self.use(*order.calculate_use())
            order.buy()
            print(self)
            

    def __str__(self):
        return f"Coffee machine. {self._stock}"



class Coffee():
    
    def __init__(self, quantity):
        self._quantity = quantity
        print("Buying {} cups of {}".format(quantity, self.__class__.__name__))
        
    
    def buy(self):
        confirm = {'y': True, 'n': False}[input(f"please enter 'y' to buy {self.__class__.__name__}: ")]
        if confirm:
            self.brew()
            print(f"Here is your {self.__class__.__name__} for ${self._price}")


    
class Espresso(Coffee):
    _water = 50
    _coffee = 18
    _price = 1.5
    
    def __init__(self, quantity):
        super().__init__(quantity)
        
    
    def brew(self):
        print(f"Mixing {self._water}ml of water with {self._coffee}g of coffee.")
        return self
    
    
    def calculate_use(self):
        return [self._water * self._quantity, self._coffee * self._quantity, 0]
    


class Latte(Coffee):
    _water = 200
    _coffee = 24
    _milk = 150
    _price = 2.5
    
    def __init__(self, quantity):
        super().__init__(quantity)
        
    
    def brew(self):
        print(f"Mixing {self._water}ml of water, {self._coffee}g of coffee and {self._milk}ml of milk.")
        return self
    
    def calculate_use(self):
        return [self._water * self._quantity, self._coffee * self._quantity, self._milk * self._quantity]
    
    
    
class Cappuccino(Coffee):
    _water = 250
    _coffee = 24
    _milk = 100
    _price = 3.0
    
    def __init__(self, quantity):
        super().__init__(quantity)
        

    def brew(self):
        print(f"Mixing {self._water}ml of water, {self._coffee}g of coffee and {self._milk}ml of milk.")
        return self
    
    def calculate_use(self):
        return [self._water * self._quantity, self._coffee * self._quantity, self._milk * self._quantity]
    
    
    
if __name__ == "__main__":
    
    # espresso = Espresso(5)
    # espresso.buy()

    # latte = Latte(5)
    # latte.buy()
    
    
    coffee_machine = CoffeeMachine()
    coffee_machine.make()