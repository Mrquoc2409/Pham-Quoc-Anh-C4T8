Movie = {
    'Name':'Spider-man Homecoming',
    'Spiderman':'Tom Holland',
    'Air date':'28 June 2018',
    
}
Movie['Others character'] = ['aunt May', 'ect..']
Movie['producter'] = ['Kevin Feige', 'Amy Pascal']
Movie['country'] = ['America']


Movie['Others character'] = ['Vulture : Michael Myers','Captain America : Chris Evans']

for key, value in Movie.items():
    print(key,":", value)

x = Movie['Others character']
x.append('Flash Thompson : Michael Myers')

for key, value in Movie.items():
    print(key,":", value)
print('_______________________________________________________________________')

for i in x:
    print(i)
