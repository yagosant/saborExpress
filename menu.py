import app
import util
import restaurante


def exibe_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante ativos')
    print('3. Listar restaurante inativos')
    print('4. Ativar restaurante')
    print('5. Sair\n')

def opcao_invalida():
    print('Opção Inválida!\n')
    util.voltar_ao_menu()  

def selecionar_opcoes(opcao):
    try:  
        if opcao == 1:
            restaurante.cadastrar_restaurante()
        elif opcao == 2:
            restaurante.listar_restaurantes_ativos()
            util.voltar_ao_menu()
        elif opcao == 3:
            restaurante.listar_restaurantes_inativos()
            util.voltar_ao_menu()    
        elif opcao == 4:
            restaurante.mudar_status_restaurante()
            util.voltar_ao_menu()
        elif opcao == 5:
            util.finalizar_app()   
        else:
            opcao_invalida()
    except: 
        opcao_invalida()