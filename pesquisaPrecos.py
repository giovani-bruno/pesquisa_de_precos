from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import time
from enviar_email import enviar_email
from janela.janela import criar_janela
from tkinter import messagebox

# Função para iniciar o navegador (Chrome)
def iniciar_navegador():
  # Configura o serviço do ChromeDriver e inicia o navegador
  try:
    servico = Service(ChromeDriverManager().install())
    nav = webdriver.Chrome(service=servico)
  except:
    messagebox.showerror(title="Erro", message="O chrome não está instalado no seu computador.")
  return nav

# Função para realizar a pesquisa do produto no Google Shopping
def realizar_pesquisa(nav, produto, preco_min, preco_max):
  # URL para pesquisa no Google
  pesquisa_google = 'https://google.com/search?q='
  
  # Listas para armazenar resultados
  produtos = []
  precos = []
  links = []

  # Realiza a pesquisa no Google
  nav.get(pesquisa_google + produto)
  try:
    # Procura pelo elemento "Shopping" e clica
    for elemento in nav.find_elements(By.CLASS_NAME, 'YmvwI'):
      if "Shopping" in elemento.text:
        elemento.click()
        break
    
    # Preenche os campos de preço mínimo e máximo
    while len(nav.find_elements(By.CLASS_NAME, "baeIxf")) < 1: # Espera o elemento carregar
      time.sleep(1)
    campos = nav.find_elements(By.CLASS_NAME, "baeIxf")
    campos[0].send_keys(preco_min)
    campos[1].send_keys(preco_max)
    time.sleep(1)
    nav.find_element(By.CLASS_NAME, "sh-dr__prs").click()
    
    # Coleta os resultados da pesquisa
    elemento_produtos = nav.find_elements(By.CLASS_NAME, 'i0X6df')
    for elemento in elemento_produtos:
      nome = elemento.find_element(By.CLASS_NAME, "tAxDx").text
      preco = elemento.find_element(By.CLASS_NAME, "a8Pemb").text
      preco = preco.replace("R$", "").replace(" ", "").replace(".", "").replace(",", ".")
      if "+impostos" in preco:
        preco = preco.replace("+impostos", "")
      preco = float(preco)
      elemento_pai = elemento.find_element(By.CLASS_NAME, "bONr3b")
      link = elemento_pai.find_element(By.XPATH, '..').get_attribute('href')
      produtos.append(nome)
      precos.append(preco)
      links.append(link)
  except Exception as e:
    # Trata possíveis erros na pesquisa
    messagebox.showerror(title="Erro", message=f"Erro na pesquisa. Por favor, tente novamente.\n\n{e}")
  return produtos, precos, links

# Função para gerar a tabela de resultados em formato HTML
def gerar_tabela(produtos, precos, links):
  if len(produtos) == len(precos) == len(links):
    # Cria um DataFrame com os resultados
    df = pd.DataFrame({
        "Produto": produtos,
        "Preço": precos,
        "Link": links
    })
    
    # Encontra o índice do produto com o menor preço
    min_preco_index = df['Preço'].idxmin()
    
    # Converte o DataFrame para HTML e destaca o produto com menor preço
    tabela_html = df.to_html(index=False, escape=False, classes='dataframe')
    tabela_html_split = tabela_html.split('</tr>')
    tabela_html_split[min_preco_index + 1] = tabela_html_split[min_preco_index + 1].replace('<tr>', '<tr class="destaque">')
    tabela_html = '</tr>'.join(tabela_html_split)

    return tabela_html
  else:
    # Retorna None se houver inconsistência nos resultados
    return None

try:
  produto, preco_min, preco_max, email_usuario = criar_janela() # Obtém as informações do usuário
  if produto:
    nav = iniciar_navegador() # Inicia o navegador
    produtos, precos, links = realizar_pesquisa(nav, produto, preco_min, preco_max) # Realiza a pesquisa do produto
    nav.quit() # Encerra o navegador
    tabela_html = gerar_tabela(produtos, precos, links) # Gera a tabela de resultados em HTML

    # Envia o e-mail com os resultados ou exibe uma mensagem de erro
    if tabela_html: 
      enviar_email(email_usuario, tabela_html) # Esta função está em um arquivo separado por questões de segurança
    else:
      messagebox.showerror(title="Erro", message="Erro ao gerar tabela. Por favor, tente novamente.")
except TypeError: # Significa que o usuário fechou a janela, ou seja, desistiu
  pass