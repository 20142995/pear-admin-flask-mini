from common import register_api
from .file_api import FilePhotoAPI

def register_file_api(api_bp):
    register_api(FilePhotoAPI, 'photo_api', '/file/photo/', pk='photo_id', app=api_bp)
