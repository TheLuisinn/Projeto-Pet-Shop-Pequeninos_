from funcoes import *

def cabecalho():
    
    print(RED) # Inserir Cor (Vermelho)
    print("*" * 50)
    print("*****************FACULDADE CESUSC*****************")
    print("Curso: ANÁLISE E DESENVOLVIMENTO DE SISTEMAS")
    print("Disciplina: LÓGICA DE PROGRAMAÇÃO E ALGORÍTMOS")
    print("Prof. Roberto Fabiano Fernandes")
    print("Alunos: Thais Dias da Silva e Luís Bolina Martins")
    print("Turma: ADS:11 / Ano: 2024")
    print("*" * 50)
    print(RESET) # Encerrar Estação da Cor (Vermelho)

def exibir_menu():

    while True:

        print("Seja Bem-Vindo(a) a Petshop Pequeninos, Escolha uma das seguintes opções:")
        print("1 - Cadastrar Dados")
        print("2 - Listar Dados")
        print("3 - Alterar Dados")
        print("4 - Excluir Dados")
        print("5 - Realizar Backup do Arquivo")
        print("0 - Sair")
        opcao = input("Digite a sua opção: ")

        if opcao == "1":
            cadastrar_dados()
        elif opcao == "2":
            listar_dados()
        elif opcao == "3":
            alterar_dados()
        elif opcao == "4":
            excluir_dados()
        elif opcao == "5":
            realizar_backup()
        elif opcao == "0":
            break
        else:
            print(RED)
            print("A opção escolhida é inválida. Digite um número entre 0 e 5.")
            print(RESET)

cabecalho()
exibir_menu()

# Cabeçalho / FEITO
# Exbir Menu / FEITO
# Cadastrar Dados / FEITO
# Listar Dados / FEITO
# Alterar Dados / 
# Excluir Dados / FEITO
# Realizar Backup / FEITO