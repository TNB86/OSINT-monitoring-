import OSINT_modules.Report_maker


def main():
    domain = input('Enter scanning domain like test.test: ')
    OSINT_modules.Report_maker.make_report(domain)
    print('Report successfully created!')


if __name__ == '__main__':
    main()
