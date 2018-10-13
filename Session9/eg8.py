a = input("write name")
b = input("write actor")


movie = {
    a:'Mr.Bean',
    "description":"about Bean's life",
    b:'Rowan Sebastian Atkinson',
    'air date':'January 1, 1990'}

p = input("Rate the movie")
movie.update({'rate':p})

print(a, movie['name'])
print("description: ", movie['description'])
print(b, movie['actor'])
print("air date: ", movie['air date'])
print("rate: ", movie['rate'])
