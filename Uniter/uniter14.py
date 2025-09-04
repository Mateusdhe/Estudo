# mensagem de boas-vindas
print("Bem vindo a Empresa do Mateus Viçozi Leite")
lista_funcionarios = []

def cadastrar_funcionario():

    id_num = int(input("Id do Funcionário: "))
    nome = input("Por favor entre com o nome do Funcionário: ")
    setor = input("Por favor entre com o setor do Funcionário: ")
    salario = float(input("Por favor entre com o salário do Funcionário: "))

    funcionario = {"id": id_num, "nome": nome, "setor": setor, "salario": salario}
    lista_funcionarios.append(funcionario.copy())
    print("Funcionário cadastrado com sucesso!\n")

def consultar_funcionarios():
    while True:
        print("---------------- MENU CONSULTAR FUNCIONÁRIO ----------------")
        print("1 - Consultar Todos os Funcionários")
        print("2 - Consultar Funcionário por id")
        print("3 - Consultar Funcionário(s) por setor")
        print("4 - Retornar")
        opc = input(">>")

        if opc == "1":
            for func in lista_funcionarios:
                print("---------------")
                print("id:", func["id"])
                print("nome:", func["nome"])
                print("setor:", func["setor"])
                print("salário:", func["salario"])
        elif opc == "2":
            id_busca = int(input("Digite o id do funcionário: "))
            encontrado = False
            for func in lista_funcionarios:
                if func["id"] == id_busca:
                    print("---------------")
                    print("id:", func["id"])
                    print("nome:", func["nome"])
                    print("setor:", func["setor"])
                    print("salário:", func["salario"])
                    encontrado = True
            if not encontrado:
                print("Id inválido.")
        elif opc == "3":
            setor_busca = input("Digite o setor do(s) funcionário(s): ")
            for func in lista_funcionarios:
                if func["setor"] == setor_busca:
                    print("---------------")
                    print("id:", func["id"])
                    print("nome:", func["nome"])
                    print("setor:", func["setor"])
                    print("salário:", func["salario"])
        elif opc == "4":
            return
        else:
            print("Opção inválida")
def remover_funcionario():
    while True:
        id_remove = int(input("Digite o id do funcionário a ser removido: "))
        removido = False
        for func in lista_funcionarios:
            if func["id"] == id_remove:
                lista_funcionarios.remove(func)
                print("Funcionário removido com sucesso!")
                removido = True
                return
        if not removido:
            print("Id inválido")

while True:
    print("---------------- MENU PRINCIPAL ----------------")
    print("1 - Cadastrar Funcionário")
    print("2 - Consultar Funcionário(s)")
    print("3 - Remover Funcionário")
    print("4 - Encerrar Programa")
    opcao = input(">>")

    if opcao == "1":
        cadastrar_funcionario()
    elif opcao == "2":
        consultar_funcionarios()
    elif opcao == "3":
        remover_funcionario()
    elif opcao == "4":
        break
    else:
        print("Opção inválida\n")
