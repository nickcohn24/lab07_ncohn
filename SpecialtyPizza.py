# SpecialtyPizza.py

from Pizza import Pizza

class SpecialtyPizza(Pizza):
    ''' a SpecialtyPizza object is a child pizza class with name and size attributes; size determines its price attribute '''
    def __init__(self, size, name):
        Pizza.__init__(self, size)
        self.name = name
        if size == 'S':
            self.price = 12.00
        elif size == 'M':
            self.price = 14.00
        elif size == 'L':
            self.price = 16.00
    def getPizzaDetails(self):
        output = 'SPECIALTY PIZZA' + '\n'
        output += f'Size: {self.size}' + '\n'
        output += f'Name: {self.name}' + '\n'
        output += f'Price: ${self.price:.2f}' + '\n'
        return output
        
