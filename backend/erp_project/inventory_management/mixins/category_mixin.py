from inventory_management.services.category_service import CategoryService
from inventory_management.utils.decorators import (
    monitor_performance, log_action,
    validate_category_existence
)
from inventory_management.services.services import (
    LoggingService, PerformanceMonitoringService, CachingService
)

# Initialize shared services
logging_service = LoggingService()
performance_monitoring_service = PerformanceMonitoringService()
caching_service = CachingService()

class CategoryMixin:
    def __init__(self):
        self.category_service = CategoryService()

    @validate_category_existence
    @log_action
    @monitor_performance
    async def get_category(self, category_id, *args, **kwargs):
        return await self.category_service.get_by_id(category_id)

    @log_action
    @monitor_performance
    async def get_all_categories(self):
        return await self.category_service.get_all()

    @log_action
    @monitor_performance
    async def add_category(self, data, *args, **kwargs):
        return await self.category_service.create(data)

    @log_action
    @monitor_performance
    async def delete_category(self, category_id, *args, **kwargs):
        return await self.category_service.delete(category_id)

    @log_action
    @monitor_performance
    async def update_category(self, category_id, data, *args, **kwargs):
        return await self.category_service.update(category_id, data)