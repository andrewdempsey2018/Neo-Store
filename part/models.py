from django.db import models


class Part(models.Model):
    name = models.CharField(max_length=30, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    image = models.ImageField(upload_to="images")

    # Method returns the models name as text
    def __str__(self):
        return self.name
