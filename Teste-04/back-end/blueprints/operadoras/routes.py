from blueprints.operadoras import bp
from flask import current_app, jsonify, request, abort
from werkzeug.exceptions import BadRequest
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

@bp.route('/search/', methods=['POST'])
def search_by():
    search_args = ['CNPJ', 'Razao_Social', 'Nome_Fantasia']
    try:
        if not request.is_json:
            raise BadRequest("no json was given")
        data = request.get_json()
        search_arg = data.get('search')

        if not search_arg:
            raise BadRequest("no search parameter was given")
        elif search_arg not in search_args:
            raise BadRequest(f"{search_arg} is not valid. Use one of {search_args}")

        if 'value' not in data:
            raise BadRequest("no value field was given")

        search_element = str(data.get('value')).lower()

        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 20))

        if page < 1 or per_page < 1:
            raise BadRequest("Page and per_page must be positive integers")

        df: pd.DataFrame = current_app.df

        search_result = df[df[search_arg].astype(str).str.lower().str.contains(search_element, regex=False, na=False)]
        search_result = search_result.sort_values(by=search_arg)

        total_items = len(search_result)
        total_pages = (total_items + per_page - 1) // per_page

        if page > total_pages:
            if total_pages > 0:
                page = total_pages
            else:
                page = 1

        start_idx = (page - 1) * per_page
        end_idx = start_idx + per_page
        paginated_results = search_result.iloc[start_idx:end_idx]

        return {"operadoras": paginated_results.to_dict(orient="records"),
                "pagination": {
                    "total_items": total_items,
                    "total_pages": total_pages,
                    "current_page": page,
                    "per_page": per_page,
                    "has_next": page < total_pages,
                    "has_previous": page > 1
                  }
                }, 200
    except BadRequest as e:
        abort(400, str(e.description))
    except Exception as e:
        abort(500, str(e))
