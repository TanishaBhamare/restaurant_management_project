from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=200)

    def __str(self):
        return self.name
