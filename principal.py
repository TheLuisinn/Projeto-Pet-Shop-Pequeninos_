RED = "\033[1;31m"  # Definição de Cores para uso no código
PINK = "\033[1;35m"
GREEN = "\033[1;32m"
RESET = "\033[0m"

def cadastrar_dados():
    try:
        with open('Dados.txt', 'a') as arquivo:  # Abrir o arquivo 'Dados.txt' em modo de apêndice (adicionar dados ao final do arquivo)

            print(PINK)
            print("******* CADASTRO DO CLIENTE *******")
            print(RESET)

            codigo_cliente = int(input("Insira o codigo do cliente: "))
            nome_cliente = input("Insira o nome do cliente: ")
            contato = int(input("Insira o número de telefone do cliente: "))
            endereco = input("Insira o endereço do cliente: ")
            bairro = input("Insira o bairro do cliente: ")
            cep = int(input("Insira o cep do cliente: "))
            ponto_de_referencia = input("Insira um ponto de referencia do cliente: ")

            print(PINK)
            print("******* CADASTRO DO PACIENTE *******")
            print(RESET)

            animal = input("Insira qual animal é o paciente:  ")
            nome_paciente = input("Insira o nome do paciente: ")
            raça = input("Insira a raça do paciente: ")
            cor_da_pelagem = input("Insira a cor da pelagem do paciente: ")
            peso = float(input("Insira o peso do paciente: "))
            data_de_nascimento = int(input("Insira a data de nascimento do paciente: ")
            restrição_alimentar = input("Insira alguma restrição alimentar do paciente: ")
            medicação_continua = input("Insira alguma medicação de uso continua do paciente: ")
            observações = input("Insira alguma observação do paciente: ")

            # Formatar os dados do cliente e paciente em uma única string
            cliente = f"{codigo_cliente},{nome_cliente},{contato},{endereco},{bairro},{cep},{ponto_de_referencia},{animal},{nome_paciente},{raça},{cor_da_pelagem},{peso},{data_de_nascimento},{restrição_alimentar},{medicação_continua},{observações}\n"

            arquivo.write(cliente)  # Escrever os dados formatados no arquivo

            print(GREEN)
            print("Dados do Cliente e do Paciente cadastrados com sucesso!")  # Exibir uma mensagem de sucesso
            print(RESET)

    except ValueError:  # Capturar um erro caso os valores fornecidos pelo usuário não estejam no formato esperado
        print(RED)
        print("O valor inserido é inválido. Não se esqueça de digitar um valor numérico e decimal corretamente.")
        print(RESET)

    except Exception as e:  # Capturar qualquer outro erro que possa ocorrer durante o cadastro dos dados
        print(RED)
        print("Ocorreu um erro ao cadastrar os dados:", str(e))
        print(RESET)

def listar_dados():
    try:
        with open('Dados.txt', 'r') as arquivo:  # Abrir o arquivo 'Dados.txt' em modo de leitura ('r')
            linhas = arquivo.readlines()  # Ler todas as linhas do arquivo e armazená-las em uma lista

            if not linhas:  # Verificar se não há linhas (dados) no arquivo
                print(RED)
                print("Não há nenhum dado cadastrado na Petshop Pequeninos.")
                print(RESET)
            else:
                print(PINK)
                print("DADOS CADASTRADOS NA PETSHOP PEQUENINOS:")  # Exibir um cabeçalho para os dados dos clientes
                print(RESET)

                for linha in linhas:  # Iterar sobre cada linha do arquivo
                    dados = linha.strip().split(',')  # Dividir a linha em partes separadas por vírgula (',') e remover os espaços em branco

                    codigo_cliente = int(dados[0])  # Extrair os valores individuais de cada dado
                    nome_cliente = dados[1]
                    contato = int(dados[2])
                    endereco = dados[3]
                    bairro = dados[4]
                    cep = int(dados[5])
                    ponto_de_referencia = dados[6]
                    animal = dados[7]
                    nome_paciente = dados[8]
                    raça = dados[9]
                    cor_da_pelagem = dados[10]
                    peso = float(dados[11])
                    data_de_nascimento = int(dados[12])
                    restrição_alimentar = dados[13]
                    medicação_continua = dados[14]
                    observações = dados[15]

                    print("--------------------")
                    print("Nome do Cliente: ", nome_cliente)
                    print("Codigo do Cliente:", codigo_cliente)
                    print("Contato:", contato)
                    print("Endereco:", endereco)
                    print("Bairro:", bairro)
                    print("Cep:", cep)
                    print("Ponto de Referencia:", ponto_de_referencia)
                    print("Animal: ", animal)
                    print("Nome do Paciente:", nome_paciente)
                    print("Raça:", raça)
                    print("Cor da Pelagem:", cor_da_pelagem)
                    print("Peso:", peso)
                    print("Data de Nascimento:", data_de_nascimento)
                    print("Restrição Alimentar:", restrição_alimentar)
                    print("Medicação Continua:", medicação_continua)
                    print("Observações:", observações)
                    print("--------------------")

    except FileNotFoundError:  # Capturar o erro caso o arquivo 'Dados.txt' não seja encontrado
        print(RED)
        print("Arquivo de dados não foi encontrado na Petshop Pequeninos.")
        print(RESET)

    except Exception as e:  # Capturar qualquer outro erro que possa ocorrer durante a listagem dos dados
        print(RED)
        print("Ocorreu um erro ao listar os dados:", str(e))
        print(RESET)

def alterar_dados():
    try:
        with open('Dados.txt', 'r') as arquivo:  # Abrir o arquivo 'Dados.txt' em modo de leitura ('r')
            linhas = arquivo.readlines()  # Ler todas as linhas do arquivo e armazená-las em uma lista

        if not linhas:  # Verificar se não há linhas (dados) no arquivo
            print(RED)
            print("Não há nenhum dado cadastrado na Petshop Pequeninos.")
            print(RESET)
            return

        codigo_cliente = int(input("Digite o código do cliente que deseja alterar: "))
        encontrado = False

        with open('Dados.txt', 'w') as arquivo:  # Abrir o arquivo 'Dados.txt' em modo de escrita ('w')

            for linha in linhas:  # Percorrer cada linha do arquivo
                dados = linha.strip().split(',')  # Dividir a linha em partes separadas por vírgula (',') e remover os espaços em branco

                if int(dados[0]) == codigo_cliente:  # Verificar se o código do aluno na linha atual corresponde ao código fornecido pelo usuário

                    print(PINK)
                    print("*******ALTERAÇÃO NO CLIENTE*******")
                    print(RESET)

                    novo_codigo_cliente = int(input("Digite o novo código do cliente: "))
                    novo_nome_tutor = input("Digite o novo nome do Tutor: ")
                    novo_contato = int(input("Adicione o novo número de telefone: "))
                    novo_endereco = input("Insira o novo endereço: ")
                    novo_bairro = input("Insira o novo bairro: ")
                    novo_cep = int(input("Insira o novo Cep: "))
                    novo_ponto_de_referencia = input("Insira um novo Ponto de Referencia: ")

                    print(PINK)
                    print("******ALTERAÇÃO NO PACIENTE******")
                    print(RESET)

                    novo_animal = input("Insira o novo tipo de animal: ")
                    novo_nome_paciente = input("Insira o novo nome do paciente: ")
                    novo_raça = input("Insira a nova raça: ")
                    novo_cor_da_pelagem = input("Insira a nova cor da pelagem: ")
                    novo_peso = float(input("Insira o novo peso: "))
                    novo_data_de_nascimento = input("Insira a nova data de nascimento: ")
                    novo_restrição_alimentar = input("Insira alguma nova restrição alimentar: ")
                    novo_medicação_continua = input("Insira alguma nova medicação de uso continua: ")
                    novo_observações = input("Insira alguma nova observação: ")

                    # Criar uma nova linha com os novos dados do cliente e paciente
                    cliente = f"{novo_codigo_cliente},{novo_nome_tutor},{novo_contato},{novo_endereco},{novo_bairro},{novo_cep},{novo_ponto_de_referencia},{novo_animal},{novo_nome_paciente},{novo_raça},{novo_cor_da_pelagem},{novo_peso},{novo_data_de_nascimento},{novo_restrição_alimentar},{novo_medicação_continua},{novo_observações}\n"

                    arquivo.write(cliente)  # Escrever a nova linha no arquivo
                    encontrado = True
                else:
                    arquivo.write(linha)  # Escrever a linha original no arquivo, caso o código do cliente não corresponda

            if encontrado:
                print(GREEN)
                print("Dados do Cliente e do Paciente alterados com sucesso!")  # Exibir uma mensagem de sucesso
                print(RESET)
            else:
                print(RED)
                print("Cliente não encontrado.")  # Exibir uma mensagem de erro caso o cliente não seja encontrado
                print(RESET)

    except ValueError:  # Capturar um erro caso os valores fornecidos pelo usuário não estejam no formato esperado
        print(RED)
        print("O valor inserido é inválido. Não se esqueça de digitar um valor numérico e decimal corretamente.")
        print(RESET)

    except Exception as e:  # Capturar qualquer outro erro que possa ocorrer durante a alteração dos dados
        print(RED)
        print("Ocorreu um erro ao alterar os dados:", str(e))
        print(RESET)

def excluir_dados():
    try:
        with open('Dados.txt', 'r') as arquivo: # Abrir o arquivo 'Dados.txt' em modo de leitura ('r')
            linhas = arquivo.readlines() # Ler todas as linhas do arquivo e armazená-las em uma lista

        if not linhas: # Verificar se não há linhas (dados) no arquivo
            print(RED)
            print("Não há nenhum dado cadastrado na Petshop Pequeninos.")
            print(RESET)
            return

        codigo_cliente = int(input("Digite o código do cliente que deseja excluir algum dado: ")) # Solicitar ao usuário o código do cliente
        encontrado = False

        for linha in linhas: # Percorrer cada linha do arquivo
            dados = linha.strip().split(',') # Dividir a linha em partes separadas por vírgula (',') e remover os espaços em branco

            if int(dados[0]) == codigo_cliente: # Verificar se o código do cliente na linha atual corresponde ao código fornecido pelo usuário
                encontrado = True # Indicar que o cliente foi encontrado

                # Exibir os dados do cliente
                print(PINK)
                print("Dados do cliente encontrado:")
                print(f"1. Nome do Tutor: {dados[1]}")
                print(f"2. Contato: {dados[2]}")
                print(f"3. Endereço: {dados[3]}")
                print(f"4. Bairro: {dados[4]}")
                print(f"5. CEP: {dados[5]}")
                print(f"6. Ponto de Referência: {dados[6]}")
                print(f"7. Animal: {dados[7]}")
                print(f"8. Nome do Paciente: {dados[8]}")
                print(f"9. Raça: {dados[9]}")
                print(f"10. Cor da Pelagem: {dados[10]}")
                print(f"11. Peso: {dados[11]}")
                print(f"12. Data de Nascimento: {dados[12]}")
                print(f"13. Restrição Alimentar: {dados[13]}")
                print(f"14. Medicação Continua: {dados[14]}")
                print(f"15. Observações: {dados[15]}")
                print(RESET)

                # Solicitar ao usuário qual dado deseja excluir
                dado_escolhido = int(input("Digite o número do dado que deseja excluir (entre 1 e 15): "))

                if 1 <= dado_escolhido <= 15:
                    dados[dado_escolhido] = ""  # Remover o dado específico
                    print(GREEN)
                    print("Dado excluído com sucesso!")
                    print(RESET)
                else:
                    print(RED)
                    print("Número inválido. Nenhum dado foi excluído.")
                    print(RESET)
                
                nova_linha = ','.join(dados) + '\n'
                linha = nova_linha  # Atualiza a linha com o dado excluído
                break

        with open('Dados.txt', 'w') as arquivo: # Abrir o arquivo 'Dados.txt' em modo de escrita ('w')
            for linha_atual in linhas:
                if linha_atual.strip().split(',')[0] != str(codigo_cliente): # Manter todas as linhas que não são do cliente atual
                    arquivo.write(linha_atual)
                else:
                    arquivo.write(linha)  # Escrever a linha atualizada do cliente

        if not encontrado: # Se nenhum cliente foi encontrado com o código fornecido
            print(RED)
            print("Nenhum cliente encontrado com o código fornecido.")
            print(RESET)

    except ValueError: # Capturar o erro se o usuário inserir um valor inválido
        print(RED)
        print("Valor inserido é inválido. Digite um valor numérico para o código do cliente.")
        print(RESET)

    except FileNotFoundError: # Capturar o erro se o arquivo 'Dados.txt' não for encontrado
        print(RED)
        print("Arquivo de dados não encontrado.")
        print(RESET)

    except Exception as e: # Capturar qualquer outro erro que ocorra durante a exclusão dos dados
        print(RED)
        print("Ocorreu um erro ao excluir os dados:", str(e))
        print(RESET)

def realizar_backup():
    try:
        with open('Dados.txt', 'r') as arquivo_origem: # Abrir o arquivo 'Dados.txt' em modo de leitura ('r')
            with open('backup_Dados.txt', 'w') as arquivo_backup: # Abrir o arquivo 'backup_Dados.txt' em modo de escrita ('w')
                conteudo = arquivo_origem.read() # Ler o conteúdo do arquivo de origem
                arquivo_backup.write(conteudo) # Escrever o conteúdo lido no arquivo de backup
    
                print(GREEN)
                print("Backup do arquivo realizado com sucesso!") # Exibir mensagem de sucesso ao realizar o backup
                print(RESET)

    except FileNotFoundError: # Capturar o erro se o arquivo 'Dados.txt' não for encontrado
        print(RED)
        print("Arquivo de dados não encontrado.")
        print(RESET)

    except Exception as e: # Capturar qualquer outro erro que ocorra durante a realização do backup
        print(RED)
        print("Ocorreu um erro ao realizar o backup:", str(e))
        print(RESET)
