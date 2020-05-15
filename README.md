# DNS_Spoofer

## Install netfilterqueue
* sudo apt install python3-pip git libnfnetlink-dev libnetfilter-queue-dev
* pip3 install -U git+https://github.com/kti/python-netfilterqueue

## Runing the program
* need to downlad the [arp_spoofing](https://github.com/YuvalAsidon/ARP_Spoofing) file in the same place ad this file
* sudo apt-get install xterm
* change in both files the IP's of everything and change the website that you want to try it on
* sudo python DNS_Spoofer.py
  * and then choose if you want it to be on your own pc or on another
* get out of the program by doing CTRL+C in both terminals that gets open
