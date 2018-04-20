import sys
import os
import requests
import whois
from datetime import datetime


def load_urls4check(path):
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as text_file:
            return text_file.read().strip().split('\n')


def is_server_respond_with_200(url):
    try:
        response = requests.get(url)
    except requests.exceptions.ConnectionError:
        return False
    return response.ok


def get_domain_expiration_date(domain_name):
    try:
        whois_info = whois.whois(domain_name)
    except whois.parser.PywhoisError as e:
        return None
    if type(whois_info.expiration_date) == list:
        whois_info.expiration_date = whois_info.expiration_date[0]
    return whois_info.expiration_date


def get_days_till_expiration(domain_expiration_date):
    days_till_expiration = (
        domain_expiration_date - datetime.now()
    ).days
    return days_till_expiration


def print_domain_expiration_info(days_till_expiration):
    min_days_till_expiration = 30
    days_if_expired = 0
    if days_till_expiration > min_days_till_expiration:
        print('Domain expires in more than 30 days')
    elif days_till_expiration < days_if_expired:
        print('Domain is already expired')
    else:
        print('Domain expires in %s days' % (days_till_expiration))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('No path specified')
    filepath = sys.argv[1]
    urls = load_urls4check(filepath)
    if urls is None:
        sys.exit('Wrong file')

    for url in urls:
        print('You are checking: %s' % url)

        if is_server_respond_with_200(url):
            print('Server is up')
        else:
            print('Server is down')

        domain_expiration_date = get_domain_expiration_date(url)
        if not domain_expiration_date:
            print('Domain name not found')
            continue

        days_till_expiration = get_days_till_expiration(domain_expiration_date)
        print_domain_expiration_info(days_till_expiration)
