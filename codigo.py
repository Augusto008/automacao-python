# Passo a passo do projeto
	
# bibliotecas em python
  ## pyautogui - RPA - automação bot
    ### pip install pyautogui
  ## pandas, numpy, openpyxl
    ### pip install pandas numpy openpyxl
import pyautogui
import time

#clicar -> pyautogui.click
#escrever -> pyautogui.write
#pressionar -> pyautogui.press
#atalhos -> pyautogui.hotkey("ctrl", "C")
#scroll -> pyautogui.scroll

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
email_login = "email@email.com.br"
password = "$%@!64852%$"

pyautogui.PAUSE = 1	

# Passo 1 - Entrar no sistema da empresa
#aperta tecla do windows
pyautogui.press("win")
#digitar nome do programa("navegador")
pyautogui.write("edge")
#apertar enter
pyautogui.press("enter")
#aguarde 5 segundos
time.sleep(3)
#digitar o link
pyautogui.write(link)
#apertar enter
pyautogui.press("enter")
#Esperar 5 segundos neste passo
time.sleep(3)

# Passo 2 - Fazer login
#clicar no campo email
pyautogui.click(x=1001, y=362)
#digitar email
pyautogui.write(email_login)
#trocar para campo senha
pyautogui.press("tab")
#digitar senha
pyautogui.write(password)
#focar botão logar
pyautogui.press("tab")
#pressionar botão logar
pyautogui.press("enter")
time.sleep(3)

# Passo 3 - Importar base de dados
import pandas

tabela = pandas.read_csv("produtos.csv")
#print(tabela)

# Passo 4 - cadastrar um produto
#pyautogui.click(x=725, y=323)

#pyautogui.write("MOLO000251")
#pyautogui.press("tab")
#pyautogui.write("Logitech")  
#pyautogui.press("tab")
#pyautogui.write("Mouse")
#pyautogui.press("tab")
#pyautogui.write(str(1))
#pyautogui.press("tab")
#pyautogui.write("25.95")
#pyautogui.press("tab")
#pyautogui.write("6.5")
#pyautogui.press("tab")
#pyautogui.write("")
#pyautogui.press("tab")
#pyautogui.press("enter")

# Passo 5 - repetir até acabar a base de dados
#diminuir tempo para preenchimento do formulário
pyautogui.PAUSE = 0.2
for linha in tabela.index:
  pyautogui.click(x=866, y=239)

  #código
  pyautogui.write(tabela.loc[linha, "codigo"])
  pyautogui.press("tab")
  #marca
  pyautogui.write(tabela.loc[linha, "marca"])
  pyautogui.press("tab")
  #tipo
  pyautogui.write(tabela.loc[linha, "tipo"])
  pyautogui.press("tab")
  #categoria
  pyautogui.write(str(tabela.loc[linha, 'categoria']))
  pyautogui.press("tab")
  #preco_unitario
  pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
  pyautogui.press("tab")
  #custo
  pyautogui.write(str(tabela.loc[linha, "custo"]))
  pyautogui.press("tab")
  #obs
  obs = tabela.loc[linha, "obs"]
  if not pandas.isna(obs):
    pyautogui.write(tabela.loc[linha, "obs"])
  pyautogui.press("tab")
  #enviar
  pyautogui.press("enter")

  pyautogui.scroll(5000)