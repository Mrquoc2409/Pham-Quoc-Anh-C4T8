movie = {
    'name':'Mr.Bean',
    "description":"about Bean's life",
    'actor':'Rowan Sebastian Atkinson',
    'air date':'January 1, 1990'}

p = input("Rate the movie")
movie.update({'rate':p})

print("name: ", movie['name'])
print("description: ", movie['description'])

