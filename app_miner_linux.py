
import os  # Importa o módulo 'os', que fornece funções para interagir com o sistema operacional.
import subprocess  # Importa 'subprocess', usado para executar comandos do sistema.
import platform  # Importa 'platform', usado para identificar o sistema operacional.

# Configurações do minerador
UNMINEABLE_URL = ""  # URL do pool de mineração para o algoritmo RandomX. Altere conforme a moeda ou pool desejada.
COIN = ""  # Código da moeda que você deseja minerar, neste caso "ATOM". Pode ser alterado para outras moedas, como BTC, DOGE, etc.
WALLET_ADDRESS = ""  # Endereço da carteira onde as recompensas da mineração serão enviadas.
WORKER_NAME = ""  # Nome do worker (identificação usada para gerenciar vários mineradores no pool).
MINER_PATH = "/usr/local/bin/xmrig"  # Caminho absoluto para o executável do minerador (neste caso, xmrig).

# Verificação do sistema operacional
def check_os():
    """
    Função para verificar se o sistema operacional é Linux.
    Se não for, exibe uma mensagem de erro e encerra o programa.
    """
    system = platform.system()  # Obtém o nome do sistema operacional atual (ex: 'Linux', 'Windows', 'Darwin' para macOS).
    if system != "Linux":  # Verifica se o sistema operacional é diferente de Linux.
        print("Este script é projetado para Linux. O sistema atual é:", system)  # Exibe uma mensagem indicando o sistema operacional incompatível.
        exit(1)  # Sai do programa com o código de erro 1.

# Função para iniciar o minerador
def start_miner():
    """
    Função para configurar e iniciar o minerador com os parâmetros definidos.
    """
    # Lista de argumentos para executar o minerador no terminal.
    miner_command = [
        MINER_PATH,  # Caminho para o executável do minerador.
        "-o", UNMINEABLE_URL,  # URL do pool de mineração.
        "-a", "rx",  # Algoritmo de mineração. 'rx' é usado para o algoritmo RandomX.
        "-u", f"{COIN}:{WALLET_ADDRESS}.{WORKER_NAME}",  # Combina a moeda, o endereço da carteira e o nome do worker no formato requerido pelo pool.
        "-p", "x"  # Senha para autenticação no pool. Geralmente é 'x' por padrão.
    ]

    try:
        print("Iniciando o minerador...")  # Exibe uma mensagem indicando que o minerador será iniciado.
        subprocess.run(miner_command)  # Executa o comando do minerador no sistema operacional.
    except FileNotFoundError:  # Captura erros se o executável do minerador não for encontrado.
        print(f"Erro: O minerador não foi encontrado no caminho {MINER_PATH}")  # Exibe uma mensagem de erro indicando que o minerador não existe no caminho especificado.
    except Exception as e:  # Captura outros tipos de erros durante a execução.
        print("Erro ao iniciar o minerador:", str(e))  # Exibe uma mensagem de erro genérica e detalha o problema.

# Função principal
if __name__ == "__main__":  # Verifica se o script está sendo executado diretamente (não importado como módulo).
    check_os()  # Chama a função para verificar o sistema operacional.
    start_miner()  # Inicia o minerador.
