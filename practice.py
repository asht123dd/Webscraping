# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 18:49:21 2021

@author: ASHUTOSH
"""

a='''abc
def
'''
print(a.splitlines())

import array as arr
My_Array=arr.array('i',[1,2,3,4])
My_list=[1,'abc',1.20]
print(My_Array)
print(My_list)

class a:
    pass
obj=a()
obj.name="xyz"
print("Name = ",obj.name)

big_ch='''A big bowl of Cheese
is laid across the Pipe.'''

count=sum(1 for line in big_ch for character in line if character.isupper())
print('count is '+str(count))

count2=len(big_ch.split('\n'))

print('count2 is '+str(count2))

list = ["1", "4", "0", "6", "9"]
list = [int(i) for i in list]
list.sort()
print (list)

A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10)
A7=['b','c','d','e','a']
A2 = sorted([i for i in A7 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}
A6 = [[i,i*i] for i in A1]
print(A0,A1,A2,A3,A4,A5,A6,sep='\n')