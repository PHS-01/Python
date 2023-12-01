#Variáveis do sistema
opcao = 'default'
dados = [[],[]] # Funcionários(0) é Usuarios(1)

# Funções
# Função de cadastro tanto de usuario e funcionario
def cadastro(nome, cpf, email, tipo, codigo = ''):
    mensagem = 'default'
    dado = 'default'
    
    if tipo == 'Funcionário':
        dado = (nome,cpf,email,codigo)
        dados[0].append(dado)
        mensagem = '\n Funcionário foi cadastrado com êxito!! \n'
        
    else:
        dado = (nome,cpf,email)
        dados[1].append(dado)
        mensagem = '\n Usuario foi cadastrado com êxito!! \n'
        
    return print(mensagem)

# Desenvolvimento
def login(nome, cpf, email, tipo, codigo = ''):
    if tipo == 'Funcionário':
        for i in range(len(dados[0])):
            if codigo == dados[0][i][3]:
                print('Seja bem vindo '+dados[0][i][3])
            else:
                print('Esse Funcionário não existe no sistema!')
    else:
        for i in range(len(dados[1])):
            
# Função para a ação de cadastro de usuario e funcionario
def acao_cadastro(tipo_acao):
    nome = input(' Digite o seu nome: ')
    cpf = str(int(input(' Digite o seu CPF: ')))
    email = str(input(' Digite o seu E-Mail: '))

    if tipo_acao == 'Funcionário':
        codigo = str(input(' Digite o seu Codigo: '))
        cadastro(nome, cpf, email, codigo,tipo=tipo_acao)
    else:
        cadastro(nome, cpf, email, tipo=tipo_acao)

#While para a repetição do codigo(Tela visual do sistema)
while opcao != '3':
    #Texto inicial
    print('\n Seja bem-vindo ao nosso sistema. \n Você deseja entrar como funcionário ou cliente?')
    print('\n 1-FUNCIONÁRIO \n 2-CLIENTE \n 3-SAIR')
    
    opcao = input('\n Qual a opção deseja? ')
    
    #print ("\n" * 130)
    
    match opcao:
        case '1':
            
        case '2':
            #Atendimento ao Cliente/Cardápio
            print('\n Bem-vindo(a) à nossa padaria!')
            print('\n Antes de realizar as compras, vamos fazer o cadastro para facilitar nas próximas compras!:) \n')

            acao_cadastro('Usuario')
            
        case '3':
            print('\n Saindo do sistema \n')
        case _:
            print('\n Essa opção não existe!!')



            
        
