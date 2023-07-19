from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=10000)
    seller = models.CharField(max_length=100) # sellerid
    create_time = models.DateTimeField()
    last_updated = models.DateTimeField()
    # image =
    price = models.IntegerField()
    discount = models.IntegerField(default=0)
    customer_count = models.IntegerField()
    stock = models.IntegerField()
    category = models.CharField()

    def __str__(self):
        return self.title

class Reviews(models.Model):
    productID = models.CharField()
    userID = models.CharField()
    review = models.CharField()
    time = models.DateTimeField()

    def __str__(self):
        return self.title
class Ratings(models.Model):
    productID = models.CharField()
    userID = models.CharField()
    ratings = models.CharField()
    time = models.DateTimeField()

    def __str__(self):
        return self.title

class Comments(models.Model):
    productID = models.CharField()
    userID = models.CharField()
    comments = models.CharField()
    time = models.DateTimeField()
    edit = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Cart(models.Model):
    productID = models.CharField()
    userID = models.CharField()
    price = models.IntegerField()
    discount = models.IntegerField()
    quantity = models.IntegerField()

