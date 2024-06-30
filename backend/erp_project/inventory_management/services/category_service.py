from inventory_management.models import Category
from core.utils.base_services import BaseService
from inventory_management.utils.decorators import handle_errors

class CategoryService(BaseService):
    @handle_errors
    async def get_all(self):
        return Category.objects.all()
    
    @handle_errors
    async def get_by_id(self, id):
        return Category.objects.get(pk=id)
    
    @handle_errors
    async def create(self, data):
        return Category.objects.create(**data)
    
    @handle_errors
    async def update(self, id, data):
        category = await Category.objects.get(pk=id)
        for key, value in data.items():
            setattr(category, key, value)
        await category.save()
        return category
    
    @handle_errors
    async def delete(self, id):
        category = await Category.objects.get(pk=id)
        await category.delete()