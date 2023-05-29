# testFile.py

import pytest

from OrderQueue import *

def test_pizza():
    
    # orders and pizza (test cases)
    cp1 = CustomPizza('S')
    cp1.addTopping('extra cheese')
    sp1 = SpecialtyPizza('L', 'Carne-more')
    order1 = PizzaOrder(12300)
    order1.addPizza(cp1)
    order1.addPizza(sp1)

    cp2 = CustomPizza('L')
    cp2.addTopping('sausage')
    sp2 = SpecialtyPizza('M', 'Hawaiian')
    order2 = PizzaOrder(9000)
    order2.addPizza(cp1)
    order2.addPizza(sp1)

    cp3 = CustomPizza('M')
    cp3.addTopping('chicken')
    sp3 = SpecialtyPizza('S', 'BBQ')
    order3 = PizzaOrder(11000)
    order3.addPizza(cp3)
    order3.addPizza(sp3)

    # OrderQueue testing
    bh = OrderQueue()
    bh.addOrder(order1)
    bh.addOrder(order2)
    print(bh.processNextOrder())
    print(bh.processNextOrder())

    #edgecase
    with pytest.raises(QueueEmptyException):
        heap = OrderQueue()
        heap.processNextOrder()

