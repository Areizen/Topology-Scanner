from .arpscan import Arpscan

#Comment this bock if you want to see scapy warnings
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

from scapy.all import srp,Ether,ARP,conf

class ScapyArpscan(Arpscan):

    def __init__(self):
        Arpscan()
        self.interface()
        self.subnet()
        self.scan()

    def interface(self):
        print("Interface set")
        self._interface="eth0"

    def subnet(self):
        print("Subnet set")
        self._subnets =["10.0.2.0/24"]

    def scan(self):
        print("Scanning initiated :\n")

        for subnet in self._subnets :

            answers, uans = srp(Ether(dst="FF:FF:FF:FF:FF:FF") / ARP(pdst=subnet), timeout=2, iface=self._interface, inter=0.1)
            answers.summary()


        print("Scan complete")
