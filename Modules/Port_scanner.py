import socket
import sys

import pyfiglet

ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)


# # Defining a target
# if len(sys.argv) == 2:
#
#     # translate hostname to IPv4
#     target = socket.gethostbyname(sys.argv[1])
# else:
#     print("Invalid amount of Argument")
#
# target = '5.1.53.123'
# # Add Banner
# print("-" * 50)
# print("Scanning Target: " + target)
# print("Scanning started at:" + str(datetime.now()))
# print("-" * 50)
#
# try:
#     # will scan ports between 1 to 65,535
#     for port in range(1, 1024):
#         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         socket.setdefaulttimeout(1)
#
#         # returns an error indicator
#         result = s.connect_ex((target, port))
#         if result == 0:
#             print("Port {} is open".format(port))
#         s.close()
#
# except KeyboardInterrupt:
#     print("\n Exiting Program !!!!")
#     sys.exit()
# except socket.gaierror:
#     print("\n Hostname Could Not Be Resolved !!!!")
#     sys.exit()
# except socket.error:
#     print("\ Server not responding !!!!")
#     sys.exit()


def port_scanner(target):
    target = target
    open_ports = []
    print('Target ip: {}'.format(target))
    try:
        # for scanning all open ports put 65536 instead of 1024 in port (mach longer output)
        for port in range(1, 1024):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target, port))
            print(port)
            if result == 0:
                print("Port {} is open".format(port))
                open_ports.append(port)
            s.close()
        return open_ports
    except KeyboardInterrupt:
        print("\n Exiting Program !!!!")
        sys.exit()
    except socket.gaierror:
        print("\n Hostname Could Not Be Resolved !!!!")
        sys.exit()
    except socket.error:
        print("\n Server not responding !!!!")
        sys.exit()


def main(domain_list):
    domain_list = domain_list
    for item in range(domain_list):
        port_scanner(domain_list)


if __name__ == '__main__':
    main()
