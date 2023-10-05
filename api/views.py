from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import  Response
from api.models import Vechicles
from api.serializers import VechicleSerializers

# Create your views here.
class Productsview(APIView):
    def get(self,request,*args,**kwargs):
        qs=Vechicles.objects.all()
        serializer=VechicleSerializers(qs,many=True)
        return Response(data=serializer.data)

    def post(self,request,*args,**kwargs):
        bname=request.data.get("name")
        bbrand=request.data.get("brand")
        bcolor=request.data.get("color")
        bprice=int(request.data.get("price"))
        Vechicles.objects.create(name=bname,brand=bbrand,color=bcolor,price=bprice)
        return Response(data="created")