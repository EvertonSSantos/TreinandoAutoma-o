import pyautogui
import time



# pyautogui.click -> clicar em algum lugar
# pyautogui.press -> apertar 1 tecla
# pyautogui.write -> escrever einamentos.com/python/intensivao/login

pyautogui.PAUSE = 5

# passo 1: Entrar no sistema da empresa -https://dlp.hashtagtreinamentos.com/python/intensivao/login
# abrir chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# digitar o site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(5)

# time.sleep(3) espera 3 seg

pyautogui.click(707, 407)
# passo 2: Fazer login
# passo 3: Importar a base de dados 
# passo 4: Cadastrar 1 produto
# passo 5: Repetir para todos os produtos
