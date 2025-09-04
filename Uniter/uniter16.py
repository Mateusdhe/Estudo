# -------------------- Bem-vindo + cardápio --------------------
print("-----  Bem-vindo a Loja de Marmitas do Mateus Viçozi Leite  -----")
print("-------------------------- Cardápio --------------------------")
print("    Tamanho     |  Bife Acebolado (BA)  |  Filé de Frango (FF)")
print("       P        |         R$ 16.00       |        R$ 15.00     ")
print("       M        |         R$ 18.00       |        R$ 17.00     ")
print("       G        |         R$ 22.00       |        R$ 21.00     ")
print("--------------------------------------------------------------")

total = 0  # acumulador

while True:

    sabor = input("Entre com o sabor desejado (BA/FF): ")
    if sabor != "BA" and sabor != "FF":
        print("Sabor inválido. Tente novamente")
        continue

    tam = input("Entre com o tamanho desejado (P/M/G): ")
    if tam != "P" and tam != "M" and tam != "G":
        print("Tamanho inválido. Tente novamente")
        continue

    if sabor == "BA":
        if tam == "P":
            preco = 16
        elif tam == "M":
            preco = 18
        else:
            preco = 22
    else:
        if tam == "P":
            preco = 15
        elif tam == "M":
            preco = 17
        else:
            preco = 21

    total = total + preco

    if sabor == "BA":
        print(f"Você pediu um Bife Acebolado no tamanho {tam}: R$ {preco:.2f}")
    else:
        print(f"Você pediu um Filé de Frango no tamanho {tam}: R$ {preco:.2f}")

    mais = input("Deseja mais alguma coisa? (S/N): ")
    if mais.upper() == "S":
        continue
    else:
        break

# total final
print(f"\nO valor total a ser pago: R$ {total:.2f}")


