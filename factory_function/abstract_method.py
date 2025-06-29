import abc
from abc import abstractmethod
class AbstractFactory(metaclass=abc.ABCMeta):
    @abstractmethod
    def create_product(self):
        """Method to create a product"""
        pass