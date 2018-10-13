Letters = ["a", "b", "c", "d"]


p = input("Input a letter.")


Letters.append(p)


j = len(Letters)
for i in range(j):
    print(i + 1,'.',*Letters[i].upper())