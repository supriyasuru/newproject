from django.conf import settings
from django.db import models
from django.core.validators import FileExtensionValidator




class Tableone(models.Model):
    f1 = models.CharField(max_length=200)
    f2 = models.CharField(max_length=200)
    f3 = models.CharField(max_length=200)
    f4 = models.CharField(max_length=200)

    def __str__(self):
        return self.f1

class Tabletwo(models.Model):
    c1 = models.CharField(max_length=200)
    c2 = models.CharField(max_length=200)
    c3 = models.CharField(max_length=200)
    c4 = models.CharField(max_length=200)

    def __str__(self):
        return self.c1

class CsvImport(models.Model):
    files = models.FileField(validators=[FileExtensionValidator(allowed_extensions=['csv'])])

    def __str__(self):
        x=str(self.files)
        return x
