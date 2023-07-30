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



class ViewUpdateDeleteProducts(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ListProductSerializer


class ListCreateProducts(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ListProductSerializer


class ViewDeleteCart(APIView):

    def get(self, request, userID):
        cart = Cart.find_one({"_id": userID}, {'product_list': 1})

        return Response({"data": cart["product_list"]})

    def delete(self, userID):
        Cart.delete_one({"_id":userID})



'''    def post(self, request, pk):
        # update api
        data = request.data
        response = Cart.insert_one(data)
        return Response({"message": "Ok"})
'''


class InsertToCart(APIView):
    def post(self, request, userID):
        entry = Cart.find_one({"_id": userID})
        print(12423)
        print(entry)
        # p = []
        data = request.data

        if entry:
            # print(4553)
            entry["product_list"][data["product"]] = data["quantity"]
            # print(231)
            Cart.update_one({"_id": userID}, {"$set": {"product_list": entry["product_list"]}})
            # print(1279)
            return Response("Success", status=status.HTTP_200_OK)
        else:
            x = Cart.insert_one({"_id": data["userID"], "product_list": {data["product"]: data["quantity"]}})
            Response("success")

    #     {
    # "userID":"U123",
    # "product":"Clothes",
    # "quantity":1}



class ProductCartDetails(APIView):
    def get(self):
        pass


class ViewCreateContainer(APIView):
    def get(self, request, id):
        # print(id)
        container = Container.find_one({"_id": id})
        return Response(container)

    def post(self, request, id):
        # how to give id?
        print(id)
        data = request.data
        print(data)
        Container.insert_one({"_id":data["id"],"product_list": data["product_list"]})
        return Response("Success")

#     Example: {"id":"123", "product_list":{"P444":1}}


class ListCreateReviews(APIView):
    def get(self,request, product):
        # print(product)
        data = Comments.find_one({"_id": product})
        return Response(data)

    def post(self, requests, product):
        entry = Comments.find_one({"_id": product})
        data = requests.data

        if entry:
            entry["reviews"][data["userID"]]=data["review"]
        else:
            print({"_id":product, "reviews":{data["userID"]:data["review"]}})
            Comments.insert_one({"_id":product, "reviews":{data["userID"]:data["review"]}})
        return Response("Success")

# {
# "review":"Good product",
# "userID":"U123"
# }

class ViewUpdateRatings(APIView):
    def get(self, product, userID):
        pass

    def update(self, product, userID):
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
    def update(self, userID):
        pass


class ViewOrder(APIView):
    def get(self, orderid):
        response = Order.find({"id": orderid})
        return Response(response)


class Coupon(APIView):
    def get(self, code):
        pass
