from django.db import models

# Create your models here.
class Products(models.Model): #sql
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

class Reviews(models.Model): # sql/nosql
    productID = models.CharField()
    userID = models.CharField()
    review = models.CharField()
    time = models.DateTimeField()
    # add edit field later
    # edit = models.BooleanField(default=False)
    def __str__(self):
        return self.title
class Ratings(models.Model): # nosql
    productID = models.CharField()
    userID = models.CharField()
    ratings = models.CharField()
    time = models.DateTimeField()

    def __str__(self):
        return self.title


    def __str__(self):
        return self.title

class Cart(models.Model): # nosql/sql
    productID = models.CharField()
    userID = models.CharField()
    price = models.IntegerField()
    discount = models.IntegerField()
    quantity = models.IntegerField()


class Container(models.Model): # nosql
    productID = models.CharField()
    ContainerID = models.CharField() # use UUIDField
    price = models.IntegerField()
    discount = models.IntegerField()
    quantity = models.IntegerField()

class User(models.Model): # sql
    name = models.CharField()


class Newsletter(models.Model): # sql
    userID = models.CharField()
    emailID = models.EmailField()

class HomePage(): # sql
    pass

class Orders(models.Model): # nosql
    orderID = models.IntegerField()
    userID = models.CharField()
    time = models.DateTimeField()
