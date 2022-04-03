# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 18:15:10 2022

@author: Krister Martinez

Project 2

Hot Dog Cookout Calculator

"""

numPeople = int(input("Enter the number of people that will attend your cookout: "))
numHotdogPerson = int(input("Enter the number of hotdogs that each person will eat: "))
print()

HOTDOG_PACKAGE = 10
BUNS_PACKAGE = 8

totalNumHotdog = numPeople * numHotdogPerson

minNumHotdogPack = totalNumHotdog // HOTDOG_PACKAGE
minNumBunsPack = totalNumHotdog // BUNS_PACKAGE
hotdogLeft = totalNumHotdog % HOTDOG_PACKAGE
bunsLeft = totalNumHotdog % BUNS_PACKAGE

print ("The minimum number of packages of hot dogs required will be: ", minNumHotdogPack)
print ("The minimum number of packages of hot dog buns required will be: ", minNumBunsPack)
print ("The number of hot dogs that will be left over is: ", hotdogLeft)
print ("The number of hot dog buns that will be left over is: ", bunsLeft)



