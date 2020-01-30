from bs4 import BeautifulSoup
from selenium import webdriver
import re


class Daraz():
    def run():
        browser = webdriver.PhantomJS()
        browser.delete_all_cookies()
        browser.get(
            'https://www.daraz.com.np/catalog/?q=shampoo&_keyori=ss&from=input&spm=a2a0e.11779170.search.go.15bb2d2bkd76XX')
        c = browser.page_source
        soup = BeautifulSoup(c, "html.parser")
        daraz_name_list = []
        daraz_price_list = []
        daraz_link_list = []
        daraz_image_list = []
        daraz_product_name = soup.select("div .c16H9d a")
        daraz_product_price = soup.select("div .c3gUW0 .c13VH6")

        daraz_image = soup.select('script', type="application/ld+json")
        image = str(daraz_image[17])
        # print(image.split())
        pattern = '"image":"https://static-01.daraz.com.np/'
        res = [x for x in image.split() if re.search(pattern, x)]
        for x in res:
            var = (x.split(','))
            var2 = [x for x in var if '"image":' in x]
            var2 = var2[0]
            var3 = var2[9:-1]
            daraz_image_list.append(var3)

        for product in daraz_product_name:
            daraz_name_list.append(product.text)
        for price in daraz_product_price:
            daraz_price_list.append(price.text)

        link = soup.find_all('div', class_='c16H9d')
        for i in link:
            for a in i.find_all('a'):
                href = (a.get('href'))
                daraz_link_list.append(href)

        daraz_data =[]
        for w, x, y, z in zip(daraz_image_list, daraz_name_list, daraz_price_list, daraz_link_list):
            temp = {
                'image': w,
                'name': x,
                'price': y,
                'link': z
            }
            daraz_data.append(temp)
        return daraz_data


d = Daraz.run()
print(d)


