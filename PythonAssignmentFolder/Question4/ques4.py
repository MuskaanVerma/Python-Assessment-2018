#!/usr/bin/env python
import re
import string
import sys
#Last function is taking the last  element of  each tuple
def last(n): return n[-1]  
#sort_list_last is sorting the  last elements derived from each tuple
def sort_list_last(parentlist):  
  return sorted(parentlist, key=lambda x:x[-1])  

totaltuples=int(input("enter the number of tuples you want"))
#k = 3
#Creating an empty list so as to append the  tuples
parentlist = []
for i in range(0, totaltuples):
    str1 = raw_input()
    parentlist.append(tuple(str1.split()))
    
#original list entered by user is stored in parent list
#print(parentlist)
print("Sorted list is:")
print(sort_list_last(parentlist))

