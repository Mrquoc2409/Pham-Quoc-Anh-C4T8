Colors = ['Red', 'Green', 'Blue']

print('Your colors are:')

for i in Colors:
    print(i)

while True:
    a = input('Input new color to your color list')

    if a == 'Done':
        break
    else:
        print('Enter "Done" if you have finished your List')
        Colors.append(a)  
for i in Colors:
    print(i)