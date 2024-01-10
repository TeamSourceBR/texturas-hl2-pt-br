import os
import colorama
from colorama import Fore

def opcao_1():
    os.system("python3 '/home/david/Projetos/Source BR/Projetos/texturas-hl2-pt-br/1. Ferramentas/Modbuilder/Funções/Busca.py'")

def opcao_2():
    os.system("python3 '/home/david/Projetos/Source BR/Projetos/texturas-hl2-pt-br/1. Ferramentas/Modbuilder/Funções/Organizar.py'")

def opcao_3():
    os.system("python3 '/home/david/Projetos/Source BR/Projetos/texturas-hl2-pt-br/1. Ferramentas/Modbuilder/Funções/Compilador.py'")

def opcao_4():
    os.system("python3 '/home/david/Projetos/Source BR/Projetos/texturas-hl2-pt-br/1. Ferramentas/Modbuilder/Funções/Compactar.py'")

def opcao_5():
    os.system("python3 '/home/david/Projetos/Source BR/Projetos/texturas-hl2-pt-br/1. Ferramentas/Modbuilder/Funções/Aplicar.py'")

def opcao_6():
    os.system("python3 '/home/david/Projetos/Source BR/Projetos/texturas-hl2-pt-br/1. Ferramentas/Modbuilder/Funções/Automake.py'")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def execute_option(option_function):
    clear_screen()
    option_function()
    input("\nPressione Enter para continuar...")
    clear_screen()

def print_interface():
    print(f"                           ")
    print(f"                          Modbuilder v.1.0 {colorama.Fore.YELLOW}{colorama.Style.BRIGHT}Half-life 2{colorama.Style.RESET_ALL}      ")
    print("==============================================================================")
    print(f"  {colorama.Fore.YELLOW}{colorama.Style.BRIGHT}1.{colorama.Style.RESET_ALL}{colorama.Style.BRIGHT}Pesquisar {colorama.Fore.YELLOW}{colorama.Style.BRIGHT}2.{colorama.Style.RESET_ALL}{colorama.Style.BRIGHT}Organizar {colorama.Fore.YELLOW}{colorama.Style.BRIGHT}3.{colorama.Style.RESET_ALL}{colorama.Style.BRIGHT}Compilar {colorama.Fore.YELLOW}{colorama.Style.BRIGHT}4.{colorama.Style.RESET_ALL}{colorama.Style.BRIGHT}Compactar {colorama.Fore.YELLOW}{colorama.Style.BRIGHT}5.{colorama.Style.RESET_ALL}{colorama.Style.BRIGHT}Aplicar {colorama.Fore.YELLOW}{colorama.Style.BRIGHT}6.{colorama.Style.RESET_ALL}{colorama.Style.BRIGHT}Automake {colorama.Fore.YELLOW}{colorama.Style.BRIGHT}0.{colorama.Style.RESET_ALL}{colorama.Style.BRIGHT}Sair{colorama.Style.RESET_ALL}")
    print("==============================================================================")

def main():
    while True:
        print_interface()
        escolha = input("Digite o número da opção desejada: ")

        if escolha == '1':
            execute_option(opcao_1)
        elif escolha == '2':
            execute_option(opcao_2)
        elif escolha == '3':
            execute_option(opcao_3)
        elif escolha == '4':
            execute_option(opcao_4)
        elif escolha == '5':
            execute_option(opcao_5)
        elif escolha == '6':
            execute_option(opcao_6)
        elif escolha == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

