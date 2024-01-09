import os
import subprocess
from colorama import init, Fore, Style

def execute_command(directory, option):
    os.chdir(directory)

    if option == 1:
        command = "vpk file --create-version 1 -c hl2_textures_dir && mv file hl2_textures_dir.vpk"
    elif option == 2:
        command = "vpk file --create-version 2 -c hl2_textures_dir && mv file hl2_textures_dir.vpk"
    else:
        print("Opção inválida.")
        return

    try:
        subprocess.run(command, shell=True, check=True)
        print(Fore.GREEN + Style.BRIGHT + "Compilação concluída com sucesso!")
    except subprocess.CalledProcessError as e:
        print(Fore.RED + Style.BRIGHT + f"Erro ao executar compilação: {e}")
    finally:
        os.chdir(os.path.expanduser("~"))

if __name__ == "__main__":
    init(autoreset=True)

    # Substitua o caminho do diretório desejado
    diretorio = "/home/david/Projetos/HL2 tradução das texturas/2. Compilação"

    print(f"{Style.BRIGHT}({Fore.YELLOW}1.{Style.RESET_ALL} {Style.BRIGHT}VPK v1 {Fore.YELLOW}2.{Style.RESET_ALL} {Style.BRIGHT}VPK v2):{Style.RESET_ALL}", end="")

    opcao = int(input(""))

    execute_command(diretorio, opcao)


