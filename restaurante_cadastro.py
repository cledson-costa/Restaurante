import os

restaurantes = [
    {'nome':'Outback', 'categoria': 'Americana', 'ativo':False},
    {'nome':'Mangai','categoria': 'Frutos do Mar','ativo':True}]


def exibir_nome_app ():
    """Aparece o inicio do sistema quando aberto o app"""

    print('Sabor Express:\n')

def menu_app():
    """Descreve as opções para acesso do sistema"""

    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Alternar Estado do Restaurante')
    print('4. Sair')

def exibir_mensagem(texto):
    os.system('cls')
    print(texto)
    print()

def escolher_opcao():
    try:
        opcao_escolher = int(input('Qual a sua escolha?'))

        if opcao_escolher == 1:
            print('Vamos Cadastrar!')
            cadastrar_restaurante()
        elif opcao_escolher == 2:
            print('Vamos Listar!')
            listar_restaurante()
        elif opcao_escolher == 3:
            print('Vamos Ativar!')
            estado_restaurante()
        elif opcao_escolher == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def voltar_menu(menu_escolhido):
    input('\nPressione enter para continuar')
    menu_escolhido()

def cadastrar_restaurante():
    exibir_mensagem('Cadastro de novo restaurante: [Digite "Sair" para voltar ao menu"]')

    nome_restaurante = input('Qual o nome do restaurante que deseja cadastrar: ').strip(" ")

    restaurante_igual = False
    if nome_restaurante != 'Sair':
        for dict_restaurante in restaurantes:
            if nome_restaurante == dict_restaurante['nome']:
                restaurante_igual = True
                print('Restaurante já cadastrado!')
                voltar_menu(cadastrar_restaurante)
                
        if not restaurante_igual:
            categoria = input(f'Qual a categoria do restaurante {nome_restaurante}: ').strip(" ")
            dados_restaurante = {'nome':nome_restaurante,'categoria':categoria,'ativo':False}
            restaurantes.append(dados_restaurante)
            print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!')
            voltar_menu(main)
    else:
        main()

def listar_restaurante():
    exibir_mensagem('Listando os restaurantes:')
    print(f'{'| Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for lista in restaurantes:
        nome = lista['nome']
        categoria = lista['categoria']
        ativo = 'Ativado' if lista['ativo'] else 'Desativado'
        print(f'| {nome.ljust(20)} | {categoria.ljust(20)} | {ativo.ljust(20)}')
    voltar_menu(main)

def estado_restaurante():
    exibir_mensagem('Alterando estado do restaurante:')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')

    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado.')
    voltar_menu(main)
    
def finalizar_app():
    """Chama a função exibir_mensagem para limpar o terminal e mostrar a mensagem finalizando o app"""

    exibir_mensagem('Finalizando o app')

def opcao_invalida():
    """Descreve que a opção do menu inicial não está dentro das opções descritas no menu"""
    
    print ('Opção inválida!')
    voltar_menu(main)

def main():
    os.system('cls')
    exibir_nome_app()
    menu_app()
    escolher_opcao()
  
if __name__  == '__main__':
    main()