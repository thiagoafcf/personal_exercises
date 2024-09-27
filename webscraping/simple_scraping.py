# 1. Scraping simples de uma página
# Objetivo: Fazer uma requisição a um site de notícias, extrair os títulos das notícias
# da página inicial e salvar em um arquivo CSV.
# Exemplo de site: https://www.bbc.com
# Passos:
# Use requests para baixar o conteúdo da página.
# Use BeautifulSoup para extrair os títulos das notícias (geralmente estão em tags <h1>, <h2> ou <a>).
# Armazene os dados em um DataFrame do pandas e exporte para um arquivo CSV.

import requests
from bs4 import BeautifulSoup
import pandas as pd


# Função que recebe uma url do usuário, busca por títulos h1, h2 e h3 e os salva em um DataFrame
def simple_scraping(user_url):
    news_titles = []

    # Tenta fazer a requisição no servidor
    try:
        response = requests.get(user_url)
        response.raise_for_status()  # Verifica se a requisição foi bem-sucedida
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return

    extract = BeautifulSoup(response.text, 'html.parser')

    # Busca por múltiplas tags de título (Para buscar uma classe específica, usar class_="")
    for title_text in extract.find_all(['h1', 'h2', 'h3']):
        title = title_text.text.strip()
        news_titles.append(title)

    # Verifica se foram encontrados títulos. Se sim, cria um DataFrame em csv.
    if news_titles:
        df_news_titles = pd.DataFrame(news_titles, columns=["Titles"])
        df_news_titles.to_csv('news_titles.csv', index=False)
        print("Titles scraped and saved successfully!")
    else:
        print("No titles found on the page.")


url = input('\nPlease, insert a valid URL: ')
simple_scraping(url)
