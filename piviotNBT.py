import argparse
from termcolor import colored
from nmb.NetBIOS import NetBIOS
from netaddr import IPNetwork
import sys

parser = argparse.ArgumentParser()
parser.add_argument("NetRange", help="Local Netwrok Range to Scan")
args = parser.parse_args()


def queryNam(name):
    n = NetBIOS(broadcast=True, listen_port=0)
    ip = n.queryName(name, timeout=0.3)
    return ip

def queryIPForName(address):
    n = NetBIOS(broadcast=True, listen_port=0)
    hostname = n.queryIPForName(address, timeout=0.2)
    return hostname

print colored("Scanning....%s Please Wait\n", "green") % args.NetRange 


for cider in IPNetwork(args.NetRange):

	hostname = queryIPForName('%s' % cider)

	if hostname != None:
		
		str2 = hostname[0]

		ip = queryNam(str2)

		if ip != None:
			print colored("Number of Piviot Points: %s ", "yellow") % len(ip)
#			print hostname[:5]
			print colored("Multi-Honed Host Detected: %s", "red") % str2
			print colored("Associated IP's: %s", "green") % ip
			print "============================================="
