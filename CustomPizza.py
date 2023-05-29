# CustomPizza.py

from Pizza import Pizza

class CustomPizza(Pizza):
    def __init__(self, size):
        Pizza.__init__(self, size)
        self.topping_list = []
        if self.size == 'S':
            self.price = 8.00
        elif self.size == 'M':
            self.price = 10.00
        elif self.size == 'L':
            self.price = 12.00
        
    def addTopping(self, topping):
        '''
        This function:
        1) adds topping to the CustomPizza's topping_list attribute
        2) adds the additional cost of a topping based on size
        '''
        self.topping_list.append(topping)
        if self.size == 'S':
            self.price += 0.50
        elif self.size == 'M':
            self.price += 0.75
        elif self.size == 'L':
            self.price += 1.00
        
    def getPizzaDetails(self):
        output = 'CUSTOM PIZZA' + '\n'
        output += f'Size: {self.size}' + '\n'
        output += f'Toppings:' + '\n'
        for topping in self.topping_list:
            output += '\t+ ' + f'{topping}' + '\n'
        output += f'Price: ${self.price:.2f}' + '\n'
        return output



        
        
        
        
