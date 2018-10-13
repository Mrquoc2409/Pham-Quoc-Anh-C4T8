Dict = {
    'hello':'xin chao',
    'dog':'cho',
    'cat':'meo',
    'hat':'mu',
    'pen':'but bi'
}
p = input("Word?")
if p == "hello":
    print('hello:',Dict['hello'])
elif p == 'dog':
    print('dog:',Dict['dog'])   
elif p == 'cat':
    print('cat:',Dict['cat'])   
elif p == 'hat':
    print('hat:',Dict['hat'])   
elif p == 'pen':
    print('pen:',Dict['pen'])   
else:
    print("This word is not in our dictionary.")