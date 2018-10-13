Words = ["Hey", "Elephant", "Hoe", "Cat"]

p = input("Input a word.")

Words.append(p)

for i in Words:
    if "e" or "E" in i:
       print(i)
   