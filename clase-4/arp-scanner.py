#!/usr/bin python
#-*- coding: utf-8 -*-


# region imports
import logging
logging.getLogger(name="scapy.runtime").setLevel(level=logging.ERROR)
import warnings
from cryptography.utils import CryptographyDeprecationWarning
warnings.filterwarnings("ignore", category=CryptographyDeprecationWarning)
import scapy.all as scapy
from termcolor import colored
from manuf import manuf
import argparse
# endregion


def scan(target: str) -> None:
    # ARP -> L2
    # -> Solicitud ARP
    # -> Broadcast L1
    arp_request: scapy.layers.l2.ARP = scapy.ARP(pdst=target)
    broadcast: scapy.layers.l2.Ether = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_packet: scapy.layers.l2.Ether = broadcast / arp_request
    answered: scapy.plist.SndRcvList
    answered, _ = scapy.srp(arp_packet, timeout=1, verbose=False)
    #answered.summary()
    parser = manuf.MacParser()
    message: str = f"IP\t\t\tMAC Address\t\t\tBrand\n" + colored(f"{'='*65}\n", "yellow")
    for element in answered:
        message += f"{element[1].psrc}\t\t{':'.join(element[1].hwsrc.split(':')[:3])}\t\t{parser.get_manuf(element[1].hwsrc)}\n" #{element[1].hwsrc}\t\t{parser.get_manuf(element[1].hwsrc)}"
    print(message)

def get_arguments() -> str:
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Target to scan", required=True)
    args: argparse.Namespace = parser.parse_args()
    return args.target

def main() -> None:
    target: str = get_arguments()
    scan(target)

if __name__ == "__main__":
    main()
