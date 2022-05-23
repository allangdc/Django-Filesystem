from django.db import models

# Create your models here.


class Paths(models.Model):
    path = models.CharField(max_length=200, unique=True)

    def __str__(self) -> str:
        return self.path
