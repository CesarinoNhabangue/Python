numero1 = int(input("Insira o primeiro numero: "))
numero2 = int(input("Insira o segundo numero: "))

somadiv1 = 0
somadiv2 = 0

for i in range(1, numero1):
    if numero1 % i == 0:
        somadiv1 += i

for i in range(1, numero2):
    if numero2 % i == 0:
        somadiv2 += i

if somadiv1 == numero2 and somadiv2 == numero1:
    print(f"{numero1} e {numero2} são números amigos.")
else:
    print(f"{numero1} e {numero2} não são números amigos.")