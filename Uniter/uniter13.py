A = int(input("Lado 1º do triângulo "))
B = int(input("Lado 2º do triângulo "))
C = int(input("Lado 3º do triângulo "))

if ((A > 0 and B > 0 and C > 0) and (A + B > C and A + C > B and B + C > A)):
    #Se chegou até aqui, é porque o triângulo e valido!
    if  (A != B and A != C and B != C):
        print('Triângulo escaçeno!')
    else:
        if (A == B and B == C):
            print('Triângulo equilatero!')
        else:
            print('Tria^ngulo isosceles!')

else:
    print('Ao menos um dos valores indicados não servem para formar um triângulo.')