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

        valor = input("\033[33mDigite aqui:\033[0m ").replace(",", ".")
        print()

        try:
            valor = float(valor)
            return valor
        except ValueError:
            print("\033[31mIsso não é um número !\033[0m")


def cadastrar_codigo():

    while True:

        codigo = random.randint(1000, 9999)

        codigo_encontrado = None

        for devedor in devedores:
            if devedor["codigo"] == codigo:
                codigo_encontrado = devedor
                break

        if codigo_encontrado is None:
            return codigo


def consultar_codigo():

    while True:

        print("Digite o codigo do devedor. ")
        codigo = int(verificaçao_numero())
        print()

        codigo_encontrado = None

        for devedor in devedores:
            if devedor["codigo"] == codigo:
                codigo_encontrado = devedor
                break

        if codigo_encontrado is not None:
            return codigo_encontrado
        else:
            print("\033[31mDevedor não encontrado !\033[0m")
            print()

print("========================")
print()
print("[1] Cria divida/devedor.")
print()
print("[2] Remover/quitar divida.")
print()
print("[3] Vizualizar devedores.")
print()
print("[4] calcular divida.")
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
        print()

        status = verificaçao_numero()
        print()

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
            print()

    codigo = cadastrar_codigo

    devedores.append(
        {
            "nome": nome,
            "divida": divida,
            "credibilidade": credibilidade,
            "credito": credito,
            "codigo": codigo,
        }
    )

    with open("devedores.json", "w", encoding="utf-8") as dividas:
        json.dump(devedores, dividas, ensure_ascii=False, indent=5)

    print("\033[32mDevedor cadastrado com sucesso !\033[0m")
    print()

elif escolha == 2:

    print("\033[33mRemoção/Quitação de divida.\033[0m")
    print()

    for devedor in devedores:
        print(f"Nome: {devedor['nome']}")
        print(f"Codigo: {devedor['codigo']}")
        print(f"Divida: {devedor['divida']}")
        print()

    remover_devedor = consultar_codigo()

    devedores.remove(remover_devedor)

    with open("devedores.json", "w", encoding="utf-8") as dividas:
        json.dump(devedores, dividas, ensure_ascii=False, indent=5)

    print("\033[32mDivida removida/quitada com sucesso.\033[0m")
    print()

elif escolha == 3:

    print("\033[33mVisualizar devedores.\033[0m")
    print()

    for devedor in devedores:
        print("==========================")
        print(f"Nome: {devedor['nome']}.")
        print(f"Divida: \033[31mR${devedor['divida']}.\033[0m")
        print(f"Credibilidade: {devedor['credibilidade']}.")
        print()

elif escolha == 4:

    print("\033[33mCalcular divida.\033[0m")
    print()

    for devedor in devedores:
        print("==========================")
        print(f"Nome: {devedor['nome']}.")
        print(f"Divida: \033[31mR${devedor['divida']}.\033[0m")
        print(f"codigo: {devedor['codigo']}.")
        print()

    editar_devedor = consultar_codigo()

    print("O que será feito ? ")
    print()
    print("[1] Subitrair da divida.")
    print()
    print("[2] Soma na divida.")
    print()
    print("[3] Status de credibilidade.")
    print()

    opçao = verificaçao_numero()

    if opçao == 1:

        print("Digite quanto vai ser pago agora. ")
        print()
        abate = verificaçao_numero()
    
        editar_devedor['divida'] = editar_devedor['divida'] - abate

    elif opçao == 2:

        print("Digite quanto vai ser somado. ")
        print()
        soma = verificaçao_numero()

        verificaçao = editar_devedor['divida'] + soma

        if verificaçao > editar_devedor['credibilidade']:
            print("Não é possivel fazer a soma pois o crédito não é o suficiente.")
            print()
        else:
            editar_devedor['divida'] = verificaçao

    elif opçao == 3:

        while True:
        
            print("Digite o novo nivel de confiança do cliente. ")
            print()
            print("[1] cliente duvidoso.")
            print()
            print("[2] Cliente novo.")
            print()
            print("[3] Cliente de confiança.")
            print()
    
            status = verificaçao_numero()
            print()
    
            if status == 1:
    
                editar_devedor["credibilidade"] = "\033[31mCliente duvidoso.\033[0m"
                editar_devedor["credito"] = 100
                break
    
            elif status == 2:
    
                editar_devedor["credibilidade"] = "\033[33mCliente novato\033[0m"
                editar_devedor["credito"] = 150
                break
    
            elif status == 3:
    
                editar_devedor["credibilidade"] = "\033[32mCliente de confiança\033[0m"
                editar_devedor["credito"] = 250
                break
    
            else:
                print("\033[31mOpção inválida !\033[0m")
                print()

    else:
        print("\033[31mOpção inválida !\033[0m")
        print()

    devedores.append(editar_devedor)

    with open("devedores.json", 'w', encoding="utf-8") as dividas:
        json.dump(devedores, dividas, ensure_ascii=False, indent=5)

    print("\033[32mEdição comcluida com sucesso !\033[0m")