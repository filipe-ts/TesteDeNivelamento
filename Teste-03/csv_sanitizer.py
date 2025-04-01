import pandas as pd
from pathlib import Path


def sanitize_number(number):
    """
    Transforma o separador do número de vírgula para ponto
    :param number: numero a ser sanitizado
    :return float
    """
    if pd.isna(number) or number == '':
        return 0

    number_str = str(number).strip().replace(',','.')
    number = float(number_str)

    return number

coluns_to_sanitize = ["VL_SALDO_INICIAL","VL_SALDO_FINAL"]

def modify_csv(path : Path):
    """
    Cria um data frame a partir de um arquivo .csv e depois sobreescreve o arquivo modificado.
    :param path:
    :return:
    """
    df = pd.read_csv(path, delimiter=';', decimal=',', thousands='.', encoding='utf-8')
    for col in coluns_to_sanitize:
        df[col] = df[col].apply(sanitize_number)
    df.to_csv(path, index=False, float_format='%.2f', sep=';')

# Pastas a serem vasculhadas
folder_path_2023 = Path(__file__).parent.joinpath('Data/2023')
folder_path_2024 = Path(__file__).parent.joinpath('Data/2024')
target_extension = "*.csv"

# sim, dois fors, para este problema basta. Aplicam modify_csv em cada csv localizado nas pastas
for file_path in folder_path_2023.glob(target_extension):
    if file_path.is_file():
        modify_csv(file_path)

for file_path in folder_path_2024.glob(target_extension):
    if file_path.is_file():
        modify_csv(file_path)