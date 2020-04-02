from django.db import models



class Config(models.Model):
    ip=models.CharField(max_length=255)
    site=models.CharField(max_length=255)

    def __str__(self):
        return self.ip


class Identifiant(models.Model):
    identifiant=models.CharField(max_length=255)
    mot_de_passe=models.CharField(max_length=255)

    def __str__(self):
        return self.identifiant
