from  rest_framework import serializers

class VechicleSerializers(serializers.Serializer):
    name=serializers.CharField()
    brand=serializers.CharField()
    color=serializers.CharField()
    price=serializers.IntegerField()
