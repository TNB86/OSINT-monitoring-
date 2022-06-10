import sys
import csv
from datetime import datetime
from Subdomain_scaner import parse_collection
from Port_scanner import port_scanner


HEADER = ['Domain', 'IsAlive', 'IP', 'Ports', 'Technologies', 'Comments', 'Sources']

def structure(domain, alive, ip, ports, techs, comments, sources):
    struct = dict()
    struct['Domain'] = domain
    struct['IsAlive'] = alive
    struct['IP'] = ip
    struct['Ports'] = ports
    struct['Technologies'] =techs
    struct['Comments'] = comments
    struct['Sources'] = sources
    return struct

def make_report():
    pass
