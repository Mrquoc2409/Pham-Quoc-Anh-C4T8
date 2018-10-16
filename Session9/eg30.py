Movie = {
    'Name':'Spider-man Homecoming',
    'Spiderman':'Tom Holland',
    'Air date':'28 June 2018',
    'Tony Stark':'Robert Downey Jr'
}
Movie['Others character'] = ['aunt May', 'ect..']
Movie['producter'] = ['Kevin Feige', 'Amy Pascal']
Movie['country'] = ['America']


Movie['Others character'] = ['Vulture : Michael Myers','Captain America : Chris Evans']

x = Movie['Others character']
x.append('Flash Thompson : Michael Myers')

for key, value in Movie.items():
    print(key,":", value)

x.pop(0)

for key, value in Movie.items():
    print(key,":", value)
