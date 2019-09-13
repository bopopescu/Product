import re
from threading import Thread
from django.http import request
from django.shortcuts import render
from bs4 import BeautifulSoup
from selenium import webdriver
# Create your views here.
import datetime
from joblib import Parallel, delayed

searchd = {}


def product(request):
    return render(request, 'compare.html')


def search(request):
    searchData = request.POST.get('search')
    start = datetime.datetime.now()
    searchd['data'] = searchData
    #
    t1 = Daraz()
    t2 = Hamrobazar()
    t3 = Sastodeal()
    # t3 = Dokoman()
    # t4 = MarketThulo()
    # t5 = Muncha()
    # t6 = Esewapasal()
    #
    t1.start()
    t2.start()
    t3.start()
    # t3.start()
    # t4.start()
    # t5.start()
    # t6.start()
    #
    daraz_data = t1.run()
    hamrobazar_data = t2.run()
    sastodeal_data =t3.run()

    # dokoman_data = t3.run()
    # marketthulo_data = t4.run()
    # muncha_data = t5.run()
    # esewapasal_data = t6.run()

    print(f'Tme taken: {datetime.datetime.now() - start}')
    return render(request, 'compare-result.html', {'daraz': daraz_data, 'hamrobazar': hamrobazar_data, 'sastodeal': sastodeal_data})


class Daraz(Thread):
    def run(self):
        browser = webdriver.PhantomJS()
        browser.delete_all_cookies()
        browser.get(
            'https://www.daraz.com.np/catalog/?q='+searchd['data']+'&_keyori=ss&from=input&spm=a2a0e.11779170.search.go.15bb2d2bkd76XX')
        c = browser.page_source
        soup = BeautifulSoup(c, "html.parser")
        daraz_name_list = []
        daraz_price_list = []
        daraz_link_list = []
        daraz_image_list = []
        daraz_product_name = soup.select("div .c16H9d a")
        daraz_product_price = soup.select("div .c3gUW0 .c13VH6")

        daraz_image = soup.select('script', type="application/ld+json")
        image = str(daraz_image[145])
        print(image.split())
        pattern = '"image":"https://static-01.daraz.com.np/'
        res = [x for x in image.split() if re.search(pattern, x)]
        for x in res:
            var = (x.split(','))
            var2 = (var[4])
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



class Hamrobazar(Thread):
    def run(self):
        browser = webdriver.PhantomJS()
        browser.delete_all_cookies()
        browser.get(
            'https://hamrobazaar.com/search.php?do_search=Search&searchword=' + searchd['data'] + '&catid_search=0')
        c2 = browser.page_source
        soup2 = BeautifulSoup(c2, "html.parser")

        hamrobazar_name_list = []
        hamrobazar_price_list = []
        link_list = []
        hamrobazar_image_list = []

        hamrobazar_product_name = soup2.select("a font b")
        hamrobazar_product_price = soup2.select("td~ td+ td > b:nth-child(1)")
        image = soup2.select('center img')
        link = soup2.select('td:nth-child(3)')

        for product in hamrobazar_product_name:
            hamrobazar_name_list.append(product.text)
        for price in hamrobazar_product_price:
            hamrobazar_price_list.append(price.text)
        for i in link:
            for a in i.find_all('a'):
                link = (a.get('href'))
                link_list.append(link)

        hamrobazar_link_list = [i for i in link_list if i.startswith('i')]

        for i in image:
            ima = (i.get('src'))
            hamrobazar_image_list.append(ima)

        hamrobazar_data =[]
        for w, x, y, z in zip(hamrobazar_image_list, hamrobazar_name_list, hamrobazar_price_list, hamrobazar_link_list):
            temp = {
                'image': w,
                'name': x,
                'price': y,
                'link': z
            }
            hamrobazar_data.append(temp)
        return hamrobazar_data

#
# class Dokoman(Thread):
#     def run(self):
#         browser = webdriver.PhantomJS()
#         browser.delete_all_cookies()
#         browser.get(
#             'https://dokoman.com/search?searhkey=' + searchd['data'])
#         c4 = browser.page_source
#         soup4 = BeautifulSoup(c4, "html.parser")
#         dokoman_name_list = []
#         dokoman_price_list = []
#         dokoman_image_list = []
#         dokoman_link_list = []
#
#         dokoman_product_name = soup4.select("#post-data a")
#         dokoman_product_price = soup4.select(".product-price-net")
#         dokoman_product_image = soup4.select("img.img-responsive.center-block")
#         dokoman_product_link = soup4.select('#post-data a')
#
#         for i in dokoman_product_name:
#             items = i.text
#             j = re.sub(r"\s", "", items)
#             spl = j.split('(')[0]
#             if spl != '':
#                 dokoman_name_list.append(spl)
#
#         for i in dokoman_product_price:
#             items = i.text
#             j = re.sub(r"\s", "", items)
#             spl = j.split('(')[0]
#             dokoman_price_list.append(spl)
#
#         for i in dokoman_product_image:
#             items = i.text
#             image = (i.get('src'))
#             dokoman_image_list.append(image)
#
#         for i in dokoman_product_link:
#             link = i.get('href')
#             if link != '#':
#                 dokoman_link_list.append(link)
#
#         context = {
#             'dokoman_name': dokoman_name_list,
#             'dokoman_price': dokoman_price_list,
#             'dokoman_link': dokoman_link_list,
#             'dokoman_image': dokoman_image_list
#         }
#         return context

#
# class MarketThulo(Thread):
#     def run(self):
#         browser = webdriver.PhantomJS()
#         browser.delete_all_cookies()
#         browser.get('https://market.thulo.com/shopping/search?q=' + searchd['data'])
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
#         for w,x,y,z in zip(market_thulo_image_list,market_thulo_product_list,market_thulo_price_list,market_thulo_link_list):
#             temp ={
#                 'image': w,
#                 'name': x,
#                 'price': y,
#                 'link': z
#             }
#             marketthulo_data.append(temp)
#         return marketthulo_data

# class Muncha(Thread):
#     def run(self):
#         browser = webdriver.PhantomJS()
#         browser.delete_all_cookies()
#         browser.get('https://muncha.com/Shop/Search?merchantID=1&CategoryID=0&q=shirt')
#         c7 = browser.page_source
#         soup7 = BeautifulSoup(c7, "html.parser")
#
#         muncha_product_name = soup7.find_all('h5', class_='product-caption-title-sm')
#         muncha_product_price = soup7.find_all('span', class_='product-caption-price-new')
#         muncha_product_image = soup7.find_all('img', class_='product-img-primary')
#         muncha_product_link = soup7.find_all('div', class_='product')
#
#         muncha_name_list = []
#         muncha_price_list = []
#         muncha_image_list = []
#         muncha_link_list = []
#
#         for i in muncha_product_name:
#             items = i.text
#             muncha_name_list.append(items)
#
#         for j in muncha_product_price:
#             item = j.text
#             muncha_price_list.append(item)
#
#         for k in muncha_product_image:
#             image = k.get('src')
#             muncha_image_list.append(image)
#
#         for l in muncha_product_link:
#             for k in l.find_all('a'):
#                 link = k.get('href')
#                 muncha_link_list.append(link)
#
#
#         muncha_data = []
#
#         for i, n, p, l in zip(muncha_image_list, muncha_name_list, muncha_price_list, muncha_link_list):
#             temp = {
#                 'image' : i,
#                 'name' : n,
#                 'price' : p,
#                 'link' : l
#             }
#             muncha_data.append(temp)
#         return muncha_data
#
# class Esewapasal(Thread):
#     def run(self):
#         browser = webdriver.PhantomJS()
#         browser.delete_all_cookies()
#         browser.get('https://www.esewapasal.com/catalogsearch/result/?q='+ searchd['data'])
#         c9 = browser.page_source
#         soup9 = BeautifulSoup(c9, "html.parser")
#         esewapasal_product_name = soup9.select('.product-item-link')
#         esewapasal_product_price = soup9.select('#maincontent .price')
#         esewapasal_product_image = soup9.select('.product-image-photo')
#
#         esewapasal_name_list = []
#         esewapasal_price_list = []
#         esewapasal_image_list = []
#         esewapasal_link_list = []
#         esewa_data =[]
#
#         for i in esewapasal_product_name:
#             items = i.text
#             esewapasal_name_list.append(items)
#
#         for j in esewapasal_product_price:
#             item = j.text
#             esewapasal_price_list.append(item)
#
#         for k in esewapasal_product_image:
#             image = k.get('src')
#             esewapasal_image_list.append(image)
#         for l in esewapasal_product_name:
#             link = (l.get('href'))
#             esewapasal_link_list.append(link)
#
#         for w,x, y, z in zip(esewapasal_image_list, esewapasal_name_list, esewapasal_price_list, esewapasal_link_list):
#             temp ={
#                 'image': w,
#                 'name': x,
#                 'price': y,
#                 'link': z
#             }
#             esewa_data.append(temp)
#         return esewa_data

class Sastodeal(Thread):
    def run(self):
        browser = webdriver.PhantomJS()
        browser.delete_all_cookies()
        browser.get(
            'https://www.sastodeal.com/search.html?q='+searchd['data']+'&hpp=16&idx=sastodeal_products&p=0&is_v=1&isProduct=N')
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
            new_price = 'Rs' + (orginal_price[1])
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
        return (sastodeal_data)