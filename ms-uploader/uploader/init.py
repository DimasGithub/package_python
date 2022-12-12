import requests
from django.conf import settings

class UploadFile:
    url_domain = None
    token_key = None

    def __init__(self, url=None, token=None):
        if url == None and token == None:
            url = getattr(settings, 'MICRO_SERVICES_URL_UPLOAD', None)
            token = getattr(settings, 'MICRO_SERVICES_TOKEN_KEY', None)
        if url != None:
            self.url_domain = url
        if token != None:
            self.token_key = token
        
    def upload_files(self, file_upload):
        try:
            data = { 'file' : file_upload }
            response = request.post(self.url_domain, headers={'Authorization': 'Token %s'%self.token_key}, data=data)
            return response.json()
        except Exception:
            return response.json()
