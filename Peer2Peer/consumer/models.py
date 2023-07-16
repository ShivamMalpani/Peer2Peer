from django.db import models

# Create your models here.
class UserDetails(models.Model):
    

    def __str__(self):
        return self.title