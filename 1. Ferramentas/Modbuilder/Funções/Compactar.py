import shutil
import zipfile
import os

def criar_zip(pasta_origem, pasta_destino, nome_arquivo_zip):
    # Caminho completo do arquivo "hl2_textures_dir.vpk"
    caminho_arquivo_origem = "/home/david/Projetos/HL2 tradução das texturas/2. Compilação/hl2_textures_dir.vpk"
    
    # Caminho completo do arquivo "Leia-me"
    caminho_leia_me = "/home/david/Projetos/HL2 tradução das texturas/2. Compilação/Leia-me.txt"
    
    # Caminho completo do arquivo ZIP
    caminho_zip = os.path.join(pasta_destino, nome_arquivo_zip)
    
    # Cria a estrutura de pastas dentro do ZIP
    estrutura_zip = os.path.join("hl2_texturas_pt_br", "custom")
    
    # Cria a pasta de destino se não existir
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)
    
    # Cria a estrutura de pastas dentro do ZIP
    with zipfile.ZipFile(caminho_zip, 'w') as zipf:
        # Adiciona o arquivo "Leia-me" à pasta "hl2_texturas_pt_br"
        zipf.write(caminho_leia_me, os.path.join("hl2_texturas_pt_br", os.path.basename(caminho_leia_me)))
        
        # Adiciona a estrutura de pastas ao ZIP
        zipf.write(caminho_arquivo_origem, os.path.join(estrutura_zip, os.path.basename(caminho_arquivo_origem)))

    # Mensagem de sucesso em verde e negrito
    print("\033[1;32mCompactação concluída com sucesso!\033[0m")

# Exemplo de uso
pasta_origem = '/home/david/Projetos/HL2 tradução das texturas/2. Compilação/'
pasta_destino = '/home/david/Projetos/HL2 tradução das texturas/2. Compilação/'
nome_arquivo_zip = 'Texturas PT-BR.zip'

criar_zip(pasta_origem, pasta_destino, nome_arquivo_zip)

