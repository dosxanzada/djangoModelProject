from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Smartphone(models.Model):
    name = models.CharField(max_length=50)
    brandId = models.ForeignKey(Brand, on_delete=models.PROTECT)
    images = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.name
        

class Accessories(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    brandId = models.ForeignKey(Brand, on_delete=models.PROTECT)
    images = models.ImageField(upload_to="images/")