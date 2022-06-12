import csv
import threading

from OSINT_modules.IsAlive import ping_server
from OSINT_modules.Port_scanner import port_scanner
from OSINT_modules.Subdomain_scaner import parse_collection, collect_data, DATE

LOCK = threading.RLock()
HEADER = ['Domain', 'IsAlive', 'IP', 'Ports', 'Technologies', 'Comments', 'Sources']


def structure(domain, alive, ip, ports, techs='', comments='', sources=''):
    struct = dict()
    struct['Domain'] = domain
    struct['IsAlive'] = alive
    struct['IP'] = ip
    struct['Ports'] = ports
    struct['Technologies'] = techs
    struct['Comments'] = comments
    struct['Sources'] = sources
    return struct


def make_single_record(item, writer):
    domain = item[0]
    ip = item[1]
    alive = ping_server(domain)[1]
    ports = port_scanner(ip)[1]
    open_ports = ''
    for port in ports:
        open_ports += f'{port}, '
    row = structure(domain, alive, ip, ports)
    with LOCK:
        writer.writerow(row)


def make_report(domain):
    data = parse_collection(collect_data(domain))
    with open(f'Reports/{domain}-{DATE}.csv', mode='w', encoding='utf-8') as w_file:
        writer = csv.DictWriter(w_file, fieldnames=HEADER, delimiter=';', lineterminator='\r')
        writer.writeheader()
    threads = list()
    with open(f'Reports/{domain}-{DATE}.csv', mode='a', encoding='utf-8') as w_file:
        writer = csv.DictWriter(w_file, fieldnames=HEADER, delimiter=';', lineterminator='\r')
        for item in data:
            x = threading.Thread(target=make_single_record, args=(item, writer,))
            x.start()
            threads.append(x)
        for thread in threads:
            thread.join()


def main():
    pass


if __name__ == '__main__':
    main()
