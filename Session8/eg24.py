import random

a = input('Give me a word.')
b = list(a)
random.shuffle(b)
print ('Here is your word with all letters mixed up')
for i in b:
    print((i).upper())