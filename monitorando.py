# pip install selenium webdriver-manager # instalar a biblioteca

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
from dotenv import load_dotenv

# Carregar variáveis do arquivo .env
load_dotenv()

# Acessar as variáveis
SHIB = os.getenv('SHIB')

# Configuração do WebDriver
def setup_webdriver():
    # Configurando o driver do Chrome automaticamente
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # Executa o navegador em modo headless (sem interface gráfica)
    options.add_argument("--disable-gpu")  # Otimiza o uso em headless
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(service=service, options=options)
    return driver

# Função para acessar o site e capturar o valor do XPath
def get_value_from_xpath():
    # Inicializa o WebDriver
    driver = setup_webdriver()

    try:
        # URL do site
        url = f"https://unmineable.com/address/{SHIB}?coin=SHIB"
        driver.get(url)  # Acessa o site
        driver.implicitly_wait(10)  # Espera o carregamento dos elementos da página
        time.sleep(25)

        # Encontra o elemento pelo XPath
        xpath = '//*[@id="app"]/section/div/div/div[3]/div/div/div[2]/div/div/div[1]/div/div/div/span'
        element = driver.find_element(By.XPATH, xpath)

        # Obtém o texto do elemento
        value = element.text
        print(f"Valor capturado: {value}")

    except Exception as e:
        print("Erro ao capturar o valor:", e)

    finally:
        # Fecha o navegador
        driver.quit()

# Executa o script
if __name__ == "__main__":
    get_value_from_xpath()
