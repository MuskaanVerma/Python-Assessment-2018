#!/usr/bin/env python
import re
import string
import sys
import array
import os
try:
#simple binary search function  0(log n)
  def binary_search(item_list,valtosearch):
      first = 0
      last = len(item_list)-1
      found = 0
      while( first<=last and not found):
          mid = (first + last)//2
          if item_list[mid] == valtosearch :
              print("found at ",mid)      
              found = 1
              return found
          else:
              if valtosearch < item_list[mid]:
                  last = mid - 1
              else:
                  first = mid + 1
   
                  
#enter all the values      
  numbers=int(input("total of numbers you wish to enter?"))
  print(numbers)
  print("Enter array items: ")
  item_list= [int(x) for x in input().split()]
  valtosearch=int(input("Enter the Value you wish to search for"))
  #print(binary_search(item_list, valtosearch))
  
  x = binary_search(item_list,valtosearch)
  if (x == 1):
      print("Found: ", x)
  else:
      x=x/0
except :
  print("Value you are searching for is not found in the list")
