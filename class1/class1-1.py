# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 13:46:11 2020

@author: eric
"""

import random

num = random.randrange(1, 2)

try:
    eric = int(input("請輸入一個數字: "))
    
    if num == eric:
        print("成功了！")
except:
    print("只能輸入整數")

