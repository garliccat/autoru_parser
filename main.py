# parser for AUTO.RU

import requests
from bs4 import BeautifulSoup as bs
import string
import datetime
import csv
import random
import time


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
        print('unable to reach page')
        return None

    return r.text


def write_csv(data):
    with open('autoru.csv', 'a', newline='', encoding='UTF-8') as f:
        #newline - to avoid blank rows after each record
        #encoding utf-16 - we are in russia, thats all`
        writer = csv.writer(f, delimiter=';')
        writer.writerow(data)


def get_data(html):
    global rec_num, today
    if html == None:
        print('Page: {} access denied'.format(html))
        return None

    soup = bs(html, 'lxml')
    try:
        cards = soup.find_all('div', {'class':'ListingItem-module__main'})
    except:
        return None
    
    # fetching datapoints from cards
    for card in cards:
        print('Nr: {}'.format(rec_num))

        title = card.find('a', {'class':'Link ListingItemTitle-module__link'}).get_text(strip=True)
        title = title.encode('iso-8859-1').decode('utf-8', 'ignore')
        print(u'Title: {}'.format(title))

        try:
            engine = card.find_all('div', {'class': 'ListingItemTechSummaryDesktop__cell'})[0].get_text(strip=True)
            engine = engine.encode('iso-8859-1').decode('utf-8', 'ignore')
        except:
            engine = ''
        print(u'Engine: {}'.format(engine))

        try:
            gear = card.find_all('div', {'class': 'ListingItemTechSummaryDesktop__cell'})[1].get_text(strip=True)
            gear = gear.encode('iso-8859-1').decode('utf-8', 'ignore')
        except:
            gear = ''
        print(u'Gear: {}'.format(gear))

        try:
            body = card.find_all('div', {'class': 'ListingItemTechSummaryDesktop__cell'})[2].get_text(strip=True)
            body = body.encode('iso-8859-1').decode('utf-8', 'ignore')
        except:
            body = ''
        print(u'Body: {}'.format(body))

        try:
            brand = card.find('a', {'class':'Link ListingItemTitle-module__link'})['href'].split('/')[-4]
            brand = brand.encode('iso-8859-1').decode('utf-8', 'ignore')
        except:
            brand = ''
        print(u'Brand: {}'.format(brand))

        try:
            model = card.find('a', {'class':'Link ListingItemTitle-module__link'})['href'].split('/')[-3]
            model = model.encode('iso-8859-1').decode('utf-8', 'ignore')
        except:
            model = ''
        print(u'Model: {}'.format(model))

        try:
            drive = card.find_all('div', {'class': 'ListingItemTechSummaryDesktop__cell'})[3].get_text(strip=True)
            drive = drive.encode('iso-8859-1').decode('utf-8', 'ignore')
        except:
            drive = ''
        print(u'Drive: {}'.format(drive))

        try:
            color = card.find_all('div', {'class': 'ListingItemTechSummaryDesktop__cell'})[4].get_text(strip=True)
            color = color.encode('iso-8859-1').decode('utf-8', 'ignore')
        except:
            color = ''
        print(u'Color: {}'.format(color))

        try:
            price = card.find('div', {'class': 'ListingItemPrice-module__content'}).get_text(strip=True)
            price = price.encode('iso-8859-1').decode('utf-8', 'ignore')
        except:
            price = ''
        print(u'Price: {}'.format(price))

        try:
            year = card.find('div', {'class': 'ListingItem-module__year'}).get_text(strip=True)
            year = year.encode('iso-8859-1').decode('utf-8', 'ignore')
        except:
            year = ''
        print(u'Year: {}'.format(year))

        try:
            mileage = card.find('div', {'class': 'ListingItem-module__kmAge'}).get_text(strip=True)
            mileage = mileage.encode('iso-8859-1').decode('utf-8', 'ignore')
        except:
            mileage = ''
        print(u'Mileage: {}'.format(mileage))

        print('Date: {}'.format(today))

        print('\n')

        write_csv([rec_num,
            today,
            title,
            brand,
            model,
            engine,
            gear,
            drive,
            color,
            year,
            mileage,
            price])

        rec_num += 1


def main():
    global today, rec_num
    rec_num = 1
    today = str(datetime.datetime.today().date())

    urls = open('urls.txt', 'r', encoding='UTF-8').read()
    urls = urls.split('\n')
    # print(urls)

    for i in urls:
        soup = bs(get_html(i), 'lxml')
        try:
            page_count = soup.find_all('a', {'class': 'Button Button_color_whiteHoverBlue Button_size_s Button_type_link Button_width_default ListingPagination-module__page'})\
                [-1].find('span', {'class': 'Button__text'}).get_text(strip=True)
            print('Page: {}\npages: {}\n\n'.format(i, page_count))
            for page in range(1, int(page_count.strip()) + 1):
                page_url = i + '&page={}'.format(page)
                get_data(get_html(page_url))
                time.sleep(2)

        except:
            get_data(get_html(i))
            continue


if __name__ == '__main__':
    main()
    