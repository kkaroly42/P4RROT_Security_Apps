from scapy.all import *

import sys
import random

ip_dst = "10.1.1.3"
ip_src = "10.1.1.2"
mac_dst = "00:11:22:33:44:55"
mac_src = "00:aa:bb:cc:dd:ee"

for i in range(100):
    decision = random.randint(0,100)
    if(decision > 50):
        p = (Ether(dst=mac_dst, src=mac_src, type="IPv4")/
            IP(src=ip_src, dst=ip_dst, version=4, ihl=5, tos=0xb8, len=76, id=19593, flags="DF", frag=0, ttl=64, proto="udp")/
            UDP(sport=123, dport=123, len=56)/
            NTP(mode="server", precision=random.randrange(100,300), delay=random.randint(0,5000)/1000000,
            dispersion = random.randint(0,9000)/100000, id=ip_src, ref = Decimal(3681558891 + random.randrange(-3000000000,3000000000)/10),
            recv = Decimal(3681558891 + random.randrange(-3000000000,3000000000)/10), orig=Decimal(0.0), sent = Decimal(3681558891 + random.randrange(-3000000000,3000000000)/10)))
    else:
        p = (Ether(dst=mac_dst, src=mac_src, type="IPv4")/
            IP(src=ip_src, dst=ip_dst, version=4, ihl=5, tos=0xb8, len=76, id=19593, flags="DF", frag=0, ttl=64, proto="udp")/
            UDP(sport=123, dport=123, len=56)/
            NTP(mode="server", precision=random.randrange(100,300), delay=random.randint(0,5000)/1000000,
            dispersion = random.randint(0,9000)/100000, id=ip_src, ref = Decimal(3681558891 + random.randrange(-3000000000,3000000000)/10),
            recv = Decimal(3681558891 + random.randrange(-3000000000,3000000000)/10), orig=Decimal(3681558891 + random.randrange(-3000000000,3000000000)/10), sent = Decimal(3681558891 + random.randrange(-3000000000,3000000000)/10)))
    sendp(p, iface="veth3")