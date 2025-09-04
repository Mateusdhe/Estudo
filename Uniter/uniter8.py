import os

# Caminho da Área de Trabalho
desktop = os.path.join(os.path.expanduser("~"), "Desktop")

# Pasta "clientes" na área de trabalho
pasta_clientes = os.path.join(desktop, "clientes")

# Cria a pasta se não existir
if not os.path.exists(pasta_clientes):
    os.makedirs(pasta_clientes)

# Caminho do arquivo TXT
arquivo = os.path.join(pasta_clientes, "cadastros.txt")

# Loop principal
while True:
    print("\n--- Cadastro de Cliente ---")
    nome = input("Nome: ")
    idade = input("Idade: ")
    email = input("Email: ")

    # Monta o bloco de texto do cliente
    bloco = f"""
==============================
Nome: {nome}
Idade: {idade}
Email: {email}
==============================\n"""

    # Salva no arquivo
    with open(arquivo, mode='a', encoding='utf-8') as f:
        f.write(bloco)

    # Pergunta se deseja continuar
    continuar = input("Deseja cadastrar outro cliente? (s/n): ").lower()
    if continuar != 's':
        print(f"\nCadastro finalizado. Arquivo salvo em:\n{arquivo}")
        break
    