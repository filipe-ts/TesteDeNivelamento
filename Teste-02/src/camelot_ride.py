import camelot
import pathlib
import pandas as pd

# obtendo arquivo da etapa anterior
src_directory = pathlib.Path(__file__).parent.parent.parent.absolute()
pdf_file_path = f'{src_directory}/Teste-01/src/data/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf'

# lendo todas as tabelas com camelot, demora alguns minutos para executar
tables = camelot.read_pdf(pdf_file_path, pages="3-181", flavor='lattice', process_background=True, strip_text="\n")

# combinando todas as tabelas num único dataframe
combined_df = pd.concat([table.df for table in tables])

# Renomeia as colunas para os campos da segunda linha (onde de fato começa a tabela)
combined_df.columns = combined_df.iloc[0]

# Remove a segunda linha que agora é desnecessária
combined_df = combined_df.drop(0)

# Resetar os indexes, apenas boas práticas
combined_df.reset_index(drop=True, inplace=True)

# Renomeia os campos pedidos
renamed_columns = {
    "OD":"Seg. Odontológica",
    "AMB": "Seg. Ambulatorial",
}

combined_df.rename(columns=renamed_columns, inplace=True)

# local salvar o csv
csv_path = f'{pathlib.Path(__file__).parent.parent}/csv/anexo-I.zip'

# Exportando o csv zipado
combined_df.to_csv(csv_path,
                   index=False,
                   compression={
                       'method': 'zip',
                       'archive_name': 'anexo-I.csv',
                   })