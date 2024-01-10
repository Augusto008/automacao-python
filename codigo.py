import pyautogui
import time

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
email_login = "email@email.com.br"
password = "$%@!64852%$"

pyautogui.PAUSE = 1	

# Passo 1 - Entrar no sistema da empresa
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")
time.sleep(3)
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)

# Passo 2 - Fazer login
pyautogui.click(x=1001, y=362)
pyautogui.write(email_login)
pyautogui.press("tab")
pyautogui.write(password)
pyautogui.press("tab")
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

  pyautogui.write(tabela.loc[linha, "codigo"])
  pyautogui.press("tab")
  pyautogui.write(tabela.loc[linha, "marca"])
  pyautogui.press("tab")
  pyautogui.write(tabela.loc[linha, "tipo"])
  pyautogui.press("tab")
  pyautogui.write(str(tabela.loc[linha, 'categoria']))
  pyautogui.press("tab")
  pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
  pyautogui.press("tab")
  pyautogui.write(str(tabela.loc[linha, "custo"]))
  pyautogui.press("tab")
  obs = tabela.loc[linha, "obs"]
	
  if not pandas.isna(obs):
    pyautogui.write(tabela.loc[linha, "obs"])
	  
  pyautogui.press("tab")
  pyautogui.press("enter")

  pyautogui.scroll(5000)
