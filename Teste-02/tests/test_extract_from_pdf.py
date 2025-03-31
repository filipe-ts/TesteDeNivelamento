import camelot
import pathlib


# obtendo arquivo da etapa anterior
src_directory = pathlib.Path(__file__).parent.parent.parent.absolute()
pdf_file_path = f'{src_directory}/Teste-01/src/data/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf'

def test_should_extract_something():
    tables = camelot.read_pdf(pdf_file_path)
    assert len(tables) > 0

