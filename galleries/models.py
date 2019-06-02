from django.db import models

class Galleries(models.Model):
    author=models.CharField(max_length=200)
    dirname=models.CharField(max_length=200)
    def __str__(self):
        return self.author
    
    