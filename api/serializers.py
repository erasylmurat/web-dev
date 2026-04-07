from rest_framework import serializers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    discounted_price = serializers.SerializerMethodField()

    def get_discounted_price(self, obj):
        return round(obj.price * 0.9, 2)

    class Meta:
        model = Product
        fields = '__all__'
        fields = ['id', 'name', 'price', 'discounted_price', 'description', 'count', 'is_active', 'category']