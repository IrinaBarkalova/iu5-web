from abc import ABCMeta, abstractmethod


class GeomShape(metaclass=ABCMeta):
    @abstractmethod
    def square(self):
        pass

    @classmethod
    @abstractmethod
    def name(cls) -> str:
        pass
