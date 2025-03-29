from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import re
import requests

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
responses = [requests.get(link) for link in pdf_links]

for response in responses:
    pdf_blob = response.content
    print(pdf_blob)
