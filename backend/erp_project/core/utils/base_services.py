from abc import ABC, abstractmethod

class BaseService(ABC):
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, id):
        pass

    @abstractmethod
    def create(self, data):
        pass

    @abstractmethod
    def update(self, id, data):
        pass

    @abstractmethod
    def delete(self, id):
        pass


class BaseLoggingService(ABC):
    @abstractmethod
    def log(self, message):
        pass


class BasePerformanceMonitoringService(ABC):
    @abstractmethod
    def monitor(self, operation):
        pass


class BaseCachingService(ABC):
    @abstractmethod
    def set_cache(self, key, value):
        pass

    @abstractmethod
    def get_from_cache(self, key):
        pass
    