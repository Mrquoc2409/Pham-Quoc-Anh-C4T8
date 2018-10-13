me = {
    'name':'PQA',
    'age':'18',
    'live in':'Hanoi'
}
p = input("Something")
if p in me:
    print('name:', me['name'])
    print('age:', me['age'])
    print('live in:', me['live in'])
else:
    print("That's not in me")
