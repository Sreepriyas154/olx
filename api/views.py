from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import  Response
from api.models import Vechicles,Reviews
from rest_framework.viewsets import ViewSet,ModelViewSet
from api.serializers import VechicleSerializers,ReviewSerializer,Userserializer
from django.contrib.auth.models import User
from rest_framework import authentication,permissions
from rest_framework.decorators import action
from api.models import Wishlists
# Create your views here.
class Productsview(APIView):
    def get(self,request,*args,**kwargs):
        qs=Vechicles.objects.all()
        serializer=VechicleSerializers(qs,many=True)
        return Response(data=serializer.data)

    def post(self,request,*args,**kwargs):
        serializer=VechicleSerializers(data=request.data)
        if serializer.is_valid():
            Vechicles.objects.create(**serializer.validated_data)
            return Response(data=serializer.data)
        else:
            return Response(serializer.errors)

class Productdetailview(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        vechicle=Vechicles.objects.get(id=id)
        serializer=VechicleSerializers(vechicle,many=False)
        return Response(data=serializer.data)
    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        Vechicles.objects.get(id=id).delete()
        return Response(data="deleted")
    def put(self,request,*args,**kwargs):
        id =kwargs.get("id")
        serializer =VechicleSerializers(data=request.data)
        if serializer.is_valid():
            Vechicles.objects.filter(id=id).update(**serializer.validated_data)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)


class Reviewview(APIView):
    def get(self,request,*args,**kwargs):
        reviews=Reviews.objects.all()
        serializer=ReviewSerializer(reviews,many=True)
        return Response(data=serializer.data)
    def post(self,request,*args,**kwargs):
        serializer=ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

class ReviewDetailview(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Vechicles.objects.get(id=id)
        serializer=VechicleSerializers(qs,many=False)
        return  Response(data=serializer.data)

    def put(self,request,*args,**kwargs):
        id= kwargs.get("id")
        qs=Reviews.objects.get(id=id)
        serializer=ReviewSerializer(instance=qs, data=request.data)  # modelserializer step
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
             return Response(data=serializer.errors)

    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        Vechicles.objects.get(id=id).delete()
        return Response(data="deleted")

class Productviewsetview(ViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def list(self,request,*args,**kwargs):
        qs=Vechicles.objects.all()
        serializer=VechicleSerializers(qs,many=True)
        return Response(data=serializer.data)
    def create(self,request,*args,**kwargs):
        serializer=VechicleSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Vechicles.objects.get(id=id)
        serializer=VechicleSerializers(qs,many=False)
        return Response(data=serializer.data)

    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Vechicles.objects.get(id=id)
        serializer = VechicleSerializers(instance=qs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Vechicles.objects.get(id=id).delete()
        return Response(data="deleted")

class Productmodelviewsetview(ModelViewSet):
    serializer_class = VechicleSerializers
    queryset = Vechicles.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    @action(methods=["post"],detail=True)
    def add_review(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Vechicles.objects.get(id=id)
        user=request.user
        Reviews.objects.create(vechicle=qs,user=user,comment=request.data.get("comment"),rating=request.data.get("rating"))
        return Response(data="created")
    @action(methods=["get"],detail=True)
    def get_review(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Vechicles.objects.get(id=id)
        reviews=qs.reviews_set.all()
        serializer=ReviewSerializer(reviews,many=True)
        return Response(data=True)
    @action(methods=["post"],detail=True)
    def add_to_wishlist(self,request,*args,**kwargs):
        id=kwargs.get(("pk"))
        qs=Vechicles.objects.get(id=id)
        user=request.user
        Wishlists.objects.create(vechicle=qs,user=user,status=request.data.get("option"))
        return Response("created")


class Reviewsmodelviewsetview(ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Vechicles.objects.all()

    def list(self, request, *args, **kwargs):
        reviews=Reviews.objects.all()
        if 'user' not in request.query_params:
            review=Reviews.objects.filter(user=request.query_params.get("user"))
        serializer=ReviewSerializer(reviews,many=True)
        return Response(data=serializer.data)
class Usersview(ModelViewSet):
    serializer_class = Userserializer
    queryset =User.objects.all()

