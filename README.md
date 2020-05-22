

# DNS_Spoofer
DNS spoofer allow you to be the man-in-the-middle, choose on which pc you want to try it on and what website you want to spoof

## Install netfilterqueue
* sudo apt install python3-pip git libnfnetlink-dev libnetfilter-queue-dev
* pip3 install -U git+https://github.com/kti/python-netfilterqueue

## Running the program
* need to downlad the [arp_spoofing](https://github.com/YuvalAsidon/ARP_Spoofing)
  * download file and place it in the same place as this file
* sudo apt-get install xterm
* change in both files the IP's of everything and change the website that you want to try it on
* sudo python DNS_Spoofer.py
  * and then choose if you want it to be on your own pc or on another
* In order to terminate the program, CTRL+C in both terminals that gets open
