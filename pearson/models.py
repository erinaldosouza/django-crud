from django.db import models


# Create your models here.
class Pearson(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    register_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + " " + self.last_name

