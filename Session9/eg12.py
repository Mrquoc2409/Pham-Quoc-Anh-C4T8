movie = {
    'name':'Mr.Bean',
    "description":"about Bean's life",
    'actor':'Rowan Sebastian Atkinson',
    'air date':'January 1, 1990'}


movie.update({'rate':'9/10'})

print("name: ", movie['name'])
print("description: ", movie['description'])
print("actor: ", movie['actor'])
print("air date: ", movie['air date'])
print("rate: ", movie['rate'])

movie['rate']= "8/10"
 
print("name: ", movie['name'])
print("description: ", movie['description'])
print("actor: ", movie['actor'])
print("air date: ", movie['air date'])
print("rate: ", movie['rate'])

p = input('Input new description:')
movie['description'] = p

print("name: ", movie['name'])
print("description: ", movie['description'])
print("actor: ", movie['actor'])
print("air date: ", movie['air date'])
print("rate: ", movie['rate'])

p = input('Delete?')
if p in movie:
    del movie[p]
else:
    print("Not exists!")

print (movie)
