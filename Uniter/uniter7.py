
#Exercicio:

print('Escolha o que deseja comprar:')
print('1 - Maça')
print('2 - Laranja' )
print('3 - Banana')

produto = int(input('Qual a sua escolha? '))
qtd = int(input('Quantas unidades? '))

if (produto == 1):    # Maça
    pagar = qtd * 2.3
    print(f'Voce comprou {qtd} maças. Total á pagar: {pagar}')
else:
    if (produto == 2):    # Laranja
        pagar = qtd * 3.6
        print(f'Voce comprou {qtd} laranjas. Total á pagar:{pagar}')
    else:
        if (produto == 3):   #Banana
            pagar =qtd * 1.85
            print(f'Voce comprou {qtd} bananas. Total á pagar {pagar}')
        else:
            print('Produto inesxixtente!')            













