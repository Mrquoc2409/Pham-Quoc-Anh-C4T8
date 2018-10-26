import random
points = 0

print("NOTE!After each answer you got  right press any button to continue!")
print("PS:And please don't press the power button")
while True:
    Word_list = ['champion', 'superstar', 'dragon', 'rhinoceros', 'geographical', 'antibiotic']
    Word_list.append('dog')
    Word_list.append('god')

    a = random.choice(Word_list)
    b = list(a)
    random.shuffle(b)
    print('Here is your word!-Try to figure it out as fast as you can')

    print( *b ,sep = '|' )

    answer = input("What's the word?")
    if answer == a:
        points +=1
        print('Wow! You are good or maybe just lucky! LOL')
    else:
        print('Nope!Learn some more word, maybe you will get it next time')
        print('That word is:')
        print(a)
        print('You got' ,str(points) ,'right')
        print('Type "again" to play more,"end" to stop.')
    n = input("")
    if n == 'end':
        points = 0
        break
end = input('Press Enter to exit.')





