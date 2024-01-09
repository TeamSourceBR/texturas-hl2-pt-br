import os
import shutil
from colorama import Fore, Style, init

def procurar_arquivo(nome_arquivo, caminho_pasta):
    resultados = []
    for pasta_atual, _, arquivos in os.walk(caminho_pasta):
        for arquivo in arquivos:
            if nome_arquivo == arquivo:
                resultados.append(os.path.relpath(os.path.join(pasta_atual, arquivo), caminho_pasta))
    return resultados

def listar_arquivos(caminho_pasta):
    return [arquivo for arquivo in os.listdir(caminho_pasta) if os.path.isfile(os.path.join(caminho_pasta, arquivo))]

def formatar_nome_arquivo(nome_arquivo):
    return f"{Fore.CYAN}{Style.BRIGHT}{nome_arquivo}{Style.RESET_ALL}"

def formatar_caminho(resultado):
    return f"{Style.BRIGHT}{os.path.join(resultado)}{Style.RESET_ALL}"

def formatar_mensagem_sucesso(mensagem):
    return f"{Fore.GREEN}{Style.BRIGHT}{mensagem}{Style.RESET_ALL}"

def formatar_mensagem_erro(mensagem):
    return f"{Fore.RED}{Style.BRIGHT}{mensagem}{Style.RESET_ALL}"

def criar_pastas(destino, caminho_pesquisa):
    caminho_destino = os.path.join(destino, *caminho_pesquisa.split('/'))
    os.makedirs(os.path.dirname(caminho_destino), exist_ok=True)
    return caminho_destino

def copiar_arquivo(origem, destino):
    shutil.copy2(origem, destino)

def main():
    init(autoreset=True)  # Inicializa colorama para redefinir as configurações de estilo automaticamente

    print(f"{Style.BRIGHT}({Fore.YELLOW}1.{Style.RESET_ALL} {Style.BRIGHT}Pesquisar arquivo {Fore.YELLOW}2.{Style.RESET_ALL} {Style.BRIGHT}Auto busca):{Style.RESET_ALL}", end="")
    opcao = input()

    if opcao == "1":
        nome_arquivo_pesquisa = input(f"Digite o nome do arquivo a ser pesquisado:")
        caminho_pasta = os.path.join(os.environ["HOME"], "Projetos", "HL2 tradução das texturas", "3. Original vpk completo")

        resultados = procurar_arquivo(nome_arquivo_pesquisa, caminho_pasta)

        if resultados:
            for resultado in resultados:
                print(f"{formatar_nome_arquivo(nome_arquivo_pesquisa)} {formatar_mensagem_sucesso('Encontrado em')} {formatar_caminho(resultado)}")
        else:
            print(f"{formatar_nome_arquivo(nome_arquivo_pesquisa)} {formatar_mensagem_erro('Não encontrado')}")

    elif opcao == "2":
        caminho_pasta_app = "/home/david/Projetos/HL2 tradução das texturas/5. Traduzidos"
        arquivos_app = listar_arquivos(caminho_pasta_app)

        if arquivos_app:
            for arquivo in arquivos_app:
                nome_arquivo = os.path.basename(arquivo)
                caminho_pasta = os.path.join(os.environ["HOME"], "Projetos", "HL2 tradução das texturas", "3. Original vpk completo")
                resultados = procurar_arquivo(nome_arquivo, caminho_pasta)
                if resultados:
                    for resultado in resultados:
                        print(f"{formatar_nome_arquivo(nome_arquivo)} {formatar_mensagem_sucesso('Encontrado em')} {formatar_caminho(resultado)}")
                else:
                    print(f"{formatar_nome_arquivo(nome_arquivo)} {formatar_mensagem_erro('Não encontrado')}")

        else:
            print(f"{formatar_mensagem_erro('Nenhum arquivo encontrado no diretório do aplicativo')}")

if __name__ == "__main__":
    main()

