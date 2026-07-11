# Projeto de automação para preenchimento de produtos no sistema da empresa
# 1 - Entrar no sistema da empresa
# 2 - Fazer login
# 3 - Importar a base de produtos pra cadastrar no sisema
# 4 - Cadastrar produto
# 5 - Repetir o processo até cadastrar todos os produtos

import pyautogui
import time
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.3

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
email = "usuario@gmail.com"
senha = "********"

pyautogui.press("Win")
time.sleep(1)
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(5)
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(5)
pyautogui.click(x=478, y=444)
pyautogui.write(email)
pyautogui.press("tab")
time.sleep(1)
pyautogui.write(senha)
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)

import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
    pyautogui.click(x=510, y=292)
    time.sleep(0.2)
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")
    time.sleep(0.2)
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")
    time.sleep(0.2)
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")
    time.sleep(0.2)
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    time.sleep(0.2)
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")
    time.sleep(0.2)
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    time.sleep(0.2)
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")
    time.sleep(0.2)
    pyautogui.press("enter")
    pyautogui.scroll(1000)
    time.sleep(0.3)



