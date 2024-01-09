import subprocess
import os

# Obtém o diretório do script principal
script_directory = os.path.dirname(os.path.abspath(__file__))

# Lista de nomes dos scripts a serem executados
script_names = ['Organizar.py', 'Compilador.py', 'Compactar.py', 'Aplicar.py']

# Itera sobre cada script e executa a função desejada
for script_name in script_names:
    script_path = os.path.join(script_directory, script_name)
    
    # Exemplo: Executa o script e passa 'funcao_principal' como argumento
    subprocess.run(['python', script_path, 'funcao_principal'])

