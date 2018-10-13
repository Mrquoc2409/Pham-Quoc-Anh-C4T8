while True:   
    Dict = {
        'hello':'xin chao',
        'dog':'cho',
        'cat':'meo',
        'hat':'mu',
        'pen':'but bi'
    }
    p = input("Word?").lower()

    if p in Dict:
        print(p,"la",Dict[p])
    else:
        print('This word is not in our dictionary')
        break