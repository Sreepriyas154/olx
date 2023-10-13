from  rest_framework import serializers
from api.views import Vechicles
from api.models import Reviews
from django.contrib.auth.models import User
class VechicleSerializers(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    brand=serializers.CharField()
    color=serializers.CharField()
    price=serializers.IntegerField()

    def create(self, validated_data):
        return Vechicles.objects.create(**validated_data)

class Vechicleserializer(serializers.ModelSerializer):
    id=serializers.IntegerField(read_only=True)
    class Meta:
        method=Vechicles
        fields="__all__"

        def validate_price(self, value):
            if value not in range(50, 1000):
                raise serializers.ValidationError("invalid error")  # field level validtaion
            return value

        def validate_qty(self, value):
            if value not in range(50, 1000):
                raise serializers.ValidationError("invalid error")  # field level validtaion
            return value


class ReviewSerializer(serializers.ModelSerializer):
    created_date=serializers.CharField(read_only=True)
    class Meta:
        model=Reviews
        fields="__all__"



class Userserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["first_name","last_name","email","password"]

    def create(self, validated_data):
        return User.objects.create_user(User,**validated_data)