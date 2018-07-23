#!/usr/bin/env python
import re
import string
import sys
sys.stdout = open("output.txt", "w+")
#created an empty dictionary
doc = {}
document_text = open('textfile.txt', 'r')
text_string = document_text.read()

#Trying to match the pattern of strings produced in sentences
matching_pattern = re.findall(r'\b[a-z]{2,15}\b', text_string)
number_pattern_match=re.findall(r'\b[0-9][0-9]*\b', text_string)

#print("printing all numbers at the top of o/p file")
print('\n'.join(map(str, number_pattern_match)))        
#printing all the words retrieved
#increment the count by retrieving the word everytime and if not found default value is set to 0
for word in matching_pattern:
    count = doc.get(word,0)
    doc[word] = count + 1

doc_list = doc.keys()
#this is sorting the document key list
doc_list = sorted(doc, key=lambda x: (x[0]))
#print("Sorted document keys are", doc_list) 

for word in doc_list:
    print (word, doc[word])

