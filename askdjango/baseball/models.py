from django.db import models


class Stadium(models.Model):
    name = models.CharField(max_length=100)


class Block(models.Model):
    stadium = models.ForeignKey(Stadium)
    name = models.CharField(max_length=100)

class Seat(models.Model):
    block = models.ForeignKey(Block)
    row = models.PositiveIntegerField()
    col = models.PositiveIntegerField()
    photo = models.ImageField()

