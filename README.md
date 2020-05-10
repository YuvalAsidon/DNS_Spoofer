# DNS_Spoofer

## Install netfilterqueue
* sudo apt install python3-pip git libnfnetlink-dev libnetfilter-queue-dev
* pip3 install -U git+https://github.com/kti/python-netfilterqueue

## Runing the program
* need to use the [arp_spoofing](https://github.com/YuvalAsidon/ARP_Spoofing)
* run everything there and then:
  * sudo iptables -I FORWARD -j NFQUEUE --queue-num 0
  * python net_cut.py
