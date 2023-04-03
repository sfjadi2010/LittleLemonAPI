from decimal import Decimal
from . import models
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Category
        fields = ['id', 'slug', 'title']

class MenuItemSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length=255)
    # price = serializers.DecimalField(max_digits=5, decimal_places=2)
    # inventory = serializers.IntegerField()

    stock = serializers.IntegerField(source='inventory')
    price_after_tax = serializers.SerializerMethodField(method_name = 'get_price_after_tax')
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    # category = serializers.HyperlinkedRelatedField(        
    #     queryset = models.Category.objects.all(),
    #     view_name='category_detail'        
    # )
    class Meta:        
        model = models.MenuItem
        fields = ['id', 'title', 'price', 'stock', 'price_after_tax', 'category', 'category_id']
        # depth = 1

    def get_price_after_tax(self, product:models.MenuItem):
        return product.price * Decimal(1.13)
    