from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Project)
admin.site.site_header = 'My Portfolio Dashboard'