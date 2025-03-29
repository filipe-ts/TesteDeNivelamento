from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import re
import requests
import os
import zipfile
import pathlib

# extrai o html do site
url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
link = urlopen(url)
html = link.read().decode('utf8')

# cria objeto representando a página html
soup = bs(html, 'html.parser')

# procura por tags <a> com Anexo I ou II dentro
pattern_str = re.compile(r'Anexo I{1,2}\s*')
pattern_href = re.compile(r'.*?pdf')
result = soup.find_all("a", string=pattern_str, href=pattern_href)

# selecionas os link para pdfs
pdf_links = [item.get('href') for item in result]

# faz o download
pdf_blobs = [requests.get(link).content for link in pdf_links]

# salva os pdfs na pasta /data
files = []
for index, blob in enumerate(pdf_blobs):
    file_name = f'{os.getcwd()}/data/{pdf_links[index].split("/")[-1]}'
    files.append(file_name)
    with open(file_name, 'wb') as f:
        f.write(blob)

# salvando os arquivos em um zip na pasta compressed
with zipfile.ZipFile(f"{os.getcwd()}/compressed/anexos.zip", 'w') as zf:
    data_directory = pathlib.Path(f"{os.getcwd()}/data/")
    for file_path in data_directory.iterdir():
        if file_path.name.endswith(".pdf"):
            zf.write(file_path, file_path.name)