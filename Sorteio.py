import random

estudantes = ["Abdus", "", "Abel ", "Agílio", "Alardo ", "Anaysa", "Arshad ", "Benjamim", "Bruna", "Cleide ", "Cléusia", "Edilson", "Edson ", "Elgin ", "Elmer", "Gerson", "Gilson", "Henrique ", "Ian", "Jeremias", "Jone ", "Mário", "Mayra", "Naheem", "Rosa ", "Rui", "Selwin ", "Shelsea ", "Shelton ", "Tarsis"]

estudantes_escolhidos = random.sample(estudantes, 3)

print("Os estudantes escolhidos são:")
for estudante in estudantes_escolhidos:
    print(estudante)