from scapy.all import *

import sys
import random

ip_dst = "11.0.0.5"
ip_src = "11.0.0.4"
mac_dst = "0a:3d:fd:0f:fc:e8"
mac_src = "42:19:8e:09:9a:0c"

data = "This is a test" 
knock_ports = [10002]

for i in knock_ports:
    p = (Ether(dst=mac_dst, src=mac_src, type="IPv4")/
        IP(src=ip_src, dst=ip_dst, version=4, ihl=5, tos=0xb8, len=76, id=19593, flags="DF", frag=0, ttl=64, proto="tcp")/
        TCP(sport=1022, dport=i))
    sendp(p, iface=sys.argv[1])
