from rest_framework import generics
from .models import Category, Item
from .serializers import CategorySerializer, ItemSerializer
from inventory_management.mixins.category_mixin import CategoryMixin
from inventory_management.mixins.item_mixin import ItemMixin
from asgiref.sync import sync_to_async

class BaseCategoryView(generics.GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    async def get_queryset(self):
        return await sync_to_async(super().get_queryset)()

    async def get_object(self):
        queryset = self.get_queryset()
        obj = await sync_to_async(queryset.get)(pk=self.kwargs['pk'])
        return obj

class BaseItemView(generics.GenericAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    async def get_queryset(self):
        return await sync_to_async(super().get_queryset)()

    async def get_object(self):
        queryset = self.get_queryset()
        obj = await sync_to_async(queryset.get)(pk=self.kwargs['pk'])
        return obj

class CategoryListView(CategoryMixin, BaseCategoryView, generics.ListCreateAPIView):
    pass

class CategoryDetailView(CategoryMixin, BaseCategoryView, generics.RetrieveUpdateDestroyAPIView):
    pass

class ItemListView(ItemMixin, BaseItemView, generics.ListCreateAPIView):
    pass

class ItemDetailView(ItemMixin, BaseItemView, generics.RetrieveUpdateDestroyAPIView):
    pass
