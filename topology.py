import sys
from src.arp.scapyarpscan import ScapyArpscan
from src.nmap.nmap import Nmap


if len(sys.argv)<3:
    print("Usage : python topology.py <interface> <subnets>")
    exit(1)

interface = sys.argv[1]
subnets = sys.argv[2]

arpscan = ScapyArpscan(interface=interface,subnets=subnets)

nmap = Nmap(arpscan.ips)
nmap.scan()
