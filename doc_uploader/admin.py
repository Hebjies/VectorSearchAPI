from django.contrib import admin
from .models import Document
# from rest_framework_api_key.admin import APIKeyModelAdmin

admin.site.register(Document, 
                    # APIKeyModelAdmin
                    )
