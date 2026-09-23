import json
import random
from time import sleep

try:
    with open("devedores.json", 'r', encoding="utf-8") as dividas:
        devedores = json.load(dividas)
except FileNotFoundError:
    devedores = []

def verificaçao_numero():

    while True:

        valor = input("Digite aqui: ")

        try:
            valor = float(valor)
            return valor
        except ValueError:
            print("\033[31mIsso não é um número !\033[0m")

print("========================")
print()
print("[1] Cria divida/devedor")
print()

