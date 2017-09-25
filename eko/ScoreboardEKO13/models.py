from django.db import models


class Name (models.Model):
    name = models.CharField(max_length=40)
    nickname = models.CharField(max_length=25)


class EventType (models.Model):
    etype = models.CharField(max_length=10)


class EventSubtype (models.Model):
    esubtype = models.CharField(max_length=30)


class Event (models.Model):
    timestamp = models.BigIntegerField()
    description = models.CharField(max_length=140)
    name_id = models.ForeignKey(Name, on_delete=models.CASCADE)
    etype_id = models.ForeignKey(EventType, on_delete=models.PROTECT)
    esubtype_id = models.ForeignKey(EventSubtype, on_delete=models.PROTECT)

# Create your models here.
