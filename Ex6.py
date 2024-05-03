tuplo = (2, 4, 23, 1, 76, 3, 36)

maior = tuplo[0]

for i in range(1,len(tuplo)):
    if maior < tuplo[i]:
        maior = tuplo[i]
print(maior)