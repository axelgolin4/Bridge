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

    def set_channel(self):
        raise NotImplementedError