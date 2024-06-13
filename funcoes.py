RED = "\033[1;31m"
GREEN = "\033[1;32m"
RESET = "\033[0m"


def cadastrar_dados():
    try:
        with open('Dados.txt', 'a') as arquivo: # Abrir o arquivo 'Dados.txt' em modo de apêndice (adicionar dados ao final do arquivo)

            print("**CADASTRO DO TUTOR**")
            codigo_cliente =int(input("Digite o codigo: "))
            Nome_Tutor = input("Digite o nome do Tutor: ")
            Contato = int(input("Adicione o número de telefone: "))
            Endereco = input("Insira o endereço: ")
            Bairro = input("Insira o bairro: ")
            Cep = int(input("Insira o Cep: "))
            Ponto_de_Referencia = input("Insira o Ponto de Referencia: ")
            print("***CADASTRO DO PACIENTE***")
            Nome_Paciente = input("Insira o nome do paciente: ")
            Raça = input("Insira a raça: ")
            Cor_da_pelagem = input("Insira a Cor da pelagem: ")
            Peso = int(input("Insira a peso : "))
            Data_de_Nascimento= int(input("Insira o Cep: "))
            Restrição_Alimentar = input("Insira alguma restrição alimentar: ")
            Medicação_continua= input("Insira alguma medica de uso continua: ")
            Observações = input("Insira alguma observação: ")

            cliente = f"{codigo_cliente},{Nome_Tutor},{Contato},{Endereco},{Bairro},{Cep},{Ponto_de_Referencia},{Nome_Paciente},{Raça},{Cor_da_pelagem},{Peso},{Data_de_Nascimento},{Restrição_Alimentar},{Medicação_continua},{Observações}\n" # Formatar os dados do cliente em uma string

            arquivo.write(cliente) 

            print(GREEN)
            print("Dados do aluno cadastrados com sucesso!") # Exibir uma mensagem de sucesso
            print(RESET)

    except ValueError: # Capturar um erro caso os valores fornecidos pelo usuário não estejam no formato esperado
        print(RED)
        print("Valor inválido. Certifique-se de digitar um valor numérico para o código do aluno e a idade, e um valor decimal para as notas.")
        print(RESET)

    except Exception as e: # Capturar qualquer outro erro que possa ocorrer durante o cadastro dos dados
        print(RED)
        print("Ocorreu um erro ao cadastrar os dados:", str(e))
        print(RESET)

def listar_dados():
    try:
        with open('Dados.txt', 'r') as arquivo: # Abrir o arquivo 'Dados.txt' em modo de leitura ('r')
            linhas = arquivo.readlines() # Ler todas as linhas do arquivo e armazená-las em uma lista

            if not linhas: # Verificar se não há linhas (dados) no arquivo
                print(RED)
                print("Não há nenhum dado cadastrado na Petshop Pequeninos.")
                print(RESET)
            else:
                print("Dados cadastrados na Petshop Pequeninos:") # Exibir um cabeçalho para os dados dos alunos
                for linha in linhas: # Iterar sobre cada linha do arquivo
                    dados = linha.strip().split(',') # Dividir a linha em partes separadas por vírgula (',') e remover os espaços em branco
                    
                    codigo_cliente = int(dados[0]) # Extrair os valores individuais de cada dado
                    Nome_Tutor = dados[1]
                    Contato = int(dados[2])
                    Endereco = dados[3]
                    Bairro = dados[4]
                    Cep = int(dados[5])
                    Ponto_de_Referencia = dados[6]
                    Nome_Paciente = dados[7]
                    Raça = dados[8]
                    Cor_da_pelagem = dados[9]
                    Peso = int(dados[10])
                    Data_de_Nascimento= int(dados[11])
                    Restrição_Alimentar = dados[12]
                    Medicação_continua= dados[13]
                    Observações = dados[14]

                    print("Codigo do Cliente:", codigo_cliente)
                    print("Contato:", Contato)
                    print("Endereco:", Endereco)
                    print("Bairro:", Bairro)
                    print("Cep:", Cep)
                    print("Ponto de Referencia:", Ponto_de_Referencia)
                    print("Nome do Paciente:", Nome_Paciente)
                    print("Raça:", Raça)
                    print("Cor da Pelagem:", Cor_da_pelagem)
                    print("Peso:", Peso)
                    print("Data de Nascimento:", Data_de_Nascimento)
                    print("Restrição Alimentar:", Restrição_Alimentar)
                    print("Medicação Continua:", Medicação_continua)
                    print("Observações:", Observações)
                    print("--------------------")


    except FileNotFoundError: # Capturar o erro caso o arquivo 'Dados.txt' não seja encontrado
        print(RED)
        print("Arquivo de dados não encontrado.")
        print(RESET)        
                
    except Exception as e:  # Capturar qualquer outro erro que possa ocorrer durante a listagem dos dados
        print(RED)
        print("Ocorreu um erro ao listar os dados:", str(e))
        print(RESET) 

def alterar_dados():
    try:
        # Abrir o arquivo 'Dados.txt' em modo de leitura ('r')
        with open('Dados.txt', 'r') as arquivo:
            # Ler todas as linhas do arquivo e armazená-las em uma lista
            linhas = arquivo.readlines()

        # Verificar se não há linhas (dados) no arquivo
        if not linhas:
            print(RED)
            print("Não há nenhum dado cadastrado na Petshop Pequeninos.")
            print(RESET)
            return

        # Solicitar ao usuário o código do aluno que deseja alterar
        codigo_cliente = int(input("Digite o código do cliente que deseja alterar: "))
        encontrado = False

        # Abrir o arquivo 'Dados.txt' em modo de escrita ('w')
        with open('Dados.txt', 'w') as arquivo:
            
            # Percorrer cada linha do arquivo
            for linha in linhas:
                
                # Dividir a linha em partes separadas por vírgula (',') e remover os espaços em branco
                dados = linha.strip().split(',')
                
                # Verificar se o código do aluno na linha atual corresponde ao código fornecido pelo usuário
                if int(dados[0]) == codigo_cliente:
                    
                    # Solicitar ao usuário os novos dados para o aluno

                    Novo_codigo_cliente =int(input("Digite o codigo: "))
                    Novo_Nome_Tutor = input("Digite o nome do Tutor: ")
                    Novo_Contato = int(input("Adicione o número de telefone: "))
                    Novo_Endereco = input("Insira o endereço: ")
                    Novo_Bairro = input("Insira o bairro: ")
                    Novo_Cep = int(input("Insira o Cep: "))
                    Novo_Ponto_de_Referencia = input("Insira o Ponto de Referencia: ")
                    print("***CADASTRO DO PACIENTE***")
                    Novo_Nome_Paciente = input("Insira o nome do paciente: ")
                    Novo_Raça = input("Insira a raça: ")
                    Novo_Cor_da_pelagem = input("Insira a Cor da pelagem: ")
                    Novo_Peso = int(input("Insira a peso : "))
                    Novo_Data_de_Nascimento= int(input("Insira o Cep: "))
                    Novo_Restrição_Alimentar = input("Insira alguma restrição alimentar: ")
                    Novo_Medicação_continua= input("Insira alguma medica de uso continua: ")
                    Novo_Observações = input("Insira alguma observação: ")

                    # Criar uma nova linha com os novos dados do aluno
                    cliente = f"{Novo_codigo_cliente},{Novo_Nome_Tutor},{Novo_Contato},{Novo_Endereco},{Novo_Bairro},{Novo_Cep},{Novo_Ponto_de_Referencia},{Novo_Nome_Paciente},{Novo_Raça},{Novo_Cor_da_pelagem},{Novo_Peso},{Novo_Data_de_Nascimento},{Novo_Restrição_Alimentar},{Novo_Medicação_continua},{Novo_Observações}\n" # Formatar os dados do cl

                    print(GREEN)
                    print("Dados do aluno alterados com sucesso!")
                    print(RESET)
                    encontrado = True
                
                # Escrever a linha no arquivo
                arquivo.write(linha)
        
        # Verificar se nenhum aluno foi encontrado com o código fornecido
        if not encontrado:
            print(RED)
            print("Nenhum aluno encontrado com o código fornecido.")
            print(RESET)

    except ValueError:
        # Capturar o erro caso algum valor inválido seja inserido pelo usuário
        print(RED)
        print("Valor inválido. Certifique-se de digitar um valor numérico para o código do aluno e a idade, e um valor decimal para as notas.")
        print(RESET)

    except FileNotFoundError:
        # Capturar o erro caso o arquivo 'Dados.txt' não seja encontrado
        print(RED)
        print("Arquivo de dados não encontrado.")
        print(RESET)

    except Exception as e:
        # Capturar qualquer outro erro que possa ocorrer durante a alteração dos dados
        print(RED)
        print("Ocorreu um erro ao alterar os dados:", str(e))
        print(RESET)

def excluir_dados():
    try:
        with open('Dados.txt', 'r') as arquivo:
            linhas = arquivo.readlines()

        if not linhas:
            print(RED)
            print("Não há nenhum dado cadastrado na Petshop Pequeninos.")
            print(RESET)
            return

        codigo_cliente = int(input("Digite o código do cliente que deseja excluir: "))
        encontrado = False

        with open('Dados.txt', 'w') as arquivo:
            for linha in linhas:
                dados = linha.strip().split(',')
                if int(dados[0]) == codigo_cliente:
                    encontrado = True
                    print(GREEN)
                    print("Dados do cliente excluídos com sucesso!")
                    print(RESET)
                else:
                    arquivo.write(linha)

        if not encontrado:
            print(RED)
            print("Nenhum cliente encontrado com o código fornecido.")
            print(RESET)

    except ValueError:
        print(RED)
        print("Valor inserido é inválido. Digite um valor numérico para o código do cliente.")
        print(RESET)

    except FileNotFoundError:
        print(RED)
        print("Arquivo de dados não encontrado.")
        print(RESET)

    except Exception as e:
        print(RED)
        print("Ocorreu um erro ao excluir os dados:", str(e))
        print(RESET)

def realizar_backup():
    try:
        with open('Dados.txt', 'r') as arquivo_origem:
            with open('backup_Dados.txt', 'w') as arquivo_backup:
                conteudo = arquivo_origem.read()
                arquivo_backup.write(conteudo)
                print(GREEN)
                print("Backup do arquivo realizado com sucesso!")
                print(RESET)

    except FileNotFoundError:
        print(RED)
        print("Arquivo de dados não encontrado.")
        print(RESET)

    except Exception as e:
        print(RED)
        print("Ocorreu um erro ao realizar o backup:", str(e))
        print(RESET)