from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from calculation import *
from sequence import *
from get_data import *
from treat_data import *

# Inicializar o driver
service = ChromeDriverManager(version="119.0.6045.160").install()
driver = webdriver.Chrome(service)

# Variaveis
url = 'https://blaze.com/pt/games/crash?modal=crash_history_index'

# Navegar até o url e pegar os dados
multiplier_list = get_data(driver, url)

# Tratar os dados
data = treat_data(multiplier_list) 

# Pegando inputs
bets = int(input('Quantas vezes você vai apostar: '))
betting_bank = float(input('Qual sua banca inicial: '))
crash = float(input('Deseja parar quando o multiplicador atingir: '))
money = float(input('Quanto deseja apostar por rodada: '))

# Pegar um sequencia aleatoria dos dados
sequence(data, bets)

# Calcular se ganhou ou perdeu
betting_bank = calculation(sequence_list, betting_bank, crash, money)

print(f'Sua banca final foi de {betting_bank}!')