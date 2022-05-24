from django.db import models
import os

# Create your models here.


class Paths(models.Model):
    path = models.CharField(max_length=200, unique=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE)

    def __str__(self) -> str:
        if self.path != "/":
            return os.path.join(str(self.parent), self.path)
        return "/"


