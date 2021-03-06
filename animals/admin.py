from django.contrib import admin
from .models import Animal, AnimalCard,  \
    Family, Kind, ZooImage

admin.site.register(Animal)
admin.site.register(AnimalCard)
admin.site.register(Family)
admin.site.register(Kind)
admin.site.register(ZooImage)
