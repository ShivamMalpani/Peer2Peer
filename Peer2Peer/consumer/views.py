from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from .models import Products, Cart
from .serializers import ListProductSerializer, CheckoutSerializer
import pymongo
import datetime

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Peer2Peer"]
Cart = mydb["Cart"]
Container = mydb["Container"]
Comments = mydb["Comments"]
Ratings = mydb["Ratings"]
Order = mydb["Order"]

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

    def get(self, request, userID):
        cart = Cart.find_one({"_id":userID},{'product_list':1})

        return Response({"data": cart["product_list"]})

    # queryset = Products.objects.all()
'''    def post(self, request, pk):
        # update api
        data = request.data
        response = Cart.insert_one(data)
        return Response({"message": "Ok"})
'''

class InsertToCart(APIView):
    def post(self, request, pk):
        l = Cart.findone({"id": pk}, {"products": 1})
        # p = []
        if l:
            data = request.data
            products = l[0]["products"].append(data["product"])
            Cart.update_one({"id": pk}, {"$set": {"products": products, "quantity": data["quantity"]}})
            Response({"Success"})
        else:
            x = Cart.insert_one(request.data)
            Response("success")

class clearCart(APIView):
    def delete(self, userID):
        pass

class ProductCartDetails(APIView):
    def get(self):
        pass


class ViewCreateContainer(APIView):
    def get(self, id):
        container = Container.findone({"id": id})
        Response(container)

    def post(self, request):
        data = request.data
        create = Container.insert_one(data)
        Response("Success")


class ListCreateReviews(APIView):
    def get(self, pk):
        l = Comments.find({"product": pk})
        Response(l)

    def post(self, requests, pk, user):
        l = Comments.findone({"product": pk})
        data = requests.data
        l = l["comments_list"].append({"user": user, "time": datetime.now(), "comment": data})
        Response("Success")


class ViewUpdateRatings(APIView):
    def get(self,product, userID):
        pass
    def update(self,product, userID):
        pass

class ListCreateRatings(APIView):
    def get(self, product):
        l = Ratings.findone({"product": product})
        count = 0
        for i in l["ratings_list"]:
            sum += i["rating"]
            count += 1
        Response(sum / count)

    def post(self, product):
        pass



class Checkout(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = CheckoutSerializer


class ListOrder(APIView):
    def get(self, user):
        pass

class UpdateOrder(APIView):
    def update(self,userID):
        pass


class ViewOrder(APIView):
    def get(self, orderid):
        response = Order.find({"id": orderid})
        return Response(response)

class Coupon(APIView):
    def get(self, code):
        pass
