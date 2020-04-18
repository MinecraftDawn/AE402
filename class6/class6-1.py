# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 13:55:14 2020

@author: eric
"""

class Car:
    def __init__(self):
        self.color = "BLACK"
        self.size = 10
        print("init執行完了")
        
    def drive(self):
        print("往前走了100公尺")
        
myCar1 = Car()
myCar1.drive()
