from django.db import models

class ranking(models.Model):
    month=models.CharField(max_length=20,default="")
    units101=models.IntegerField()
    units102=models.IntegerField()
    units103=models.IntegerField()
    units104=models.IntegerField()
    units105=models.IntegerField()
    units106=models.IntegerField()
    units107=models.IntegerField()
    units108=models.IntegerField()
    units109=models.IntegerField()
    units110=models.IntegerField()
    def __str__(self):
        return self.month

class query(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    query=models.TextField()
    def __str__(self):
        return self.name