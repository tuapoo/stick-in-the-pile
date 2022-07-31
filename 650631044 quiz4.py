# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 13:24:03 2022

@author: tuapoo
"""

import random
import time
coin=random.randint(1,2)


sitp=int(input("how many stick in the pile\n"))
print("There are",sitp,"stick in the pile")
name=input("What is your name :\n")
print("My name is :",name)
print("Let random to find who will go first . . .\n ")
time.sleep(1)
stake=0
Btakestick=0
i=0
n=0
if coin == 1 :
  print("its head,",name,"will go first")
elif coin ==2 :
  print("its tail, bot will go first")
  
while sitp>0 :
    #print(sitp,"remain")
    if coin==1:
      time.sleep(1)
      stake=int(input("{} how many stick you will take : ".format(name)))
      sitp=sitp-stake
      winner="bot, try again later"
      coin=2
    elif coin==2:
      if sitp ==8:
          Btakestick =1
      elif sitp == 9:
          Btakestick =2
      elif sitp == 6:
          Btakestick =2
      elif sitp == 5:
          Btakestick = 1
      elif sitp == 3:
          Btakestick = 2
      elif sitp == 2 :
          Btakestick = 1
      elif sitp == 1:
          Btakestick = 1
      else :
          Btakestick=random.randint(1,2)
      sitp=sitp-Btakestick
      print("bot will take :",Btakestick)
      winner=name,", try again later"
      coin =1
      time.sleep(1)
    if (Btakestick>=3 or stake>=3):
      print("you can not take more than 2 sticks!\n")
      if Btakestick>=3:
         print("please choose stick again!\n")
         sitp=sitp+Btakestick
         coin=2
      elif stake>=3:
         print("please choose stick again!\n")
         sitp=sitp+stake
         coin=1
    elif (stake <= 0) and i==1 :
      print("No you cant take more less than 1 stick")
      sitp=sitp+stake
      coin=1
    elif ((stake or Btakestick)==1 or (stake  or Btakestick)==2) and sitp ==0 :
      print("the winner is :",winner)
    elif ((stake or Btakestick) ==2) and sitp <0 :
      print("You can not take till stick in the pile <0 please choose stick again!\n")
      time.sleep(1)
      if stake==2 and coin==2:
        print("please choose stick again!\n")
        sitp=sitp+stake
        coin=1
      elif Btakestick==2 and coin==1:
        print("please choose stick again!\n")
        sitp=sitp+Btakestick
        coin=2        
    elif ((stake or Btakestick)==1 or (stake  or Btakestick)==2) and sitp >0:
       print("There are ",sitp,"in the pile now\n")
    i=i+1
    
    
