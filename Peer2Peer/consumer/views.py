from django.contrib.auth import authenticate
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.views import APIView
from .models import Products, Cart, Coupon
from rest_framework.authtoken.models import Token
from .serializers import ListProductSerializer, CheckoutSerializer, CouponSerializer, LoginSerializer
from .connection import mydb
from .trie import *


Cart = mydb["Cart"]
Container = mydb["Container"]
Comments = mydb["Comments"]
Ratings = mydb["Ratings"]
Order = mydb["Order"]


class UserSignupView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            request,
            username=serializer.validated_data['email'],
            password=serializer.validated_data['password']
        )

        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response(
                {'error': 'Invalid credentials'},
                status=status.HTTP_401_UNAUTHORIZED
            )


class ViewUpdateDeleteProducts(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ListProductSerializer


class ListCreateProducts(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ListProductSerializer


class ViewDeleteCart(APIView):

    def get(self,request):
        userID = self.request.query_params.get("userid")
        print(userID)
        cart = Cart.find_one({"_id": userID}, {'product_list': 1})
        if cart is None:
            return Response({"data":{}})
        print(cart)
        return Response({"data": cart["product_list"]})

    def delete(self):
        userID = self.request.query_params.get("userid")
        Cart.delete_one({"_id": userID})
        return Response("success")


'''    def post(self, request, pk):
        # update api
        data = request.data
        response = Cart.insert_one(data)
        return Response({"message": "Ok"})
'''


class InsertToCart(APIView):
    def post(self, request):
        userID = self.request.data.get("userID")
        entry = Cart.find_one({"_id": userID})
        print(userID)
        print(entry)
        # p = []
        data = request.data
        print(data)
        if entry is not None:
            # print(4553)
            entry["product_list"][data["product"]] = data["quantity"]
            # print(231)
            Cart.update_one({"_id": userID}, {"$set": {"product_list": entry["product_list"]}})
            # print(1279)
            return Response("Success", status=status.HTTP_200_OK)
        else:
            x = Cart.insert_one({"_id": data["userID"], "product_list": {data["product"]: data["quantity"]}})
            return Response("success")

    #     {
    # "userID":"U123",
    # "product":"Clothes",
    # "quantity":1}


class ProductCartDetails(APIView):
    def get(self):
        pass


class ViewCreateContainer(APIView):
    def get(self, request):
        id = self.request.query_params.get('id')
        # print(id)
        container = Container.find_one({"_id": id})
        if container is None:
            return Response("gj")
        return Response({"data":container["product_list"]})

    def post(self, request):
        # how to give id?
        print(id)
        data = request.data
        print(data)
        Container.insert_one({"_id": data["id"], "product_list": data["product_list"]})
        return Response("Success")


#     Example: {"id":"123", "product_list":{"P444":1}}


class ListCreateReviews(APIView):
    pagination_class = PageNumberPagination
    page_size = 2

    def get(self, request, product):
        # print(product)
        data = Comments.find_one({"_id": product})
        return Response(data)

    def post(self, requests, product):
        entry = Comments.find_one({"_id": product})
        data = requests.data

        if entry:
            entry["reviews"][data["userID"]] = data["review"]
            Comments.update_one({"_id": product}, {"$set": {"reviews": entry["reviews"]}})
        else:
            print({"_id": product, "reviews": {data["userID"]: data["review"]}})
            Comments.insert_one({"_id": product, "reviews": {data["userID"]: data["review"]}})
        return Response("Success")


# {
# "review":"Good product",
# "userID":"U123"
# }

class ViewUpdateRatings(APIView):
    def get(self, requests, product, userID, rate):
        data = Ratings.find_one({"_id": product})
        print(data)
        try:
            if data and data["ratings"][userID]:
                return Response({"rating": data["ratings"][userID]})
            return Response({"rating": 0})
        except:
            return Response({"rating": 0})

    def put(self, requests, product, userID, rate):
        data = Ratings.find_one({"_id": product})
        if data is None:
            data = {"_id": product, "ratings": {}}
            entry = data["ratings"]
            entry[userID] = rate
            Ratings.insert_one({"_id": product, "ratings": entry})
        else:
            entry = data["ratings"]
            entry[userID] = rate
            Ratings.update_one({"_id": product}, {"$set": {"ratings": entry}})
        print(entry)
        return Response("Success")


class ListRatings(APIView):
    def get(self, requests, product):
        data = Ratings.find_one({"_id": product})
        print(data)
        if data is None:
            return Response({"ratings": 0, "users_count": 0})
        count = 0
        sum = 0
        for userID in data["ratings"]:
            sum += int(data["ratings"][userID])
            count += 1
        return Response({"ratings": sum / count, "users_count": count})


class Checkout(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = CheckoutSerializer


class ListOrder(APIView):
    def get(self, request):
        userid = self.request.query_params.get('orderid')
        response = Order.find_all({"userid": userid})
        return Response(response)


class UpdateOrder(APIView):
    def put(self):
        pass


class ViewOrder(APIView):
    def get(self):
        orderid = self.request.query_params.get('orderid')
        response = Order.find({"id": orderid})
        return Response(response)


class SearchProducts(APIView):
    def get(self,request):
        query = self.request.query_params.get('query')
        search = Search()
        words = search.starts_with(query)
        return Response({"words": words})


class Coupons(APIView):
    serializer_class = CouponSerializer

    def get_queryset(self):
        code = self.request.query_params.get('code')
        queryset = Coupon.objects.all()

        if code:
            queryset = queryset.filter(code=code)
        return queryset

    def get(self, request):
        queryset = self.get_queryset()
        serializer = CouponSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CouponSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response({"message": "Success"})
        else:
            return Response({"message": "Failure"})
