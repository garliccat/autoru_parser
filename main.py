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

        try:
            brand = card.find('a', {'class':'Link ListingItemTitle-module__link'})['href'].split('/')[-4]
        except:
            brand = ''
        print(u'Brand: {}'.format(brand.encode('iso-8859-1').decode('utf-8', 'ignore')))

        try:
            model = card.find('a', {'class':'Link ListingItemTitle-module__link'})['href'].split('/')[-3]
        except:
            model = ''
        print(u'Model: {}'.format(model.encode('iso-8859-1').decode('utf-8', 'ignore')))

        try:
            drive = card.find_all('div', {'class': 'ListingItemTechSummaryDesktop__cell'})[3].get_text(strip=True)
        except:
            drive = ''
        print(u'Drive: {}'.format(drive.encode('iso-8859-1').decode('utf-8', 'ignore')))

        try:
            color = card.find_all('div', {'class': 'ListingItemTechSummaryDesktop__cell'})[4].get_text(strip=True)
        except:
            color = ''
        print(u'Color: {}'.format(color.encode('iso-8859-1').decode('utf-8', 'ignore')))

        try:
            price = card.find('div', {'class': 'ListingItemPrice-module__content'}).get_text(strip=True)
        except:
            price = ''
        print(u'Price: {}'.format(price.encode('iso-8859-1').decode('utf-8', 'ignore')))

        try:
            year = card.find('div', {'class': 'ListingItem-module__year'}).get_text(strip=True)
        except:
            year = ''
        print(u'Year: {}'.format(year.encode('iso-8859-1').decode('utf-8', 'ignore')))

        try:
            mileage = card.find('div', {'class': 'ListingItem-module__kmAge'}).get_text(strip=True)
        except:
            mileage = ''
        print(u'Mileage: {}'.format(mileage.encode('iso-8859-1').decode('utf-8', 'ignore')))


        print('\n')



def main():
    for i in range(100, 110):
        url = 'https://auto.ru/moskva/cars/used/?page={}'.format(i)
        get_data(get_html(url))
    

main()