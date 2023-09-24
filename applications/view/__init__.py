from flask import Flask

from .system import index_bp,logs_bp,role_bp
from .file import file_bp

def init_view(app: Flask):
    app.register_blueprint(index_bp)
    app.register_blueprint(logs_bp)
    app.register_blueprint(role_bp)
    app.register_blueprint(file_bp)
