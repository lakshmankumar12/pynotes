
#capture
sniff(iface="nap301",filter="udp",prn=lambda x:x.summary())

#convert pkt to str
str(pkt)

#list of fields values to stdout. Returns None
ls(pkt)

#print hexdump on stdout. Returns None
hexdump(pkt)

pkt.summary()
pkt.show()

pkt[IP]
pkt[IP].src
pkt[IP].dst
pkt[IP][UDP]
pkt[IP][UDP].sport
pkt[IP][UDP].payload


#ping
dip="10.10.1.1"
a=IP(dst=dip)/ICMP(id=RandShort(),seq=RandShort())/Raw("Random String")
reply=sr1(a)



