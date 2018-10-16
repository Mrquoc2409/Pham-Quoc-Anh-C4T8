Questions = {
    '1':'Who is Spiderman ?',
    'Answers' :{
        'A':'Tom Holland',
        'B':'Steve Job',
        'C':'You'
    },
    'Correct answer':'A'
}
print (Questions['1'])
for i in Questions['Answers']:
    print (i,'.', Questions['Answers'][i])
a = input("What's your answer ?").upper()
b = Questions['Correct answer']
if a == b:
    print ('Hurayy')
