import requests
import os

link1 = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
link2 = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf"

def test_should_save_file():
    response = requests.get(link1)
    file_name = link1.split("/")[-1]

    assert file_name == "Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"

    blob = response.content
    cwd = os.getcwd()
    data_folder = cwd + "/data"
    with open(data_folder + "/" + file_name, "w+b") as f:
        f.write(blob)

    with open(data_folder + "/" + file_name, "rb") as f:
        binary = f.read()

    assert binary == blob



