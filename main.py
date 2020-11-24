import requests
from bs4 import BeautifulSoup as bs
import string


def get_html(url):
    try:
        r = requests.get(url)
    except:
        print('unable to reach page')
        return None

    return r.text


def get_data(html):
    if html == None:
        return None

    soup = bs(html, 'lxml')
    cards = soup.find_all('div', {'class':'ListingItem-module__main'})
    
    for card in cards:
        title = card.find('a', {'class':'Link ListingItemTitle-module__link'}).get_text(strip=True)
        print(u'Title: {}'.format(title.encode('iso-8859-1').decode('utf-8', 'ignore')))

        try:
            engine = card.find_all('div', {'class': 'ListingItemTechSummaryDesktop__cell'})[0].get_text(strip=True)
        except:
            engine = ''
        print(u'Engine: {}'.format(engine.encode('iso-8859-1').decode('utf-8', 'ignore')))

        try:
            gear = card.find_all('div', {'class': 'ListingItemTechSummaryDesktop__cell'})[1].get_text(strip=True)
        except:
            gear = ''
        print(u'Gear: {}'.format(gear.encode('iso-8859-1').decode('utf-8', 'ignore')))

        try:
            body = card.find_all('div', {'class': 'ListingItemTechSummaryDesktop__cell'})[2].get_text(strip=True)
        except:
            body = ''
        print(u'Body: {}'.format(body.encode('iso-8859-1').decode('utf-8', 'ignore')))



def main():
    url = 'https://auto.ru/moskva/cars/used/?page=500'
    get_data(get_html(url))
    

main()