from django.db import models


class Family(models.Model):
    """ Animals Family: Bears - Ursus """
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Kind(models.Model):
    """ Animals Family Kind: brown bear, giant panda """
    name = models.CharField(max_length=64)
    family = models.ForeignKey(Family, on_delete=models.PROTECT)

    unique_together = [['name', 'family']]

    def __str__(self):
        return self.name


class AnimalCard(models.Model):
    """ animal information """
    text = models.TextField()

    def __str__(self):
        return self.text


class Food(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Animal(models.Model):
    name = models.CharField(max_length=64)
    age = models.PositiveIntegerField()
    card = models.OneToOneField(AnimalCard, on_delete=models.CASCADE, blank=True)
    food = models.ManyToManyField(Food)
    kind = models.ForeignKey(Kind, on_delete=models.PROTECT)
    img = models.ImageField(upload_to='animals', blank=True, null=True)

    def __str__(self):
        return self.name


class ZooImage(models.Model):
    img = models.ImageField(upload_to='zoo_img', blank=True, null=True)
