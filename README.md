# DNS_Spoofer

## Install netfilterqueue
* sudo apt install python3-pip git libnfnetlink-dev libnetfilter-queue-dev
* pip3 install -U git+https://github.com/kti/python-netfilterqueue

## Runing the program
* need to use the [arp_spoofing](https://github.com/YuvalAsidon/ARP_Spoofing)
* sudo apt-get install xterm
* run everything there and then:
  * sudo iptables -I FORWARD -j NFQUEUE --queue-num 0
  * python net_cut.py
  * and after you get out of the program write:
    * sudo iptables --flush
* if you want to try it on you own computer:
  * sudo iptables -I OUTPUT-j NFQUEUE --queue-num 0
  * sudo iptables -I INPUT-j NFQUEUE --queue-num 0
  * python net_cut.py
  * and after you get out of the program write:
    * sudo iptables --flush
