'''
2. Scraping de uma tabela HTML
Objetivo: Extrair dados de uma tabela em uma página da web e salvar em CSV.
Exemplo de site: https://www.worldometers.info/world-population/
Passos:
Faça o download da página com requests.
Localize a tabela com BeautifulSoup e extraia os dados.
Converta a tabela em um DataFrame do pandas e exporte para CSV.
'''

import requests
import pandas as pd
from io import StringIO


# Função que recebe uma url do usuário, busca tabelas e as salva em arquivos csv
def html_table_scraping(user_url):
    try:
        response = requests.get(user_url)
        response.raise_for_status()  # Verifica se a a requisição foi bem sucedida
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return

    # Correção para já adaptar o código para futuras versões do pandas, que pedirá objetos StringIO para o read_html
    try:
        html_data = StringIO(response.text)
        tables = pd.read_html(html_data)
    except ValueError as e:
        print(f"No tables found on the page: {e}")
        return

    if tables:
        # Itera sobre o índice (i) e sobre objetos (table) em conjunto, usando a função enumerate
        for i, table in enumerate(tables):
            file_name = f"html_table_{i+1}.csv"
            table.to_csv(file_name, index=False)
            print(f"Table {i+1} extracted and saved as {file_name} successfully!")
    else:
        print("No tables found.")


url = input("\nPlease, insert a valid URL: ")
html_table_scraping(url)

'''
Apesar de o enunciado pedir para utilizar o BeautifulSoup, foi sugerido pelo chatGPT usar a função read_html do pandas
por ser uma forma melhor para extrair as tabelas e mantê-las em formato tabular.
'''
