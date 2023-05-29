# OrderQueue.py

from PizzaOrder import *

class OrderQueue():
    ''' an OrderQueue type object stores PizzaOrder objects in a list formatted via MinHeap '''
    def __init__(self):
        self.heaplist = [0]
        self.currentSize = 0
    def percUp(self, i):
        while i // 2 > 0:
            if self.heaplist[i].getTime() < self.heaplist[i // 2].getTime():
                temp = self.heaplist[i // 2]
                self.heaplist[i // 2] = self.heaplist[i]
                self.heaplist[i] = temp
            i = i // 2
            
    def addOrder(self, pizzaOrder):
        self.heaplist.append(pizzaOrder)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heaplist[i].getTime() > self.heaplist[mc].getTime():
                temp = self.heaplist[i]
                self.heaplist[i] = self.heaplist[mc]
                self.heaplist[mc] = temp
            i = mc

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heaplist[i*2].getTime() < self.heaplist[i*2+1].getTime():
                return i * 2
            else:
                return i * 2 + 1
    
    def processNextOrder(self):
        ''' uses heaplist attribute to return the first PizzaOrder and remove it from the OrderQueue '''
        if self.heaplist == [0]:
            raise QueueEmptyException()
        else:
            order = self.heaplist[1]
            self.heaplist[1] = self.heaplist[self.currentSize]
            self.currentSize = self.currentSize - 1
            self.heaplist.pop()
            self.percDown(1)
            return order.getOrderDescription()

class QueueEmptyException(Exception):
        pass




