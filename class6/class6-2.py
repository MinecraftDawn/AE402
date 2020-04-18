# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 14:05:51 2020

@author: eric
"""

class Animal:
    def __init__(self, HP):
        self.HP = HP
        
    def hurt(self, damage):
        self.HP -= damage
        print("剩下血量：" + str(self.HP))    
        

class Dog(Animal):
    def __init__(self, HP):
        super().__init__(HP)
        
    def howl(self):
        print("汪汪汪")
        
class Chihuahua(Dog):
    def __init__(self):
        super().__init__(1)
        
    def howl(self):
        print("挖挖挖挖挖挖")
        
        
myChi = Chihuahua()
myChi.howl()


