List = []

while True:
    a = input ("Fill your favorite list.")

    if a == 'Done':
        break
    else:
        print('Enter "Done" if you have finished your List')
        List.append(a)      

print ('Here is your list!')
print (List)