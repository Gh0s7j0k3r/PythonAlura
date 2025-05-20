import os

restaurantes = ['Pizza', 'Sushi']

def exibir_nome():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")
    
def exibir_opcoes():
    print('Escolha uma opção:')
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizando app...')

def voltar_menu():
    input('\nDigite uma tecla para voltar ao menu principal... ')
    main()

def opcao_invalida():
    print('Opção inválida! Tente novamente.\n')
    voltar_menu()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastros de novos restaurante') #comando valido apenas para Windows
    
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!\n')
    voltar_menu()

def listar_restaurante():
    exibir_subtitulo('Listando restaurantes... ')
    for restaurante in restaurantes:
        print(f'.{restaurantes}')
    voltar_menu()

def escolher_opcoes():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurante()
        elif opcao_escolhida == 3:
            print('Ativar restaurante')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

# Mesma lógica, mas utilizando o match-case (Python 3.10+)
'''def escolher_opcoes():
    opcao_escolhida = int(input('Escolha uma opção: '))
    
    match opcao_escolhida:
        case 1:
            print('Adicionar restaurante')
        case 2:
            print('Listar restaurantes')
        case 3:
            print('Ativar restaurante')
        case 4:
            print('Finalizar app')
        case _:
            print('Opção inválida!')'''

def main():
    os.system('cls') #comando valido apenas para Windows
    exibir_nome()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()
    a