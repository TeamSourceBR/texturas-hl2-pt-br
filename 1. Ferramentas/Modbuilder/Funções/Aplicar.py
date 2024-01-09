import subprocess
from colorama import init, Fore, Style

def execute_command(command):
    try:
        subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(Fore.GREEN + Style.BRIGHT + "Aplicado com sucesso!")
    except subprocess.CalledProcessError as e:
        print(Fore.GREEN + Style.BRIGHT + "Aplicado com sucesso!", end=" ")
        print(Fore.YELLOW + Style.BRIGHT + "O cache já estava limpo.")

if __name__ == "__main__":
    init(autoreset=True)

    # Caminho completo do arquivo a ser copiado
    caminho_arquivo = "'/home/david/Projetos/HL2 tradução das texturas/2. Compilação/hl2_textures_dir.vpk'"

    # Comando desejado
    comando = f"cp -f {caminho_arquivo} '/home/david/.var/app/com.valvesoftware.Steam/.local/share/Steam/steamapps/common/Half-Life 2/hl2/custom' && rm '/home/david/.var/app/com.valvesoftware.Steam/.local/share/Steam/steamapps/common/Half-Life 2/hl2/custom/hl2_textures.vpk.sound.cache'"

    execute_command(comando)

