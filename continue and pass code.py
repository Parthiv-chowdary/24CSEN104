for i in range(3):
    if i == 1:
        continue
    if i == 2:
        pass
    print(i)
for i in range(5):
    if i == 3:
        continue
    print(i)


OUTPUT:
0
2
0
1
2
4
