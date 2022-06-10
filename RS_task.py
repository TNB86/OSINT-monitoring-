from Scanners.Port_scanner import port_scanner


def main():
    open = port_scanner('5.1.53.123')
    print(open)


if __name__ == '__main__':
    main()
