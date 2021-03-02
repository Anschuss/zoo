from django.core.management.base import BaseCommand, CommandError
from animals.models import Family, Kind, Food


class Command(BaseCommand):
    help = 'Add object to Database'

    def handle(self, *args, **options):
        family = ['Ursus', 'Psittacidae', 'Canis', 'Hippopotamidae', 'Felidae']
        food = ['Мясо', 'Сено', 'Зерно', 'Фрукты', 'Овощи', 'Корм']
        all_kind = [['americanus' 'arctos', 'maritimus', 'thibetanus'],
                    ['Poicephalus', 'Psittacus', 'Bavaripsitta'],
                    ['familiaris', 'lupus', 'latrans', 'lupaster', 'simensis', 'aureus'],
                    ['amphibius', 'liberiensis'],
                    ['Panthera', ' Neofelis', 'Catopuma', 'Pardofelis',
                     ' Caracal', 'Leptailurus', ' Leopardus', 'Lynx',
                     'Puma', 'Herpailurus', ' Acinonyx', 'Prionailurus', 'Otocolobus', 'Felis']]

        for name in family:
            fmly = Family.objects.create(name=name)
            fmly.save()
            for kind in all_kind:
                for kind_name in kind:
                    knd = Kind.objects.create(name=kind_name, family_id=fmly.id)
                    knd.save()
                all_kind.remove(kind)
                break

        for food_name in food:
            elm = Food.objects.create(name=food_name)
            elm.save()
