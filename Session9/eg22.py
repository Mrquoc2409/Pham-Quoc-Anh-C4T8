print('Noted!The currency is dollar')

p1 = {
    'name':'Huy',
    'role':'waiter',
    'how':12,
    'sph':0.8
}

p2 = {
    'name':'Tung',
    'role':'cook',
    'how':24,
    'sph':1.5
}

p3 = {
    'name':'M.Duc',
    'role':'manager',
    'how':20,
    'sph':2
}


Res = [p1,p2,p3]

print(*Res, sep ="|||")

#Additional
p4 = {
    'name':'Don',
    'role':'waiter',
    'how':12,
    'sph':0.9
}

p5 = {
    'name':'H.Duc',
    'role':'waiter',
    'how':14,
    'sph':0.7
}

Res.append(p4)
Res.append(p5)

print('_________________________________________________________________________________________________________')

print(*Res, sep ="|||")


Res[0] = {
    'name':'Huyen',
    'role':'waitress',
    'how':14,
    'sph':1
}

print('_________________________________________________________________________________________________________')
print(*Res, sep = '|||')

Res.pop(4)

print('_________________________________________________________________________________________________________')
for i in Res:
    print(i)
