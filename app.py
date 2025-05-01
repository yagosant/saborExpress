import os
import util
import menu
 #print(type(opcao_escolhida))


def main():
    os.system('cls')
    util.exibir_nome_programa()
    menu.exibe_opcoes()
    opcao_escolhida = int(input('Escolha uma opção: '))
    menu.selecionar_opcoes(opcao_escolhida)

#falando que é o programa principal
if __name__ == '__main__':
    main()