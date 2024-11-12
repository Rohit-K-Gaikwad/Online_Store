from rest_framework import serializers
from .models import Category, Product, Order


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class CreateOrderSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    product_ids = serializers.ListField(child=serializers.IntegerField())

    def validate(self, data):
        product_ids = data['product_ids']
        products = Product.objects.filter(id__in=product_ids)

        if not products.exists():
            raise serializers.ValidationError("Invalid product IDs.")

        for product in products:
            if product.stock < 1:
                raise serializers.ValidationError(f"Product {product.name} is out of stock.")
        return data