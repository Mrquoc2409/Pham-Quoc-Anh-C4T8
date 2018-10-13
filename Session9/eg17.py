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