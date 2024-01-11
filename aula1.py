#Automação para cadastrar produtos em estoque.
    #Passo 1 - Entrar e logar no sistema da empresa
    #Passo 2 - importar a database
    #Passo 3 - Cadastrar um produto e repetir até o fim da database
    
    
# Passo 1

import pyautogui
import time
pyautogui.PAUSE = 0.8

link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
email = 'drielli.intensivo@automacao.com'
senha = 'testandoessamerda'

pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("Enter")
pyautogui.click(x=251, y=69)
pyautogui.write(link)
pyautogui.press("Enter") 
pyautogui.click(x=703, y=411)
pyautogui.write(email)
pyautogui.press("Tab")
pyautogui.write(senha)
pyautogui.press('Tab')
pyautogui.press('Enter')
time.sleep(2)


#Passo 2 

import pandas
import numpy

tabela = pandas.read_csv("produtos.csv") #a pasta não pode estar dentro de outra pasta, de preferência que esteja na área de trabalho.



# Passo 3

for linha in tabela.index:

    codigo = tabela.loc[linha, 'codigo']
    marca = tabela.loc[linha, 'marca']
    tipo = tabela.loc[linha, 'tipo']
    categoria = tabela.loc[linha, 'categoria']
    preco_unitario = tabela.loc[linha, 'preco_unitario']
    custo = tabela.loc[linha, 'custo']
    obs = tabela.loc[linha, 'obs']

    pyautogui.click(x=942, y=290)
    pyautogui.write(codigo)
    pyautogui.press('Tab')
    pyautogui.write(marca)
    pyautogui.press('tab')
    pyautogui.write(tipo)
    pyautogui.press('tab')
    pyautogui.write(str(categoria))
    pyautogui.press('tab')
    pyautogui.write(str(preco_unitario))
    pyautogui.press('tab')
    pyautogui.write(str(custo))
    pyautogui.press('tab')
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press('tab')
    pyautogui.press('Enter')

    pyautogui.scroll(5000)








