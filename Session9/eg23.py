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


Res[0] = {
    'name':'Huyen',
    'role':'waitress',
    'how':14,
    'sph':1
}

print('_______________________________________________________________________')
for i in Res:
    print(i)

print('_______________________________________________________________________')
print("Salary per month for each")

s1 = p1['how'] * p1['sph'] * 30
s2 = p2['how'] * p2['sph'] * 30
s3 = p3['how'] * p3['sph'] * 30
s4 = p4['how'] * p4['sph'] * 30
s5 = p5['how'] * p5['sph'] * 30
print(p1['name'], "'s",'Salary:','$', int(s1))
print(p2['name'], "'s",'Salary:','$', int(s2))
print(p3['name'], "'s",'Salary:','$', int(s3))
print(p4['name'], "'s",'Salary:','$', int(s4))
print(p5['name'], "'s",'Salary:','$', int(s5))