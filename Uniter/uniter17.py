# mensagem de boas-vindas
print("Bem-vindo a Loja do Mateus Viçozi Leite")

# entrada do valor e quantidade de parcelas
valorDoPedido = float(input("Entre com o valor do pedido: "))
quantidadeParcelas = int(input("Entre com a quantidade de parcelas: "))

# definição do juros
if quantidadeParcelas < 4:
    juros = 0
elif quantidadeParcelas >= 4 and quantidadeParcelas < 6:
    juros = 0.04
elif quantidadeParcelas >= 6 and quantidadeParcelas < 9:
    juros = 0.08
elif quantidadeParcelas >= 9 and quantidadeParcelas < 13:
    juros = 0.16
else:
    juros = 0.32

# cálculo do valor da parcela e total parcelado
valorDaParcela = (valorDoPedido * (1 + juros)) / quantidadeParcelas
valorTotalParcelado = valorDaParcela * quantidadeParcelas

# saída formatada
print(f"O valor das parcelas é de: R$ {valorDaParcela:.2f}")
print(f"O valor Total Parcelado é de: R$ {valorTotalParcelado:.2f}")

