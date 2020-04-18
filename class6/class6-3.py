# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 14:20:28 2020

@author: eric
"""

class Human:
    def __init__(self, H, W):
        self.H = H
        self.W = W
        
    def BMI(self):
        bmi = self.W / (self.H / 100) ** 2
        print(bmi)
    
h = Human(181, 75)
h.BMI()