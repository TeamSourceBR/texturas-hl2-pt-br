import os
import shutil

def procurar_arquivo(nome_arquivo, caminho_pasta):
    resultados = []
    for pasta_atual, _, arquivos in os.walk(caminho_pasta):
        for arquivo in arquivos:
            if nome_arquivo == arquivo:
                resultados.append(os.path.relpath(os.path.join(pasta_atual, arquivo), caminho_pasta))
    return resultados

def listar_arquivos_em_pasta(caminho_pasta):
    caminho_absoluto = os.path.abspath(caminho_pasta)
    return [os.path.join(caminho_absoluto, arquivo) for arquivo in os.listdir(caminho_absoluto) if os.path.isfile(os.path.join(caminho_absoluto, arquivo))]

def formatar_nome_arquivo(nome_arquivo):
    return f"\033[1;34m{nome_arquivo}\033[0m"

def formatar_caminho(resultado):
    return f"{os.path.join(resultado)}"

def formatar_caminho_apartir_compilacao(resultado):
    return f"{os.path.join('Compilação', resultado)}"

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
    caminho_pasta_verificacao = "/home/david/Projetos/HL2 tradução das texturas/5. Traduzidos"  # Substitua pelo caminho desejado
    arquivos_app = listar_arquivos_em_pasta(caminho_pasta_verificacao)

    if arquivos_app:
        for arquivo in arquivos_app:
            nome_arquivo = os.path.basename(arquivo)
            caminho_pasta = os.path.join(os.environ["HOME"], "Projetos", "HL2 tradução das texturas", "3. Original vpk completo")
            resultados = procurar_arquivo(nome_arquivo, caminho_pasta)
            
            if resultados:
                for resultado in resultados:
                    caminho_destino = criar_pastas(os.path.join(os.environ["HOME"], "Projetos", "HL2 tradução das texturas", "2. Compilação", "hl2_textures_dir"), resultado)
                    caminho_relativo = formatar_caminho_apartir_compilacao(resultado)
                    copiar_arquivo(arquivo, caminho_destino)
                    print(f"{formatar_nome_arquivo(nome_arquivo)} {formatar_mensagem_sucesso('Copiado para')} {formatar_caminho(caminho_relativo)}")
            else:
                print(f"{formatar_nome_arquivo(nome_arquivo)} {formatar_mensagem_erro('Não encontrado')}")

if __name__ == "__main__":
    altobuild()

