# Topology-Scanner
A topology scanner using Nmap with Arp for python3

## Requirements
```
sudo apt-get install -y python3-pip
sudo pip3 -r requirements.txt
```

## Usage :
```
python topology.py <interface> <subnets>
    
Exemple: 
    python topology.py eth0 192.168.1.0/24
    python topology.py eth0,wlan0 192.168.1.0/24,10.0.10.0/24 
```