# PizzaOrder.py

from CustomPizza import *

from SpecialtyPizza import *

class PizzaOrder:
    ''' a PizzaOrder object that stores pizza type objects in its pizzas (list) attribute '''
    def __init__(self, time):
        self.time = time
        self.pizzas = []
    def getTime(self):
        return self.time
    def setTime(self, time):
        self.time = time
    def addPizza(self, pizza):
        self.pizzas.append(pizza)
    def getOrderDescription(self):
        output = '******\n' + f'Order Time: {self.time}' + '\n'
        total_price = 0
        for pizza in self.pizzas:
            total_price += pizza.getPrice()
            output += pizza.getPizzaDetails() + '\n----\n'
        output += f'TOTAL ORDER PRICE: ${total_price:.2f}' + '\n******\n'
        return output
