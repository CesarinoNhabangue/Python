frase = input("Digite uma frase: ")
palavra = ""
for i in range(len(frase)):
    if frase[i] == " ":
        print(palavra)
        palavra = ""
    else:
        palavra += frase[i]
print(palavra)

tamanho = len(palavra)

if tamanho % 2 == 0:
    #lmeio = int(tamanho / 2)
   # n
