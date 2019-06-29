"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


tel=[]
for t in range(0,len(calls)):
    for i in range(0,2):
        if(tel.count(calls[t][i])==0):
            tel.append(calls[t][i])
print(len(tel))

for t in range(0,len(texts)):
    for i in range(0,2):
        if(tel.count(texts[t][i])==0):
            tel.append(texts[t][i])

print(len(tel))

"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""
