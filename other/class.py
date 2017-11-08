#!/usr/bin/env python3

import numpy as np 

class Bag:
    def __init__(self):
        self.data = []

    def add(self,x):
        self.data.append(x)

    def print(self):
        print(self.data)

    def get(self):
        return self.data
        
    def addtwice(self,x):
        self.add(x)
        self.add(x)

x = Bag()

x.add(1)




print(x.get())

#print(x.get())