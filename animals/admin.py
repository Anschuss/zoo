from django.contrib import admin
from .models import Animal, AnimalCard, Food, \
    Family, Kind, ZooImage

admin.site.register(Animal)
admin.site.register(AnimalCard)
admin.site.register(Food)
admin.site.register(Family)
admin.site.register(Kind)
admin.site.register(ZooImage)
