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
# passo 2: Fazer login
pyautogui.click(707, 407)
pyautogui.write("evertonever368@gmail.com")
pyautogui.press("tab")
pyautogui.write("eutonever")
pyautogui.press("tab")
pyautogui.press("enter")

# passo 3: Importar a base de dados 
import pandas as pd

tabela = pd.read_csv("produtos.csv")

print(tabela)

# passo 4: Cadastrar 1 produto
for linha in tabela.index:

   # clicar no botão de produtos         
    pyautogui.click(752, 291)

    #pegar da tabela o valor que a gente quer prencher
    codigo = tabela.loc[linha, "codigo"]

    #preencher o campo 
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))       
    pyautogui.press("tab")        
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab") 
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")    #cadastra o produto (botao enviar)      
 
     #dar scroll de tudo para cima
    pyautogui.scroll(5000)
    # passo 5: Repetir para todos os produtos