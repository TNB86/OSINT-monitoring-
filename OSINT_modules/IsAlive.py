import json
import socket

import OSINT_modules.Subdomain_scaner


def get_json():
    with open(f'../logs/info.json', 'r', encoding='utf-8') as file:
        json_res = json.load(file)
        res = Subdomain_scaner.parse_collection(json_res)
        return res


def ping_server(server, port=80, timeout=3):
    domain = server
    is_alive = [domain]
    try:
        socket.setdefaulttimeout((timeout))
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((domain, port))
    except OSError as error:
        is_alive.append(False)
    else:
        is_alive.append(True)
    s.close()
    return is_alive


def ping_server_array(server, port=80, timeout=3):
    is_alive = []
    for item in server:
        domain = item[0]
        try:
            socket.setdefaulttimeout(timeout)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((domain, port))
        except OSError as error:
            is_alive.append([domain, False])
        else:
            is_alive.append([domain, True])
    s.close()
    return is_alive


def main():
    pass


if __name__ == '__main__':
    main()
