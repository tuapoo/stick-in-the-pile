# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 23:18:11 2022

@author: tuapoo
"""

import numpy as np
DMT=int(input("dimension of array : "))
arr=np.random.randint(100, size=DMT)
print(arr)
lis1=[]
lis2=[]
string=''
x=0
#factorial for of all probability
n = DMT
factorial = 1
for i in range (1,n+1):
   factorial = factorial * i
print("Factorail  is : ",factorial)


while x < factorial :
    np.random.shuffle(arr)
    #convert interger to str
    for i in range(DMT):
        convertnum=str(arr[i])
        string = string+convertnum    
    lis1.append(string)
    #eliminates the number that duplicate
    if [i for n, i in enumerate(lis1) if i not in lis1[:n]] :
        lis1sort = [i for n, i in enumerate(lis1) if i not in lis1[:n]]
    string=''
    x=len(lis1sort)
print(x)
print(lis1sort)
#convert str to integer to find max number
for i in range(factorial):
    convertston=int(lis1sort[i])
    lis2.append(convertston)
print("the largest number is",max(lis2))