from abc import ABCMeta, abstractmethod


class Arpscan :

    __metaclass__ = ABCMeta

    def __init__(self):
        self._interface = None
        self._subnets = None


    """
    method that is used to get the interface
    """
    @abstractmethod
    def interface(self): pass

    """
    abstract method that is used to get the subnet
    """
    @abstractmethod
    def subnet(self): pass

    """
    abstract method that is used to make an ARP scan of the subnet
    """
    @abstractmethod
    def scan(self): pass