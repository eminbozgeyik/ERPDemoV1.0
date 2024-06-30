from core.utils.base_services import BaseLoggingService, BasePerformanceMonitoringService, BaseCachingService
import logging
import time

class LoggingService(BaseLoggingService):
    async def log(self, message):
        logging.info(message)

class PerformanceMonitoringService(BasePerformanceMonitoringService):
    async def monitor(self, operation):
        start_time = time.time()
        # Your operation logic here
        end_time = time.time()
        duration = end_time - start_time
        logging.info(f"Operation '{operation}' took {duration} seconds")

class CachingService(BaseCachingService):
    def __init__(self):
        self.cache = {}

    def set_cache(self, key, value):
        self.cache[key] = value

    def get_from_cache(self, key):
        return self.cache.get(key, None)
