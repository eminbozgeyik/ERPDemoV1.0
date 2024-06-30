from inventory_management.services.item_service import ItemService
from inventory_management.utils.decorators import (
    monitor_performance, log_action,
    validate_item_existence
)
from inventory_management.services.services import (
    LoggingService, 
    PerformanceMonitoringService, CachingService
)

# Initialize shared services
logging_service = LoggingService()
performance_monitoring_service = PerformanceMonitoringService()
caching_service = CachingService()

class ItemMixin:
    def __init__(self):
        self.item_service = ItemService()

    @validate_item_existence
    @log_action
    @monitor_performance
    async def get_item(self, item_id, *args, **kwargs):
        return await self.item_service.get_by_id(item_id)

    @log_action
    @monitor_performance
    async def get_all_items(self):
        return await self.item_service.get_all()

    @log_action
    @monitor_performance
    async def add_item(self, data, *args, **kwargs):
        return await self.item_service.create(data)

    @log_action
    @monitor_performance
    async def delete_item(self, item_id, *args, **kwargs):
        return await self.item_service.delete(item_id)

    @log_action
    @monitor_performance
    async def update_item(self, item_id, data, *args, **kwargs):
        return await self.item_service.update(item_id, data)