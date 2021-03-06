from django.contrib import admin
from .models import News, Tag, Them

admin.site.register(News)
admin.site.register(Them)
admin.site.register(Tag)
