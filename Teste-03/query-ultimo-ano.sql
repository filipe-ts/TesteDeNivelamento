CREATE INDEX IF NOT EXISTS idx_dc_reg_ans ON demonstracao_contabel (reg_ans);
CREATE INDEX IF NOT EXISTS idx_dc_data ON demonstracao_contabel ("DATA");
CREATE INDEX IF NOT EXISTS idx_op_registro_ans ON operadora (registro_ans);
SELECT p.id, p.registro_ans, p.razao_social, (-1* (dc.vl_saldo_final - dc.vl_saldo_inicial)) AS GASTO
    FROM operadora p JOIN
        (SELECT reg_ans, vl_saldo_inicial, vl_saldo_final, descricao
            FROM demonstracao_contabel WHERE (
                "DATA" >= '2024-01-01' AND
                descricao ILIKE 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
                    )
                        ) AS dc
    ON p.registro_ans = dc.reg_ans
    ORDER BY GASTO desc
    LIMIT 10;