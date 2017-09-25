from django.db import models


class Name (models.Model):
    name = models.CharField(max_length=40)
    nickname = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class ExploitType (models.Model):
    etype = models.CharField(max_length=10)
    description = models.CharField(max_length=140)
    
    def __str__(self):
        return self.etype


class Vuln (models.Model):
    name = models.ForeignKey(Name, on_delete=models.CASCADE)
    timestamp = models.BigIntegerField()
    description = models.CharField(max_length=140)
    
    def __str__(self):
        return self.description


class Exploit (models.Model):
    name = models.ForeignKey(Name, on_delete=models.CASCADE)
    vuln = models.ForeignKey(Vuln, on_delete=models.PROTECT)
    etype = models.ForeignKey(ExploitType, on_delete=models.PROTECT)
    timestamp = models.BigIntegerField()
    description = models.CharField(max_length=140)
    
    def __str__(self):
        return self.description

# Create your models here.
