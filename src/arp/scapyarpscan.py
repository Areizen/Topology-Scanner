from .arpscan import Arpscan

#Comment this bock if you want to see scapy warnings
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

from scapy.all import srp,Ether,ARP,conf

class ScapyArpscan(Arpscan):

    def __init__(self,interface,subnets):
        Arpscan()
        self._interface = interface
        self._subnets = subnets.split(",")
        self.ips = self.scan()

    def interface(self):
        pass

    def subnet(self):
        pass

    def scan(self):
        print("Scanning subnets : \n" + str(self._subnets) + "\n")
        answers, uans = srp(Ether(dst="FF:FF:FF:FF:FF:FF") / ARP(pdst=self._subnets), timeout=2, iface=self._interface)

        ips = []
        for send, received in answers:
            ips.append(received[ARP].psrc)
            print("IP Found : "+received[ARP].psrc)

        return ips
