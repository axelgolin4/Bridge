import abc
from abc import abstractmethod


class Device(metaclass=abc.ABCMeta):
    @abstractmethod
    def is_enabled(self):
        raise NotImplementedError

    def enabled(self):
        raise NotImplementedError

    def disable(self):
        raise NotImplementedError

    def get_volumen(self):
        raise NotImplementedError

    def set_volumen(self):
        raise NotImplementedError

    def get_channel(self):
        raise NotImplementedError

    def set_channel(self, chal):
        raise NotImplementedError
    
    def set_Netflix(self):
        raise NotImplemented

    def set_Amazon(self):
        raise NotImplemented

    def set_Youtube(self):
        raise NotImplemented