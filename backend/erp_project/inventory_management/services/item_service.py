from inventory_management.models import Item
from core.utils.base_services import BaseService
from inventory_management.utils.decorators import handle_errors

class ItemService(BaseService):
    @handle_errors
    async def get_all(self):
        return Item.objects.all()
    
    @handle_errors
    async def get_by_id(self, id):
        return Item.objects.get(pk=id)

    @handle_errors
    async def create(self, data):
        return Item.objects.create(**data)

    @handle_errors
    async def update(self, id, data):
        item = await Item.objects.get(pk=id)
        for key, value in data.items():
            setattr(item, key, value)
        await item.save()
        return item

    @handle_errors
    async def delete(self, id):
        item = await Item.objects.get(pk=id)
        await item.delete()
