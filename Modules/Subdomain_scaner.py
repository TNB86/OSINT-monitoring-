import json

import requests
from datetime import datetime
HEADERS = {
    # API-ключ от аккаунта Евнгения
    # email - paholap485@musezoo.com
    # password - Password_123
    'x-apikey': 'ab5e3e594eaece7f56782e83a27eef8ac11243306d0086e9377fec2fdc2545d0'
}

# URL для поиска поддоменов и их ip
URL = 'https://www.virustotal.com/api/v3/domains/'


def collect_data(domain):
    response = requests.get(URL + domain + '/subdomains?limit=40', headers=HEADERS)
    t_date = datetime.now().strftime('%d_%m_%Y')
    with open(f'../logs/{domain}-{t_date}.json', 'w') as file:
        json.dump(response.json(), file, indent=4, ensure_ascii=False)
    return response


def parse_collection(response):
    data = response['data']
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
    collect_data('utmn.ru')
    with open(f'../logs/info.json', 'r', encoding='utf-8') as file:
        json_res = json.load(file)
        print(parse_collection(json_res))
        print(parse_collection(json_res)[0])


if __name__ == '__main__':
    main()
