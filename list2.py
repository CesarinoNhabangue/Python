n = int(input("Insira o numero de candidatos"))
votos = [0]*n
v = int(input("insira o numero de votantes"))
for i in range(v):
    voto = input("em que candidato votou?")
    voto[voto-1]=1
