from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=15)
    slug = models.SlugField(unique=True)


class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    ticket_type = models.CharField(max_length=15)
    price = models.IntegerField()
