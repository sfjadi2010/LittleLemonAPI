from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import serializers
from rest_framework import status


from . import models

# Create your views here.
@api_view(['GET', 'POST'])
def menu_items(request):    
    if request.method == 'GET':
      items = models.MenuItem.objects.select_related('category').all()
      serialized_items = serializers.MenuItemSerializer(items, many=True, context={'request': request})
      return Response(serialized_items.data)
    
    if request.method == 'POST':
      serialized_item = serializers.MenuItemSerializer(data=request.data)
      serialized_item.is_valid(raise_exception=True)
      serialized_item.save()
      return Response(serialized_item.data, status.HTTP_201_CREATED)

@api_view(['GET'])
def single_item(request, pk):
    item = get_object_or_404(models.MenuItem, id=pk)
    serialized_item = serializers.MenuItemSerializer(item)
    return Response(serialized_item.data, many=False, context={'request': request})

@api_view(['GET'])
def category_detail(request, pk):
    category = get_object_or_404(models.Category, id=pk)
    serialized_category = serializers.CategorySerializer(category)
    return Response(serialized_category.data)