#!/usr/bin/env python
import re
import string
import sys
import logging
#Used to load configuration from file and level is set to INFO(which will act like Print statement
#likewise we can also debug, create a warning, display errors
logging.basicConfig(filename='test1.log',level=logging.INFO)

#validate function is validating the string  by checking the  conditions
def validate(str):
    countAZ=countnumber=countaz=checkcharacter=0
    
    for i in range(len(str)):
        if(str[i] == "@" or str[i] == "$" or str[i] == "#" ):
            checkcharacter=1
        elif(str[i] >= 'a' and str[i] <= 'z'):
            countaz=1
        elif(str[i] >= 'A' and str[i] <= 'Z'):
            countAZ=1
        elif(str[i] >= '0' and str[i] <= '9'):
            countnumber=1
     
    if(checkcharacter == 1 and countnumber == 1 and countAZ == 1 and countaz == 1):
        logging.info("It is a Valid Password")
    else:
        logging.info("Its an InValid Pasword")
    
#main program takes input and calls the Validate Function
def main():
    str= raw_input("Enter the Password ")
    print(str)
    length=len(str)
    if (length < 6 or length > 12):
        logging.info("Its an Invalid Password, as the length either <6 or more than 12")
    else:
        validate(str)
    
if __name__ == "__main__":
 main()


