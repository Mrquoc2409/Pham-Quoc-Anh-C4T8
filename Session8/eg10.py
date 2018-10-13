import string
Likes = ["Games", "Sports","Music"]
print(*Likes, sep=" | ")

Likes.append("Movies")

print(Likes[1].upper(),Likes[3].upper(),Likes[2].upper(), sep=" | ")