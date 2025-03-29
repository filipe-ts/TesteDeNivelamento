from _ast import pattern
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import re
import requests


url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
link = urlopen(url)
html = link.read().decode('utf8')
soup = bs(html, 'html.parser')

link1 = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
link2 = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf"


def test_should_return_not_empty():
    result = soup.find_all('a')

    assert result is not None

def test_should_return_correct_lengh():
    correct_lenght = 3
    pattern_str = re.compile(r'Anexo I{1,2}\s*')

    result = soup.find_all('a', string=pattern_str)
    assert len(result) == correct_lenght

    correct_lenght = 2
    pattern_href = re.compile(r'.*?pdf')
    result = soup.find_all('a', string=pattern_str, href=pattern_href)

    assert len(result) == correct_lenght

def test_should_return_correct_href():
    # procura por tags <a> com Anexo I ou II dentro
    pattern_str = re.compile(r'Anexo I{1,2}\s*')
    pattern_href = re.compile(r'.*?pdf')
    result = soup.find_all("a", string=pattern_str, href=pattern_href)

    # selecionas os link para pdfs
    pdf_links = [item.get('href') for item in result]

    assert pdf_links == [link1, link2]

def test_should_get_something():
    responses = [requests.get(pdf_link) for pdf_link in [link1, link2]]

    for response in responses:
        assert response.status_code == 200