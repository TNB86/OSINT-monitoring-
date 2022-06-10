import json
import socket

import domain


def get_json():
    with open(f'info.json', 'r', encoding='utf-8') as file:
        json_res = json.load(file)
        res = domain.parse_collection(json_res)
        return res


def ping_server(server: str, port: int = 80, timeout=3):
    """ping server"""
    is_alive = []
    for i in range(len(server)):
        for j in range(len(server[i])):
            domain = server[i][0]
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


server = get_json()
print(ping_server(server))
