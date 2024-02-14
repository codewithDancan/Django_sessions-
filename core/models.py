from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='products', default='img/no_image.png')

    def __str__(self):
        return self.title

