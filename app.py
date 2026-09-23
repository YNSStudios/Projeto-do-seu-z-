import json
import random
from time import sleep

try:
    with open("devedores.json", "r", encoding="utf-8") as dividas:
        devedores = json.load(dividas)

except FileNotFoundError:
    devedores = []


def verificaçao_numero():

    while True:

        valor = input("\033[33mDigite aqui:\033[0m ")

        try:
            valor = float(valor)
            return valor
        except ValueError:
            print("\033[31mIsso não é um número !\033[0m")


print("========================")
print()
print("[1] Cria divida/devedor")
print()

escolha = verificaçao_numero()
print()

if escolha == 1:

    print("\033[33mCriação de divida/devedor \033[0m")
    print()

    nome = input("Digite o nome do devedor: ").title().strip()
    print()

    print("Digite o valor da divida do devedor. ")
    divida = verificaçao_numero()
    print()

    while True:

        print("Digite o nivel de confiança do cliente. ")
        print()
        print("[1] cliente duvidoso.")
        print()
        print("[2] Cliente novo.")
        print()
        print("[3] Cliente de confiança.")

        status = verificaçao_numero()

        if status == 1:

            credibilidade = "\033[31mCliente duvidoso.\033[0m"
            credito = 100
            break

        elif status == 2:

            credibilidade = "\033[33mCliente novato\033[0m"
            credito = 150
            break

        elif status == 3:

            credibilidade = "\033[32mCliente de confiança\033[0m"
            credito = 250
            break

        else:
            print("\033[31mOpção inválida !\033[0m")

    devedores.append(
        {
            "nome": nome,
            "divida": divida,
            "credibilidade": credibilidade,
            "credito": credito,
        }
    )

    with open("devedores.json", "r", encoding="utf-8") as dividas:
        json.dump(devedores, dividas, ensure_ascii=False, indent=4)
