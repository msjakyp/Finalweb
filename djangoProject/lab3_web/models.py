from django.db import models


class Articles(models.Model):
    picture = models.ImageField('images', upload_to='images/')
    title = models.CharField('Flowers', max_length=50)
    price = models.CharField('Price', max_length=250)

    def __str__(self):
        return str(self.id) + " " + self.title

class Customers(models.Model):
    email = models.CharField('Email', max_length=20)
    phone = models.CharField("Phone", max_length=20)
    password = models.CharField("Password", max_length=20)

    def __str__(self):
        return self.email

class Orders(models.Model):
    # flowerid = models.ForeignKey(Articles, on_delete=models.CASCADE)
    # сustomerid = models.ForeignKey(Customers, on_delete=models.CASCADE)
    email = models.CharField('Email', max_length=20)

    def __str__(self):
        return self.email