import os
import util

#dicionario
restaurantes = [{'nome': 'Mc donalts', 'categoria': 'fast-food', 'ativo': False},
                {'nome': 'Novo Sabor', 'categoria': 'fast-food', 'ativo': True}]

'''Essa é função é responsavel por cadastrar um novo restaurante 

    Inputs: 
    -nome
    -categoria
'''
def cadastrar_restaurante():
    os.system('cls')
    util.exibir_subtitulo('Cadastro de novos restaurantes\n')
    nome = input('Digite o nome do restaurante que deseja cadastrar: \n')
    categoria = input('Digite a categoria do restaurante [fastfood, japones, almoço, café]: \n')

    dados_restaurante = {'nome': nome, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_restaurante)
    print(f'O restaurante {nome} foi cadastrado com sucesso!\n')
    util.voltar_ao_menu()


def listar_restaurantes_ativos():
    util.exibir_subtitulo("Lista de restaurantes ativos")
    try:
        for indice, restaurante in enumerate(restaurantes):
            nome = restaurante['nome']
            status = restaurante['ativo']
            if(status == True):
                print(f" {indice} - {nome} ")
    except ZeroDivisionError:
        print("A lista está vazia, não é possível calcular a média.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")   

def listar_restaurantes_inativos():
    util.exibir_subtitulo("Lista de restaurantes inativos")
    try:
        for indice, restaurante in enumerate(restaurantes):
            nome = restaurante['nome']
            status = restaurante['ativo']
            if(status == False):
                print(f" {indice} - {nome} ")
    except ZeroDivisionError:
        print("A lista está vazia, não é possível calcular a média.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")          

def mudar_status_restaurante():
    util.exibir_subtitulo("Editar status restaurantes")
    nome = input('Digite o nome do restaurante a ser alterado o status: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if(nome == restaurante['nome']):
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = print(f'O restaurante {nome} foi ativado com sucesso!\n ' if restaurante['ativo'] 
                             else f'O restaurante {nome} foi desativado com sucesso!\n')
            print(mensagem)
    if not restaurante_encontrado:
        print('Não foi possivel encontrar o restaurante')            