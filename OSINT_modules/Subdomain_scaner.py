import json
from datetime import datetime

import requests

HEADERS = {
    # API-ключ от аккаунта Евнгения
    # email - paholap485@musezoo.com
    # password - Password_123
    'x-apikey': 'ab5e3e594eaece7f56782e83a27eef8ac11243306d0086e9377fec2fdc2545d0'
}

# URL для поиска поддоменов и их ip
URL = 'https://www.virustotal.com/api/v3/domains/'
DATE = datetime.now().strftime('%d_%m_%Y')


def collect_data(domain):
    response = requests.get(URL + f'{domain}/subdomains?limit=40', headers=HEADERS)
    with open(f'logs/{domain}-{DATE}.json', 'w') as file:
        json.dump(response.json(), file, indent=4, ensure_ascii=False)
    return response


def get_json(filename):
    with open(f'../logs/{filename}.json', 'r', encoding='utf-8') as file:
        json_res = json.load(file)
    return json_res


def parse_collection(response):
    if type(response) is dict:
        data = response['data']
    else:
        data = response.json()['data']
    res = []
    for item in data:
        id = item.get('id')  # Домен
        atr = item.get('attributes')  # В атрибуте лежит last_dns_records
        dns = atr.get('last_dns_records')  # В last_dns_records лежит value c ip (ip есть только у type = A)
        for dnss in dns:
            type_name = dnss.get('type')
            if type_name == 'A':
                ip = dnss.get('value')
                res.append([id, ip])
    return res


def main():
    pass


if __name__ == '__main__':
    main()
