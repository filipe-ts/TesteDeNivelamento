import pytest
from app import create_app
import pandas as pd
from pathlib import Path


@pytest.fixture(scope='module')
def test_client():
    class TestConfig:
        # CSV_PATH = f'{Path(__file__).parent.resolve()}/assets/relatorio_test.csv'  # Use a test CSV
        CSV_PATH = '/Users/filipesoares/Documents/Code/IntuitiveCare/Teste-04/back-end/tests/assets/relatorio_test.csv'
        TESTING = True

    app = create_app(config_class=TestConfig)

    with app.test_client() as testing_client:
        with app.app_context():
            yield testing_client