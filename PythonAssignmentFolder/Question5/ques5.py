#!/usr/bin/env python
import re
import string
import sys
import json 

#opening the .json file for loading the content
with open('jsonfile.json') as f:
    data=json.load(f)
#printing data type object(dictionary)
print(type(data))
#printing the final value of records->s3->bucket->arn(this will fetch the value
print(data['Records'][0]['s3']['bucket']['arn'])#['s3']['bucket'])#['arn'])
#print(data.keys())
#Records['Records']['s3']['bucket']

"""
for record in data['Records']:
    for sthree in data['s3']:
        print(record[s3['bucket']])

for buck in data[Records[s3['bucket']]]:
    print(buck[bucket])
"""


