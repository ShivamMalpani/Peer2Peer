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
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Reviews(models.Model): # sql/nosql
    productID = models.CharField(max_length=100)
    userID = models.CharField(max_length=100)
    review = models.CharField(max_length=100)
    # time = models.DateTimeField()
    # add edit field later
    # edit = models.BooleanField(default=False)
    def __str__(self):
        return self.title
class Ratings(models.Model): # nosql
    productID = models.CharField(max_length=100)
    userID = models.CharField(max_length=100)
    ratings = models.CharField(max_length=100)
    time = models.DateTimeField()

    def __str__(self):
        return self.title


    def __str__(self):
        return self.title

class Cart(models.Model): # nosql/sql
    productID = models.CharField(max_length=100)
    userID = models.CharField(max_length=100)
    price = models.IntegerField()
    discount = models.IntegerField()
    quantity = models.IntegerField()


class Container(models.Model): # nosql
    productID = models.CharField(max_length=100)
    ContainerID = models.CharField(max_length=100) # use UUIDField
    price = models.IntegerField()
    discount = models.IntegerField()
    quantity = models.IntegerField()

class User(models.Model): # sql
    name = models.CharField(max_length=100)


class Newsletter(models.Model): # sql
    userID = models.CharField(max_length=100)
    emailID = models.EmailField()

class HomePage(): # sql
    pass

class Orders(models.Model): # nosql
    orderID = models.IntegerField()
    userID = models.CharField(max_length=100)
    time = models.DateTimeField()
