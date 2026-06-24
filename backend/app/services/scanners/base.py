from abc import ABC
from abc import abstractmethod


class BaseScanner(ABC):

    @abstractmethod
    def scan(self, target):
        pass