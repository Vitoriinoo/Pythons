import os

restaurantes = [{'nome':'Praça', 'categoria':'Japonsa', 'ativo':False},
                {'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Italiana', 'ativo':False}]

def exibir_nome_do_programa():  
    '''Essa função é responsável por exibir o nome do programa estilizado na tela'''
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      """) 
    
def exibir_opcoes():  
    '''Essa função é responsável por exibir as opções do programa,     
    print('1. Cadastrar restaurante ')
    print('2. Listar restaurante ')
    print('3. Alternar estado do restaurante ')
    print('4. Sair\n')''' 
    print('1. Cadastrar restaurante ')
    print('2. Listar restaurante ')
    print('3. Alternar estado do restaurante ')
    print('4. Sair\n')

def finalizar_app():
    '''Exibe mnensaem de finalização do app'''
    exibir_subtitulo('Finalizar app')

def voltar_ao_menu_principal():
    '''Essa função é responsável por voltar ao menu principal, solicita um tecla para que o usuário volte ao menu principal
    Inputs:
    - Digite uma tecla para voltar ao menu principal
    
    
    Outputs:
    - Retorna ao menu rpincipla
    '''
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def opcao_invalida():
    '''Essa função é responsável por exibir uma mensagem de opção inválida'''
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    '''Essa função é responsável por exibir um subtítulo'''
    os.system('cls')
    linha = '*'  * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    ''' Essa função é responsável por cadastar um novo restaurante
    
    Inputs:
    - Nome_do_restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes

'''
    exibir_subtitulo('Cadastro de novos restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: \n')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: \n')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Essa função é responsável por listar os restaurentes já cadastrados'''
    exibir_subtitulo('Listando restaurantes')

    print(f'{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(22)} | {"Status"}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo ='ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alternar_estado_do_restaurante():
    '''essa função é responsável por alternar o estado do restaurante (ativo/desativo)'''
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)

    if not restaurante_encontrado:
        print(f'O restaurante não foi encontrado')  
    
    voltar_ao_menu_principal()

def escolher_opcao():
    '''Essa função é responsável por escolher a opção do menu'''
    try:
        opcao_escolhida = int(input('Escolha um opção: '))
        #opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()  
        elif opcao_escolhida == 2:
            listar_restaurantes() 
        elif opcao_escolhida == 3:
            alternar_estado_do_restaurante() 
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida() 
def main():
    '''Essa função é responsável por executar o programa'''
    os.system
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
    

