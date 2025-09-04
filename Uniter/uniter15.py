# mensagem de boas-vindas com menu de modelos
print("Bem vindo a Fábrica de Camisetas do Mateus Viçozi Leite\n")
print("Entre com o modelo desejado")
print("MCS - Manga Curta Simples")
print("MLS - Manga Longa Simples")
print("MCE - Manga Curta Com Estampa")
print("MLE - Manga Longa Com Estampa")

def escolha_modelo():
    while True:
        modelo = input(">>")
        if modelo == "MCS":
            return 1.80
        elif modelo == "MLS":
            return 2.10
        elif modelo == "MCE":
            return 2.90
        elif modelo == "MLE":
            return 3.20
        else:
            print("Escolha inválida, entre com o modelo novamente")

def num_camisetas():
    while True:
        try:
            qtd = int(input("Entre com o número de camisetas: "))
            if qtd > 20000:
                print("Não aceitamos tantas camisetas de uma vez.\nPor favor, entre com o número de camisetas novamente.")
                continue
            if qtd < 20:
                return qtd
            elif qtd >= 20 and qtd < 200:
                return qtd * 0.95
            elif qtd >= 200 and qtd < 2000:
                return qtd * 0.93
            else:
                return qtd * 0.88
        except:
            print("Valor inválido. Digite um número inteiro.")

def frete():
    while True:
        print("Escolha o tipo de frete:")
        print("1 - Frete por transportadora - R$ 100.00")
        print("2 - Frete por Sedex - R$ 200.00")
        print("0 - Retirar pedido na fábrica - R$ 0.00")
        opc = input(">>")
        if opc == "1":
            return 100
        elif opc == "2":
            return 200
        elif opc == "0":
            return 0
        else:
            print("Opção de frete inválida, tente novamente.")

preco_modelo = escolha_modelo()
qtd_final = num_camisetas()
valor_frete = frete()

total = (preco_modelo * qtd_final) + valor_frete
print(f"Total: R$ {total:.2f} (Modelo: {preco_modelo} * Quantidade(com desconto): {qtd_final} + frete: {valor_frete})")
