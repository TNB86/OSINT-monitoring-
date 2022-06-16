import socket
import sys
import threading

DATA = []


def port_scanner(target):
    target = target
    open_ports = [target, []]
    try:
        # for scanning all open ports put 65536 instead of 1024 in port (mach longer output)
        for port in range(1, 1024):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target, port))
            if result == 0:
                open_ports[1].append(port)
            s.close()
        DATA.append(open_ports)
        return open_ports
    except KeyboardInterrupt:
        print('\n Exiting Program !!!!')
        sys.exit()
    except socket.gaierror:
        print('\n Hostname Could Not Be Resolved !!!!')
        sys.exit()
    except socket.error:
        print('\n Server not responding !!!!')
        sys.exit()


def scan_threading(domain_list):
    domain_list = domain_list
    threads = list()
    for item in domain_list:
        x = threading.Thread(target=port_scanner, args=(item[1],))
        x.start()
        threads.append(x)
    for thread in threads:
        thread.join()
    print(DATA)


def main():
    pass


if __name__ == '__main__':
    main()
