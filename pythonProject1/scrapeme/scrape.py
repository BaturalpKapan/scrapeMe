from bs4 import BeautifulSoup
import pandas as pd
import requests


class Product:
    name: str
    price: int
    url: str

    def create_objects(self):
        website = 'https://scrapeme.live/shop'
        result = requests.get(website, verify=False)
        content = result.text

        soup = BeautifulSoup(content, 'lxml')

        pagination = soup.find_all('ul', class_='page-numbers')
        for pages in pagination:
            pages_l = pages.find_all('a', class_='page-numbers')

        # https://scrapeme.live/shop/page/2/

        root = "https://scrapeme.live/shop/"
        links = []
        prices = []
        names = []
        for i in range(1, 49):
            website = f'{root}/page/' + str(i)
            result = requests.get(website, verify=False)

            content = result.text
            soup = BeautifulSoup(content, 'lxml')

            box = soup.find('main', class_='site-main')

            for link in box.findAll('a', class_='woocommerce-LoopProduct-link woocommerce-loop-product__link',
                                    href=True):
                links.append(link['href'])

            for price in box.findAll('span', class_='price'):
                prices.append(price.text)

            for name in box.findAll('h2', class_='woocommerce-loop-product__title'):
                names.append(name.text)
        dict_print = {'prices': prices, 'links': links, 'names': names, 'page-numbers': i}
        df = pd.DataFrame.from_dict(dict_print)
        df.to_csv('scrapeme.csv')


product = Product()
product.create_objects()
