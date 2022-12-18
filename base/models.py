from django.db import models

class skill(models.Model):
    id = models.AutoField(primary_key=True)
    language = models.CharField(max_length=50)
    persentage = models.IntegerField()

class atchviements(models.Model):
    img = models.CharField(max_length=50)
    topic = models.CharField(max_length=50)
    date_place = models.CharField(max_length=50)

class certificate(models.Model):
    img = models.CharField(max_length=50)
    topic = models.CharField(max_length=50)
    date_place = models.CharField(max_length=50)

class projects(models.Model):
    id = models.AutoField(primary_key=True)
    img = models.CharField(max_length=500)
    topic = models.CharField(max_length=500)
    date_place = models.CharField(max_length=500)
    paragraph = models.CharField(max_length=500)

class hackthons(models.Model):
    img = models.CharField(max_length=50)
    topic = models.CharField(max_length=50)
    sub_topic = models.CharField(max_length=50)
    date_place = models.CharField(max_length=50)
    team = models.CharField(max_length=50)
    result = models.CharField(max_length=50)

