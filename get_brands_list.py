# parser for getting URLS from AUTO.RU for each producer

import requests
from bs4 import BeautifulSoup as bs
import random


def get_html(url):
    user_agent_list = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 YaBrowser/20.9.3.136 Yowser/2.5 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
    ]

    try:
        r = requests.get(url, headers={'User-Agent': random.choice(user_agent_list)}, timeout=10)
    except:
        print('unable to reach page: {}'.format(url))
        return None

    return r.text


def get_data(html):
    if html == None:
        print('Page: {} access denied'.format(html))
        return None

    soup = bs(html, 'lxml')
    cards = soup.find_all('div', {'class':'ListingPopularMMM-module__item'})
    brand_urls = []
    for card in cards:
        u = card.find('a')['href']
        brand_urls.append(u)
        print(u)
    print(len(cards))
    return brand_urls


def main():
    # url = 'https://auto.ru/moskva/cars/used/'
    with open('web.html', encoding='UTF-8') as f:
        f = f.read()
    o = open('urls.txt', 'a')
    o.write('\n'.join(get_data(f)))
    o.close()

    
if __name__ == '__main__':
    main()
