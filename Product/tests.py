import re
from time import sleep

from django.contrib.sites import requests
from django.test import TestCase
from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import re

# browser = webdriver.PhantomJS()
# browser.delete_all_cookies()
# browser.get('https://market.thulo.com/shopping/search?q=shampoo')
# c6 = browser.page_source
# soup6 = BeautifulSoup(c6, "html.parser")
# market_thulo_price = soup6.select('.thirdGridActive span')
# market_thulo_product = soup6.select('h4 a')
# market_thulo_link = soup6.select('h4 a')
#
# market_thulo_price_list = []
# market_thulo_product_list = []
# market_thulo_link_list = []
#
# for j in market_thulo_product:
#     item = j.text
#     if item != '':
#         market_thulo_product_list.append(item)
#
# print(market_thulo_price_list)
# for i in market_thulo_price:
#     items = i.text
#     if items != '×':
#         if items != '':
#             market_thulo_price_list.append(items)
#
# for i in market_thulo_link:
#     item = (i.get('href'))
#     market_thulo_link_list.append(item)
#
# market_thulo_link_list.pop(0)
#
# print(market_thulo_link_list)
#
# market_thulo = dict(zip(market_thulo_product_list, market_thulo_price_list))
# print(market_thulo)


# browser = webdriver.PhantomJS()
# browser.delete_all_cookies()
# browser.get('https://smartdoko.com/search?q=shampoo')
# c8 = browser.page_source
# soup8 = BeautifulSoup(c8, "html.parser")
#
# smartdoko_product_name = soup8.find_all('p', class_='title')
# smartdoko_product_price = soup8.select('.text-center h2')
#
# smartdoko_name_list = []
# smartdoko_price_list = []
#
# for i in smartdoko_product_name:
#     items = i.text
#     smartdoko_name_list.append(items)
#
# for j in smartdoko_product_price:
#     item = j.text
#     smartdoko_price_list.append(item)
#
# smartdoko = dict(zip(smartdoko_name_list, smartdoko_price_list))
# print(smartdoko)

# browser = webdriver.PhantomJS()
# browser.delete_all_cookies()
# browser.get('https://www.esewapasal.com/catalogsearch/result/?q=shampoo')
# c9 = browser.page_source
# soup9 = BeautifulSoup(c9, "html.parser")
# esewapasal_product_name = soup9.select('.product-item-link')
# esewapasal_product_price = soup9.select('#maincontent .price')
# esewapasal_product_image = soup9.select('.product-image-photo')
# print(esewapasal_product_image)
#
# esewapasal_name_list = []
# esewapasal_price_list = []
# esewapasal_image_list =[]
# esewapasal_link_list =[]
#
# for i in esewapasal_product_name:
#     items = i.text
#     esewapasal_name_list.append(items)
#
# for j in esewapasal_product_price:
#     item = j.text
#     esewapasal_price_list.append(item)
#
# for k in esewapasal_product_image:
#     image = k.get('src')
#     esewapasal_image_list.append(image)
# for l in esewapasal_product_name:
#     link = (l.get('href'))
#     esewapasal_link_list.append(link)
#
# esewapasal = dict(zip(esewapasal_name_list, esewapasal_price_list))
# #
# browser = webdriver.PhantomJS()
# browser.delete_all_cookies()
# browser.get('https://www.style97.com/?search_category=&s=belt&search_posttype=product')
# c5 = browser.page_source
# soup5 = BeautifulSoup(c5, "html.parser")
#
# style97_price = soup5.select('span.woocommerce-Price-amount.amount')
# style97_product = soup5.select('h4 a')
# style97_image = soup5.select('.wp-post-image')
#
# style97_price_list = []
# style97_product_list = []
# style97_image_list = []
#
# for j in style97_price:
#     item = j.text
#     style97_price_list.append(item)
#
# for i in style97_product:
#     items = i.text
#     if items != 'Quick View':
#         if items != 'Add to cart':
#             if items != 'Read more':
#                 if items != 'Clear':
#                     if items !='Select options':
#                         if items != '':
#                             style97_product_list.append(items)
#
# for j in style97_image:
#     image = (j.get('src'))
#     style97_image_list.append(image)
#
# style97 = dict(zip(style97_product_list, style97_price_list))
#
# print(len(style97_image_list))
# print(len(style97_price_list))
# print(style97_price_list)
# print(len(style97_product_list))
# print(style97_image_list)
#
# from threading import *
#
# class Hello(Thread):
#     def run(selfs):
#         browser = webdriver.PhantomJS()
#         browser.delete_all_cookies()
#         browser.get(
#             'https://www.daraz.com.np/catalog/?q=shampoo&_keyori=ss&from=input&spm=a2a0e.11779170.search.go.15bb2d2bkd76XX')
#         c = browser.page_source
#         soup = BeautifulSoup(c, "html.parser")
#         daraz_name_list = []
#         daraz_price_list = []
#         daraz_link_list = []
#         daraz_image_list = []
#         daraz_product_name = soup.select("div .c16H9d a")
#         daraz_product_price = soup.select("div .c3gUW0 .c13VH6")
#         for product in daraz_product_name:
#             daraz_name_list.append(product.text)
#         for price in daraz_product_price:
#             daraz_price_list.append(price.text)
#
#         link = soup.find_all('div', class_='c16H9d')
#         for i in link:
#             for a in i.find_all('a'):
#                 href = (a.get('href'))
#                 daraz_link_list.append(href)
#
#         daraz = dict(zip(daraz_name_list, daraz_price_list))
#         print(daraz_name_list)
#         print(daraz_price_list)
#         print(daraz_link_list)
#         print(daraz_image_list)
#
#
# class Hi(Thread):
#     def run(selfs):
#         browser = webdriver.PhantomJS()
#         browser.delete_all_cookies()
#         browser.get('https://market.thulo.com/shopping/search?q=shampoo')
#         c6 = browser.page_source
#         soup6 = BeautifulSoup(c6, "html.parser")
#         market_thulo_price = soup6.select('.thirdGridActive span')
#         market_thulo_product = soup6.select('h4 a')
#         market_thulo_link = soup6.select('h4 a')
#
#         market_thulo_price_list = []
#         market_thulo_product_list = []
#         market_thulo_link_list = []
#
#         for j in market_thulo_product:
#             item = j.text
#             if item != '':
#                 market_thulo_product_list.append(item)
#
#         print(market_thulo_price_list)
#         for i in market_thulo_price:
#             items = i.text
#             if items != '×':
#                 if items != '':
#                     market_thulo_price_list.append(items)
#
#         for i in market_thulo_link:
#             item = (i.get('href'))
#             market_thulo_link_list.append(item)
#
#         market_thulo_link_list.pop(0)
#         print('______Item_List________')
#
#         print(market_thulo_link_list)
#
#         market_thulo = dict(zip(market_thulo_product_list, market_thulo_price_list))
#         print(market_thulo)
#
#
# class thread2(Thread):
#    def run(self):
#        browser = webdriver.PhantomJS()
#        browser.delete_all_cookies()
#        browser.get('https://market.thulo.com/shopping/search?q=pant')
#        c6 = browser.page_source
#        soup6 = BeautifulSoup(c6, "html.parser")
#        market_thulo_price = soup6.select('.thirdGridActive span')
#        market_thulo_product = soup6.select('h4 a')
#        market_thulo_link = soup6.select('h4 a')
#
#        market_thulo_price_list = []
#        market_thulo_product_list = []
#        market_thulo_link_list = []
#
#        for j in market_thulo_product:
#            item = j.text
#            if item != '':
#                market_thulo_product_list.append(item)
#
#        print(market_thulo_price_list)
#        for i in market_thulo_price:
#            items = i.text
#            if items != '×':
#                if items != '':
#                    market_thulo_price_list.append(items)
#
#        for i in market_thulo_link:
#            item = (i.get('href'))
#            market_thulo_link_list.append(item)
#
#        market_thulo_link_list.pop(0)
#        print('______Item_List________')
#
#        print(market_thulo_link_list)
#
#        market_thulo = dict(zip(market_thulo_product_list, market_thulo_price_list))
#        print(market_thulo)
#
# t1 = Hello()
# t2 = Hi()
# t3 =thread2()
#
# t1.start()
# t2.start()
# t3.start()



# browser = webdriver.PhantomJS()
# browser.delete_all_cookies()
# browser.get('https://www.brainyquote.com/topics/brain-quotes')
# c = browser.page_source
# soup = BeautifulSoup(c, "html.parser")
#
# quote = soup.select('.oncl_q')
# tags = soup.select('.oncl_list_kc')
# print(tags)
# for i in quote:
#     print('Quote')
#     print(i.text)
#
# for i in tags:
#     print(i.text)


#
# browser = webdriver.Chrome()
# browser.delete_all_cookies()
# browser.get('https://logisparktech.com/WDN/')
# c = browser.page_source
# soup = BeautifulSoup(c, "html.parser")
#
# link = soup.findAll('a')
# link_list = []
# for i in link:
#     lin = (i.get('href'))
#     link_list.append(lin)
#
# print(link_list)


# class MarketThulo():
#     def run(self):
#         browser = webdriver.PhantomJS()
#         browser.delete_all_cookies()
#         browser.get('https://market.thulo.com/shopping/search?q=shampoo')
#         c6 = browser.page_source
#         soup6 = BeautifulSoup(c6, "html.parser")
#
#         market_thulo_price = soup6.select('.thirdGridActive span')
#         market_thulo_product = soup6.select('h4 a')
#         market_thulo_link = soup6.select('h4 a')
#
#         market_thulo_image_list = []
#         market_thulo_price_list = []
#         market_thulo_product_list = []
#         market_thulo_link_list = []
#
#         for j in market_thulo_product:
#             item = j.text
#             if item != '':
#                 market_thulo_product_list.append(item)
#         print()
#
#         for i in market_thulo_price:
#             items = i.text
#             if items != '×':
#                 if items != '':
#                     market_thulo_price_list.append(items)
#
#         for i in market_thulo_link:
#             item = (i.get('href'))
#             market_thulo_link_list.append(item)
#
#         market_thulo_link_list.pop(0)
#
#         marketthulo_data = []
#
#         print(market_thulo_product_list)
#         print(market_thulo_price_list)
#         print(market_thulo_link_list)
#         print((market_thulo_image_list))
#
#         for w,x,y,z in zip(market_thulo_image_list,market_thulo_product_list,market_thulo_price_list,market_thulo_link_list):
#             temp ={
#                 'image': w,
#                 'name': x,
#                 'price': y,
#                 'link': z
#             }
#             marketthulo_data.append(temp)
#         return marketthulo_data
#
#
# ob = MarketThulo()
# ob.run()

# class Daraz():
#     def run(self):
#         browser = webdriver.PhantomJS()
#         browser.delete_all_cookies()
#         browser.get(
#             'https://www.daraz.com.np/catalog/?q=shirt&_keyori=ss&from=input&spm=a2a0e.11779170.search.go.15bb2d2bkd76XX')
#         c = browser.page_source
#         soup = BeautifulSoup(c, "html.parser")
#         daraz_name_list = []
#         daraz_price_list = []
#         daraz_link_list = []
#         daraz_image_list = []
#         daraz_product_name = soup.select("div .c16H9d a")
#         daraz_product_price = soup.select("div .c3gUW0 .c13VH6")
#
#         daraz_image = soup.select('script' ,type="application/ld+json")
#         image = str(daraz_image[145])
#         print(image.split())
#         pattern = '"image":"https://static-01.daraz.com.np/'
#         res = [x for x in image.split() if re.search(pattern, x)]
#         for x in res:
#             var = (x.split(','))
#             var2 = (var[4])
#             var3 = var2[9:-1]
#             daraz_image_list.append(var3)
#         print(daraz_image_list)
#         for product in daraz_product_name:
#             daraz_name_list.append(product.text)
#         for price in daraz_product_price:
#             daraz_price_list.append(price.text)
#
#         link = soup.find_all('div', class_='c16H9d')
#         for i in link:
#             for a in i.find_all('a'):
#                 href = (a.get('href'))
#                 daraz_link_list.append(href)
#
#         context = {
#             'daraz_image': daraz_image_list,
#             'daraz_name': daraz_name_list,
#             'daraz_price': daraz_price_list,
#             'daraz_link': daraz_link_list
#         }
#         print(context)
#         return context
#
#
# ob = Daraz()
# ob.run()


class Sastodeal():
    def run(self):
        browser = webdriver.PhantomJS()
        browser.delete_all_cookies()
        browser.get(
            'https://www.sastodeal.com/search.html?q=shirt&hpp=16&idx=sastodeal_products&p=0&is_v=1&isProduct=N')
        c = browser.page_source
        soup = BeautifulSoup(c, "html.parser")

        sastodeal_image_list = []
        sastodeal_name_list = []
        sastodeal_price_list = []
        sastodeal_link_list = []

        sastodeal_product_image = soup.select('#hits img')
        sastodeal_product_name = soup.select("#hits a")
        sastodeal_product_price = soup.select(".product-price")

        for i in sastodeal_product_image:
            image = i.get('src')
            sastodeal_image_list.append(image)


        for k in sastodeal_product_name:
            links = k.get('href')
            sastodeal_link_list.append(links)

        for j in sastodeal_product_name:
            name = j.text
            if name != '':
                sastodeal_name_list.append(name)

        print(sastodeal_name_list)

        for l in sastodeal_product_price:
            price = l.text
            orginal_price = price.split('रु')
            new_price = (orginal_price[1])
            sastodeal_price_list.append(new_price)

        sastodeal_data = []
        for w,x,y,z in zip(sastodeal_image_list,sastodeal_name_list, sastodeal_price_list, sastodeal_link_list):
            temp ={
                'image': w,
                'name': x,
                'price': y,
                'link': z
            }
            sastodeal_data.append(temp)
        print(sastodeal_data)


ob = Sastodeal()
ob.run()