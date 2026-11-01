#Construct an Ethernet frame with the specified destination/source MAC,
#  IPv4 source/destination,
#  UDP source port 53000/destination port 53,
#  and DNS query www.example.com.

from scapy.all import *

pkt = (
    Ether(dst='ff:ff:ff:ff:ff:ff',
          src='00:00:00:00:00:00') /
    IP(src='10.0.1.1',dst='10.0.1.2') /
    UDP(sport=53000, dport=53) /
    DNS(rd=1, qd=DNSQR(qname='www.example.com'))
)

pkt.show()