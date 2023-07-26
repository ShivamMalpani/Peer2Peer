from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from .models import Products, Cart
from .serializers import ListProductSerializer,CheckoutSerializer
import pymongo
import datetime


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Peer2Peer"]
Cart = mydb["Cart"]
Container = mydb["Container"]
Comments = mydb["Comments"]
Ratings = mydb["Ratings"]

mydict = {"id": "John", "address": "Highway 37"}
x = Cart.insert_one(mydict)
for x in Cart.find({'name': "John"}):
    print(x)

class ViewUpdateDeleteProducts(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ListProductSerializer


class ListCreateProducts(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ListProductSerializer


class ViewUpdateCart(APIView):

    def get(self,request,pk):
        cart = Cart.find()
        data = []
        for product in cart:
            print(product)
            try:
                data.append({"name":product["name"]})
            except Exception as err:
                pass
        return Response({"data":data})
    # queryset = Products.objects.all()
    def post(self,request,pk):
        # update api
        data = request.data
        response = Cart.insert_one(data)
        return Response({"message":"Ok"})

class InsertToCart(APIView):
    def post(self,request,pk):
        l = Cart.findone({"id":pk},{"products":1})
        # p = []
        if l:
            data = request.data
            products = l[0]["products"].append(data["product"])
            Cart.update_one({"id":pk},{"$set":{"products":products, "quantity":data["quantity"]}})
            Response({"Success"})
        else :
            x = Cart.insert_one(request.data)
            Response("success")

