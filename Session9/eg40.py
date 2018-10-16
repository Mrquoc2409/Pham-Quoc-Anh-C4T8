points = 0

Questions = {
    '1':'Who is Spiderman ?',
    'Answers' :{
        'A':'Tom Holland',
        'B':'Steve Job',
        'C':'You'
    },
    'Correct answer':'A'
}
print ('1',Questions['1'])
for i in Questions['Answers']:
    print (i,'.', Questions['Answers'][i])
a = input("What's your answer ?").upper()
b = Questions['Correct answer']
if a == b:
    points +=1
    print ('Hurayy')
else:
    print('The answer is A !')

#Question2
question2 = {
    '2':'Who is Iron-man ?',
    'Answers' :{
        'A':'Peter Parker',
        'B':'Tony Stark',
        'C':'Steve Roger'
    },
    'Correct answer':'B'
    
}
Questions.update(question2)
print('2', question2['2'])
for i in question2['Answers']:
    print (i,'.', question2['Answers'][i])
a = input("What's your answer ?").upper()
b = question2['Correct answer']
if a == b:
    points +=1
    print ('Hurayy')
else:
    print('The answer is B !')

#Question3
question3 = {
    '3':'Who is Captain America ?',
    'Answers' :{
        'A':'Peter Parker',
        'B':'Steve Roger',
        'C':'Tony Stark'
        
    },
    'Correct answer':'B'
    
}
Questions.update(question3)
print('3', question3['3'])
for i in question3['Answers']:
    print (i,'.', question3['Answers'][i])
a = input("What's your answer ?").upper()
b = question2['Correct answer']
if a == b:
    points +=1
    print ('Hurayy')
else:
    print('The answer is B !')

print("You have done all the quiz!")
print("You have "+str(points)+" correct answer(s)")