from rest_framework import serializers
from .models import Product, Material, ProductMaterial, Warehouse


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'key']


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ['id', 'name']


class ProductMaterialSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    material = MaterialSerializer(read_only=True, many=True)

    class Meta:
        model = ProductMaterial
        fields = ['id', 'product', 'material', 'quantity']


class WarehouseSerializer(serializers.ModelSerializer):
    material = MaterialSerializer(read_only=True, many=True)

    class Meta:
        model = Warehouse
        fields = ['id', 'material', 'remainder', 'price']


class ProductQuantitySerializer(serializers.Serializer):
    name = serializers.CharField()
    quantity = serializers.IntegerField()
