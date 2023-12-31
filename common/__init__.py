def register_api(view, endpoint, url, pk='id', pk_type='int', app=None):
    view_func = view.as_view(endpoint)
    app.add_url_rule(url, defaults={pk: None}, view_func=view_func, methods=['GET', ])
    app.add_url_rule(url, view_func=view_func, methods=['POST', ])
    app.add_url_rule(f'{url}<{pk_type}:{pk}>', view_func=view_func, methods=['GET', 'PUT', 'DELETE'])
