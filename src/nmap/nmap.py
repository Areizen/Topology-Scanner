from libnmap.process import NmapProcess

class Nmap:

    def __init__(self,ip_list):
        self.ips = ip_list


    def scan(self):
        nm = NmapProcess(self.ips, options="-sV -T5")
        rc = nm.run()

        if rc == 0:
            f = open("out.xml","w")
            f.write(nm.stdout)
            f.close()
        else:
            print(nm.stderr)

