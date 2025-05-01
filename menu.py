import app
import util
import restaurante


def exibe_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def opcao_invalida():
    print('Opção Inválida!\n')
    util.voltar_ao_menu()  

def selecionar_opcoes(opcao):
    try:  
        if opcao == 1:
            restaurante.cadastrar_restaurante()
        elif opcao == 2:
            restaurante.listar_restaurantes()
            util.voltar_ao_menu()
        elif opcao == 3:
            print('Ativar restaurantes')
        elif opcao == 4:
            util.finalizar_app()   
        else:
            opcao_invalida()
    except: 
        opcao_invalida()