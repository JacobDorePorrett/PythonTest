# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 11:06:08 2021

@author: s2989594
"""

pressures = [0.273, 0.275, 0.277, 0.276]
print ('First item of pressure:', pressures[0])


#For Loops

"I like cats"
"I like dogs"
"I like fish"
"I like Brett"

subjects = ["cats", "dogs", "goldfish", "Brett"]

for i in subjects: 
    print("I really like", i)
    
    
for number in [2, 4, 6, 7, 432]:
    print('The value is', number*2)
    
for i in range(0, 4, 2):
    print("The Value is", i)
    
masses = [2, 4, 6, 12, 231, 6]

for i in masses:
    if i > 3.0 and i <= 10.0:
        print(i, "- This one is large")
    elif i > 10.0:
        print(i, "- Rediculously large")
    else:
        print (i, "- It aint large")
        

def average(values):
    if len(values) == 0:
        print("There are no values. You must provide some values")
        return None
    elif total = sum(values) / len(values):
        print("Average is:", total)
    
    


