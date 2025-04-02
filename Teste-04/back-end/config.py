import os
from dotenv import load_dotenv
import pathlib

basedir = pathlib.Path(__file__).parent.resolve()
load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', "weak_secret_key")
    CSV_PATH = os.getenv('CSV_PATH', f'{basedir.parent.parent.resolve()}/Teste-03/Data/Relatorio_cadop.csv')

if __name__ == '__main__':
    print(Config.CSV_PATH) # verificando caminho do csv