import sys
import os
import requests
import whois
from datetime import datetime


def load_urls4check(path):
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as text_file:
            return text_file.read().splitlines()


def is_server_respond_ok(url):
    try:
        response = requests.get(url)
    except requests.exceptions.ConnectionError:
        return False
    return response.ok


def get_domain_expiration_date(domain_name):
    try:
        whois_info = whois.whois(domain_name)
        if type(whois_info.expiration_date) == list:
            whois_info.expiration_date = whois_info.expiration_date[0]
        return whois_info.expiration_date
    except whois.parser.PywhoisError:
        return None


def is_domain_paid(domain_expiration_date):
    if domain_expiration_date:
        min_days_till_expiration = 30
        days_till_expiration = (
            domain_expiration_date - datetime.now()
        ).days
        if days_till_expiration > min_days_till_expiration:
            return True


def print_domain_info(expiration_is_soon, server_is_ok):
    server_status = 'up' if server_is_ok else 'down'
    print('Server is {}'.format(server_status))
    domain_status = 'paid' if domain_is_paid else 'not paid'
    print('Domain is {} for the next month'.format(domain_status))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('No path specified')
    filepath = sys.argv[1]
    urls = load_urls4check(filepath)
    if urls is None:
        sys.exit('Wrong file')
    for url in urls:
        print('You are checking: {}'.format(url))
        domain_expiration_date = get_domain_expiration_date(url)
        domain_is_paid = is_domain_paid(domain_expiration_date)
        server_is_ok = is_server_respond_ok(url)
        print_domain_info(domain_is_paid, server_is_ok)
