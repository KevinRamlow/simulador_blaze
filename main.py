from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from calculation import *
from sequence import *

# Iniciarlizar o driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Variaveis
data = {}
c = 0
url = 'https://blaze.com/pt/games/crash?modal=crash_history_index'

# Navegar até o url e pegar os dados
# Separa esse codigo em um função getData(driver, url)
# retornar o multiplier_list (eu chamaria de multiplier_dict, pq é um dicionario, e nao uma lista)
driver.get(url)

history = driver.find_element(By.ID, 'history')
multiplier_list = history.find_elements(By.CLASS_NAME, 'bet-amount')

# Tratar os dados
# Separa esse codigo em uma função treatData(multiplier_list)
# Cria a variavel data = {} fora dessa função mas dentro do mesmo arquivo
# Dentro da função retorna a variavel data
for element in multiplier_list:
    multiplier = float(element.text.replace(' x', ''))
    data[c] = multiplier
    c += 1

# Pegando inputs
bets = int(input('Quantas vezes você vai apostar: '))
betting_bank = float(input('Qual sua banca inicial: '))
crash = float(input('Deseja parar quando o multiplicador atingir: '))
money = float(input('Quanto deseja apostar por rodada: '))

# fazer os calculos
sequence(data, bets)
calculation(sequence_list, betting_bank, crash, money)
