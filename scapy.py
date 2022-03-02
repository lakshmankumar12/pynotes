'''
Good docs of scapy:

#on sr functions
https://thepacketgeek.com/scapy-p-06-sending-and-receiving-with-scapy/



'''
import scapy.all
from scapy.all import *
from scapy.layers.inet import *
#from scapy.layers.inet import IP, ICMP, Ether

#capture
#  use the count arg to return immdly after n pkts
sniff(iface="nap301",filter="udp",prn=lambda x:x.summary(),count=10)

#convert pkt to str
str(pkt)

#convert pkt to bytes to send if you need to write() it.
raw(pkt)

#list of fields values to stdout. Returns None
ls(pkt)

#better view of pkt
pkt.show()

#print hexdump on stdout. Returns None
hexdump(pkt)

pkt.summary()
pkt.show()

# getting individual fields in a pkt
pkt[IP]
pkt[IP].src
pkt[IP].dst
pkt[IP][UDP]
pkt[IP][UDP].sport
pkt[IP][UDP].payload

# removing a layer
#  Remove/Strip ether layer off.
ippkt = etherpkt[IP]

## To explore availalbe fields , use the pkt.show() api.

## Check if pkt has a layer
pkt.haslayer(IP)

#ping
dip="10.10.1.1"
a=IP(dst=dip)/ICMP(id=RandShort(),seq=RandShort())/Raw("Random String")
reply=sr1(a)

#get o/p of tcpdump -xX
IP(import_hexcap())
0x0000:  4500 0034 8ecc 4000 4006 cfb8 0a1e 6402  E..4..@.@.....d.
0x0010:  0a1e 6401 0516 e811 afc4 2bb6 ba8d 2c21  ..d.......+...,!
0x0020:  8010 0041 143f 0000 0101 080a 2a32 2ab5  ...A.?......*2*.
0x0030:  1add 66e8                                ..f.
^D

#ping
dip="10.10.1.1"
a=IP(dst=dip)/ICMP(id=RandShort(),seq=RandShort())/Raw("Random String")
reply=sr1(a)


#import a pcap file
a=rdpcap("/path/to/file.cap")

#Not scapy but general ip functions
def carry_around_add(a, b):
    c = a + b
    return (c & 0xffff) + (c >> 16)

def checksum(msg):
    s = 0
    for i in range(0, len(msg), 2):
        w = ord(msg[i]) + (ord(msg[i+1]) << 8)
        s = carry_around_add(s, w)
    return ~s & 0xffff




#raw socket bind
from socket import socket, AF_PACKET, SOCK_RAW
#from scapy.all import *
s = socket(AF_PACKET, SOCK_RAW)
s.bind(("greto312", 0))

a='whatever'
s.send(a)

