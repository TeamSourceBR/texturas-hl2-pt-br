import os
import shutil

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
    return f"\033[1;34m{nome_arquivo}\033[0m"

def formatar_caminho(resultado):
    return f"{os.path.join(resultado)}"

def formatar_mensagem_sucesso(mensagem):
    return f"\033[1;32m{mensagem}\033[0m"

def formatar_mensagem_erro(mensagem):
    return f"\033[1;31m{mensagem}\033[0m"

def criar_pastas(destino, caminho_pesquisa):
    caminho_destino = os.path.join(destino, *caminho_pesquisa.split('/'))
    os.makedirs(os.path.dirname(caminho_destino), exist_ok=True)
    return caminho_destino

def copiar_arquivo(origem, destino):
    shutil.copy2(origem, destino)

def altobuild():
    caminho_pasta_app = os.path.dirname(os.path.abspath(__file__))
    arquivos_app = listar_arquivos(caminho_pasta_app)

    if arquivos_app:
        for arquivo in arquivos_app:
            nome_arquivo = os.path.basename(arquivo)
            caminho_pasta = os.path.join(os.environ["HOME"], "Projetos", "HL2 tradução das texturas", "Original vpk completo")
            resultados = procurar_arquivo(nome_arquivo, caminho_pasta)
            if resultados:
                for resultado in resultados:
                    caminho_destino = criar_pastas(os.path.join(os.environ["HOME"], "Projetos", "HL2 tradução das texturas", "Compilação", "hl2_textures_dir"), resultado)
                    copiar_arquivo(arquivo, caminho_destino)
                    print(f"{formatar_nome_arquivo(nome_arquivo)} {formatar_mensagem_sucesso('Copiado para')} {formatar_caminho(caminho_destino)}")
            else:
                print(f"{formatar_nome_arquivo(nome_arquivo)} {formatar_mensagem_erro('Não encontrado')}")

    else:
        print(f"{formatar_mensagem_erro('Nenhum arquivo encontrado no diretório do aplicativo')}")

def main():
    opcao = input("Escolha uma opção (1 - Pesquisar, 2 - Auto Busca, 3 - Altobuild): ")

    if opcao == "1":
        nome_arquivo_pesquisa = input("Digite o nome do arquivo a ser pesquisado: ")
        caminho_pasta = os.path.join(os.environ["HOME"], "Projetos", "HL2 tradução das texturas", "Original vpk completo")

        resultados = procurar_arquivo(nome_arquivo_pesquisa, caminho_pasta)

        if resultados:
            for resultado in resultados:
                print(f"{formatar_nome_arquivo(nome_arquivo_pesquisa)} {formatar_mensagem_sucesso('Encontrado em')} {formatar_caminho(resultado)}")
        else:
            print(f"{formatar_nome_arquivo(nome_arquivo_pesquisa)} {formatar_mensagem_erro('Não encontrado em')} {formatar_caminho(caminho_pasta)} ou em suas subpastas")

    elif opcao == "2":
        caminho_pasta_app = os.path.dirname(os.path.abspath(__file__))
        arquivos_app = listar_arquivos(caminho_pasta_app)

        if arquivos_app:
            for arquivo in arquivos_app:
                nome_arquivo = os.path.basename(arquivo)
                caminho_pasta = os.path.join(os.environ["HOME"], "Projetos", "HL2 tradução das texturas", "Original vpk completo")
                resultados = procurar_arquivo(nome_arquivo, caminho_pasta)
                if resultados:
                    for resultado in resultados:
                        print(f"{formatar_nome_arquivo(nome_arquivo)} {formatar_mensagem_sucesso('Encontrado em')} {formatar_caminho(resultado)}")
                else:
                    print(f"{formatar_nome_arquivo(nome_arquivo)} {formatar_mensagem_erro('Não encontrado')}")

        else:
            print(f"{formatar_mensagem_erro('Nenhum arquivo encontrado no diretório do aplicativo')}")

    elif opcao == "3":
        altobuild()

    else:
        print(f"{formatar_mensagem_erro('Opção inválida. Escolha 1 para Pesquisar, 2 para Auto Busca ou 3 para Altobuild')}")

if __name__ == "__main__":
    main()

