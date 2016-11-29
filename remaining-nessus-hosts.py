#!/usr/bin/env python3

import os,sys
import argparse
import ipaddress

parser = argparse.ArgumentParser(description='Nessus Target Remain Generator')

parser.add_argument('-i',dest='input_file',help='Specify the file with the IP Address list (one per line)')
parser.add_argument('-r',dest='range',help='Specify the range that was being scanned: e.g. 10.3.4.0/23')
args = parser.parse_args()

scanned_array = []
for ip in open(args.input_file):
    scanned_array.append(ip.rstrip())

output_array = []
range = ipaddress.ip_network(args.range)

for x in range.hosts():
    ip_x = str(x).rstrip()

    for z in scanned_array:
        ip_z = str(z).rstrip()

        if ip_x == ip_z:
            skip = True
            break
        else:
            skip = False

    if skip is False:
        output_array.append(x)

for out in output_array:
    print (out)
