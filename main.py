import os
import requests
from colors import Imprimir
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

IDZONE = os.getenv('IDZONE')
KEY = os.getenv('APIKEY')
EMAIL = os.getenv('EMAIL')
TTL = os.getenv('TTL')
PROXIED = os.getenv('PROXIED')
URL = 'https://api.cloudflare.com/client/v4'

headers = {
    'Authorization': 'Bearer ' + KEY,
    'Content-Type': 'application/json',
}

Imprimir.printInfo(f'{(datetime.today()).strftime("%d-%m-%Y %H:%M:%S")} - Obtendo endereco IP')
IP = requests.get('https://checkip.amazonaws.com').text
IP = IP.replace('\n', '')
Imprimir.printSuccess(f'{(datetime.today()).strftime("%d-%m-%Y %H:%M:%S")} - Meu IP: {IP}')


def getDNSRecords():
    baseURL = URL + '/zones/' + IDZONE + '/dns_records?type=A'
    response = requests.get(baseURL, headers=headers)
    parse = response.json()['result'] if response.ok else []
    return parse


def updateDNSRecord(id, nome, ip):
    baseURL = URL + '/zones/' + IDZONE + '/dns_records/' + id
    params = {
        'type': 'A',
        'ttl': TTL,
        'proxied': True if PROXIED == 'True' else False,
        'name': nome,
        'content': f'{ip}',
    }
    response = requests.put(baseURL, headers=headers, json=params)
    parse = response.json()['result'] if response.ok else []
    return parse


Imprimir.printInfo(f'{(datetime.today()).strftime("%d-%m-%Y %H:%M:%S")} - Conectando a Cloudflare')
zonas = getDNSRecords()
Imprimir.printSuccess(f'{(datetime.today()).strftime("%d-%m-%Y %H:%M:%S")} - Registros DNS: {len(zonas)}')

for zona in zonas:
    Imprimir.printDanger(f'{(datetime.today()).strftime("%d-%m-%Y %H:%M:%S")} - Anterior {zona["name"]} <- {zona["content"]}')
    Imprimir.printSuccess(f'{(datetime.today()).strftime("%d-%m-%Y %H:%M:%S")} - Novo {zona["name"]} -> {IP}')
    if IP != zona['content']:
        updateDNSRecord(zona['id'], zona['name'], IP)
        Imprimir.printInfo(f'{(datetime.today()).strftime("%d-%m-%Y %H:%M:%S")} - Atualizado {zona["name"]} -> {IP}')
    else:
        Imprimir.printInfo(f'{(datetime.today()).strftime("%d-%m-%Y %H:%M:%S")} - não é necessario realizar update')