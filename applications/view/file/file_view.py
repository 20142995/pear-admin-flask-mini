from flask import render_template
from flask import Blueprint
from applications.view import index_bp
from common.utils.rights import view_logging_required, permission_required

file_bp = Blueprint('files', __name__)

@file_bp.get('/file')
@view_logging_required
@permission_required("admin:file:main")
def file_index():
    return render_template('admin/file/photo.html')


@file_bp.get('/file/photo/add')
@view_logging_required
@permission_required("admin:file:main")
def file_photo_add():
    return render_template('admin/file/photo_add.html')
