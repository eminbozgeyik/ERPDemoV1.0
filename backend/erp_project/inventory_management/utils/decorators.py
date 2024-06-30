from functools import wraps
import logging
from rest_framework.exceptions import NotFound
from inventory_management.services.services import (
    LoggingService, PerformanceMonitoringService, CachingService
)

async def validate_category_existence(func):
    @wraps(func)
    async def wrapper(self, id, *args, **kwargs):
        category = await self.category_service.get_by_id(id)
        if not category:
            raise NotFound("Category not found")
        return await func(self, id, *args, **kwargs)
    return wrapper

async def validate_item_existence(func):
    @wraps(func)
    async def wrapper(self, id, *args, **kwargs):
        item = await self.item_service.get_by_id(id)
        if not item:
            raise NotFound("Item not found")
        return await func(self, id, *args, **kwargs)
    return wrapper

async def log_action(func):
    @wraps(func)
    async def wrapper(self, *args, **kwargs):
        message = f"Calling {func.__name__}"
        await LoggingService.log(self, message)
        return await func(self, *args, **kwargs)
    return wrapper

async def monitor_performance(func):
    @wraps(func)
    async def wrapper(self, *args, **kwargs):
        message = f"Calling {func.__name__}"
        await PerformanceMonitoringService.monitor(self, message)
        return await func(self, *args, **kwargs)
    return wrapper

async def cache_result(func):
    @wraps(func)
    async def wrapper(self, *args, **kwargs):
        # Implement caching logic here
        key = f"{func.__name__}-{args}-{kwargs}"
        if key in CachingService.cache:
            return CachingService.cache[key]
        result = await func(self, *args, **kwargs)
        CachingService.cache[key] = result
        return result
    return wrapper

def handle_errors(func):
    wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except Exception as e:
            logging.error(f"Error in {func.__name__}: {e}")
            # Handle the error as needed, e.g., return a specific value or re-raise
            raise
    return wrapper
