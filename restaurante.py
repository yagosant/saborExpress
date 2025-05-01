import os
import util

restaurantes = []

def cadastrar_restaurante():
    os.system('cls')
    print('Cadastro de novos restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: \n')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    util.voltar_ao_menu()

def listar_restaurantes():
    print("Lista de restaurantes")
    for indice, nome in enumerate(restaurantes):
        print(f" {indice} - {nome} ")
        