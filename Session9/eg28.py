Movie = {
    'Name':'Spider-man Homecoming',
    'Spiderman':'Tom Holland',
    'Air date':'28 June 2018',
    'Tony Stark':'Robert Downey Jr'
}
Movie['Others character'] = ['aunt May', 'ect..']
Movie['producter'] = ['Kevin Feige', 'Amy Pascal']
Movie['country'] = ['America']

for key, value in Movie.items():
    print(key,":", value)

Movie['Others character'] = ['Vulture : Michael Myers','Captain America : Chris Evans']

for key, value in Movie.items():
    print(key,":", value)