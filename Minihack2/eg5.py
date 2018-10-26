import string

print ("If you are done deleting things, type done to exit.")

while True:
    Colors = ['red', 'green', 'blue']
    a = input('Input the thing you want to delete or the number of it.')

    if a in string.digits:
        b = int(a) - 1 
        Colors.pop(b)
        print (Colors)
    if a in Colors:
        Colors.remove(a)
        print(Colors)
    elif a == 'done':
        break