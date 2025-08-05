from django.db import models
 
class Contact(models.Model):
    name = models.CharField(max_lenght=100)
    email = models.EmailField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def__str__(self):
        return f"{self.name} - {self.email}"