from blueprints.operadoras import bp
from flask import current_app, jsonify, request, abort
import pandas as pd

@bp.route('/hi')
def hi():
    return '<h1>Hi from \'operadoras/\'!</h1>'

@bp.route('/columns')
def columns():
    df: pd.DataFrame = current_app.df
    columns_json = {}
    for index, column in enumerate(df.columns):
        columns_json[index] = column

    return jsonify(columns_json), 200

@bp.route('/searchByCNPJ/', methods=['POST'])
def search_by_cnpj():
    try:
        data = request.get_json()
        cnpj = data.get('CNPJ')
        df: pd.DataFrame = current_app.df

        search_result = df[df['CNPJ'].astype(str).str.contains(str(cnpj), regex=False, na=False)]
        return {"operadoras": search_result.to_dict(orient="records"),
                "len": len(search_result)}, 200
    except Exception as e:
        abort(500, str(e))
