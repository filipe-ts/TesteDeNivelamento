\i Operadoras.sql

\copy operadora (Registro_ANS, CNPJ, Razao_Social, Nome_Fantasia, Modalidade, Logradouro, Numero, Complemento, Bairro, Cidade, UF, CEP, DDD, Telefone, Fax, Endereco_eletronico, Representante, Cargo_Representante, Regiao_de_Comercializacao, Data_Registro_ANS) FROM './Data/Relatorio_cadop.csv' DELIMITER ';' CSV HEADER;

\i DemonstracoesContabeis.sql

\copy demonstracao_contabel ("DATA", REG_ANS, CD_CONTA_CONTABIL, DESCRICAO, VL_SALDO_INICIAL, VL_SALDO_FINAL) FROM './Data/2023/1T2023.csv' DELIMITER ';' CSV HEADER;

\copy demonstracao_contabel ("DATA", REG_ANS, CD_CONTA_CONTABIL, DESCRICAO, VL_SALDO_INICIAL, VL_SALDO_FINAL) FROM './Data/2023/2t2023.csv' DELIMITER ';' CSV HEADER;

\copy demonstracao_contabel ("DATA", REG_ANS, CD_CONTA_CONTABIL, DESCRICAO, VL_SALDO_INICIAL, VL_SALDO_FINAL) FROM './Data/2023/3T2023.csv' DELIMITER ';' CSV HEADER;

SET DateStyle = 'DMY';
\copy demonstracao_contabel ("DATA", REG_ANS, CD_CONTA_CONTABIL, DESCRICAO, VL_SALDO_INICIAL, VL_SALDO_FINAL) FROM './Data/2023/4T2023.csv' DELIMITER ';' CSV HEADER;

SET DateStyle = 'ISO';
\copy demonstracao_contabel ("DATA", REG_ANS, CD_CONTA_CONTABIL, DESCRICAO, VL_SALDO_INICIAL, VL_SALDO_FINAL) FROM './Data/2024/1T2024.csv' DELIMITER ';' CSV HEADER;

\copy demonstracao_contabel ("DATA", REG_ANS, CD_CONTA_CONTABIL, DESCRICAO, VL_SALDO_INICIAL, VL_SALDO_FINAL) FROM './Data/2024/2T2024.csv' DELIMITER ';' CSV HEADER;

\copy demonstracao_contabel ("DATA", REG_ANS, CD_CONTA_CONTABIL, DESCRICAO, VL_SALDO_INICIAL, VL_SALDO_FINAL) FROM './Data/2024/3T2024.csv' DELIMITER ';' CSV HEADER;

\copy demonstracao_contabel ("DATA", REG_ANS, CD_CONTA_CONTABIL, DESCRICAO, VL_SALDO_INICIAL, VL_SALDO_FINAL) FROM './Data/2024/4T2024.csv' DELIMITER ';' CSV HEADER;