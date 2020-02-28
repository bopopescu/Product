import re
import urllib
from threading import Thread
import json
import random
from django.db.models import Count
from django.http import request
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
from selenium import webdriver
# Create your views here.
import datetime
from .models import SearchQuery, Feedback, IP
from django.views.decorators.csrf import csrf_exempt
from uuid import getnode as get_mac

from joblib import Parallel, delayed

searchd = {}

def product(request):
    return render(request, 'compare.html')


def search(request):
    ip_list = []
    searchData = request.POST.get('search')
    print(searchData)
    daraz = request.POST.get('daraz')
    hamrobazar =  request.POST.get('hamrobazar')
    sastodeal =  request.POST.get('sastodeal')
    dokoman = request.POST.get('dokoman')
    marketthulo = request.POST.get('marketthulo')
    muncha = request.POST.get('muncha')
    esewapasal = request.POST.get('esewapasal')
    print(daraz)
    print(hamrobazar)
    # searchsave = SearchQuery.objects.create(search=searchData)
    # searchsave.save()
    start = datetime.datetime.now()
    searchd['data'] = searchData
    site = {}
    display = {}
    if (daraz == 'daraz'):

        t1 = Daraz()
        t1.start()
        daraz_data = t1.run()
        site['daraz']= daraz_data
        print('here')
        print(site['daraz'])
        display['daraz'] = True


    if(hamrobazar == 'hamrobazar'):
        t2 = Hamrobazar()
        t2.start()
        hamrobazar_data = t2.run()
        site['hamrobazar'] = hamrobazar_data
        display['hamrobazar'] = True


    if(sastodeal == 'sastodeal'):
        t3 = Sastodeal()
        t3.start()
        sastodeal_data = t3.run()
        site['sastodeal'] = sastodeal_data
        display['sastodeal'] = True


    if (dokoman == 'dokoman'):
        t4 = Dokoman()
        t4.start()
        dokoman_data = t4.run()
        site['dokoman'] = dokoman_data
        display['dokoman'] = True


    if (marketthulo== 'marketthulo'):
        t5 = MarketThulo()
        t5.start()
        marketthulo_data = t5.run()
        site['marketthulo'] = marketthulo_data
        display['marketthulo'] = True


    if (muncha == 'muncha'):
        t6 = Muncha()
        t6.start()
        muncha_data = t6.run()
        site['muncha'] = muncha_data
        display['muncha'] = True

    if (esewapasal == 'esewapasal'):
        t7 = Esewapasal()
        t7.start()
        esewapasal_data = t7.run()
        site['esewapasal'] = esewapasal_data
        display['esewapasal'] = True


    print(site)
    print(display)
    daraz_data_status = True
    sasto_data_status = True
    hamrobazar_data_status = True
    esewapasal_data_status = True
    muncha_data_status = True
    dokoman_data_status = True

    try:
        if bool(site['daraz']):
            daraz_data_status = True
        else:
            daraz_data_status = False
    except:
        print('error')

    try:
        if bool(site['sastodeal']):
            sasto_data_status = True
        else:
            sasto_data_status = False
    except:
        print('error')

    try:
        if bool(site['hamrobazar']):
            hamrobazar_data_status = True
        else:
            hamrobazar_data_status = False
    except:
        print('error')

    try:
        if bool(site['esewapasal']):
            esewapasal_data_status = True
        else:
            esewapasal_data_status = False
    except:
        print('error')
    try:
        if bool(site['muncha']):
            muncha_data_status = True
        else:
            muncha_data_status = False
    except:
        print('error')
    try:
        if bool(site['dokoman']):
            dokoman_data_status = True
        else:
            dokoman_data_status = False
    except:
        print('error')
    ip_client = (get_client_ip(request))
    ip_save = IP.objects.create(ip_address=ip_client)
    ip_save.save()
    print(f'Tme taken: {datetime.datetime.now() - start}')
    return render(request, 'compare-result.html',{'site':site, 'display':display, 'daraz_st': daraz_data_status, 'hamrobazar_st': hamrobazar_data_status, 'sastodeal_st': sasto_data_status, 'muncha_st': muncha_data_status, 'dokoman_st': dokoman_data_status, 'esewapasal_st': esewapasal_data_status})
    # return render(request, 'compare-result.html', {'site':site, 'display': display})


# class Daraz(Thread):
#     def run(self):
#         browser = webdriver.PhantomJS()
#         browser.delete_all_cookies()
#         browser.get(
#             'https://www.daraz.com.np/catalog/?q='+searchd['data']+'&_keyori=ss&from=input&spm=a2a0e.11779170.search.go.15bb2d2bkd76XX')
#         c = browser.page_source
#         soup = BeautifulSoup(c, "html.parser")
#         daraz_name_list = []
#         daraz_price_list = []
#         daraz_link_list = []
#         daraz_image_list = []
#         daraz_product_name = soup.select("div .c16H9d a")
#         daraz_product_price = soup.select("div .c3gUW0 .c13VH6")
#
#         daraz_image = soup.select('script', type="application/ld+json")
#         image = str(daraz_image[17])
#         # print(image.split())
#         pattern = '"image":"https://static-01.daraz.com.np/'
#         res = [x for x in image.split() if re.search(pattern, x)]
#         for x in res:
#             var = (x.split(','))
#             var2 = [x for x in var if '"image":' in x]
#             var2 = var2[0]
#             var3 = var2[9:-1]
#             daraz_image_list.append(var3)
#
#         for product in daraz_product_name:
#             daraz_name_list.append(product.text)
#
#         for price in daraz_product_price:
#             pric = price.text
#             nprice = pric.replace("Rs.", '')
#             price = nprice.replace(',', '')
#             daraz_price_list.append(price)
#
#         link = soup.find_all('div', class_='c16H9d')
#         for i in link:
#             for a in i.find_all('a'):
#                 href = (a.get('href'))
#                 daraz_link_list.append(href)
#
#         daraz_data =[]
#         for w, x, y, z in zip(daraz_image_list, daraz_name_list, daraz_price_list, daraz_link_list):
#             temp = {
#                 'image': w,
#                 'name': x,
#                 'price': y,
#                 'link': z
#             }
#             daraz_data.append(temp)
#         return daraz_data

class Daraz(Thread):
    def run(self):
        urlpage = 'https://www.daraz.com.np/catalog/?q='+searchd['data']+'&_keyori=ss&from=input&spm=a2a0e.searchlist.search.go.545a77524tE5ep'
        page = urllib.request.urlopen(urlpage)
        soup = BeautifulSoup(page, 'html.parser')
        data = soup.select('script')

        list = []
        for i in data:
            list.append(i)

        a = (str(list[3]))[24:-9]
        list1 = (json.loads(a))["mods"]["listItems"]
        data = [{"name": x["name"], "link": x["productUrl"], "price": x["price"], "image": x["image"]} for x in
                      list1]
        daraz_data1 =json.dumps(data)
        daraz_data = json.loads(daraz_data1)
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
            pric = price.text
            nprice = pric.replace("Rs.", '')
            price = nprice.replace(',', '')
            hamrobazar_price_list.append(price)

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


class Dokoman(Thread):
    def run(self):
        browser = webdriver.PhantomJS()
        browser.delete_all_cookies()
        browser.get(
            'https://dokoman.com/search?searhkey=' + searchd['data'])
        c4 = browser.page_source
        soup4 = BeautifulSoup(c4, "html.parser")
        dokoman_name_list = []
        dokoman_price_list = []
        dokoman_image_list = []
        dokoman_link_list = []

        dokoman_product_name = soup4.select("#post-data a")
        dokoman_product_price = soup4.select(".product-price-net")
        dokoman_product_image = soup4.select("img.img-responsive.center-block")
        dokoman_product_link = soup4.select('#post-data a')

        for i in dokoman_product_name:
            items = i.text
            j = re.sub(r"\s", "", items)
            spl = j.split('(')[0]
            if spl != '':
                dokoman_name_list.append(spl)

        for i in dokoman_product_price:
            items = i.text
            j = re.sub(r"\s", "", items)
            spl = j.split('(')[0]
            dokoman_price_list.append(spl)

        for i in dokoman_product_image:
            items = i.text
            image = (i.get('src'))
            dokoman_image_list.append(image)

        for i in dokoman_product_link:
            link = i.get('href')
            if link != '#':
                dokoman_link_list.append(link)

        dokoman_data = []
        for w, x, y, z in zip(dokoman_image_list, dokoman_name_list, dokoman_price_list, dokoman_link_list):
            temp = {
                'image': w,
                'name': x,
                'price': y,
                'link': z
            }
            dokoman_data.append(temp)
        return dokoman_data


class MarketThulo(Thread):
    def run(self):
        browser = webdriver.PhantomJS()
        browser.delete_all_cookies()
        browser.get('https://market.thulo.com/shopping/search?q=' + searchd['data'])
        c6 = browser.page_source
        soup6 = BeautifulSoup(c6, "html.parser")

        market_thulo_price = soup6.select('.thirdGridActive span')
        market_thulo_product = soup6.select('h4 a')
        market_thulo_link = soup6.select('h4 a')

        market_thulo_image_list = []
        market_thulo_price_list = []
        market_thulo_product_list = []
        market_thulo_link_list = []

        for j in market_thulo_product:
            item = j.text
            if item != '':
                market_thulo_product_list.append(item)

        for i in market_thulo_price:
            items = i.text
            if items != '×':
                if items != '':
                    market_thulo_price_list.append(items)

        for i in market_thulo_link:
            item = (i.get('href'))
            market_thulo_link_list.append(item)

        market_thulo_link_list.pop(0)

        marketthulo_data = []

        for w,x,y,z in zip(market_thulo_image_list,market_thulo_product_list,market_thulo_price_list,market_thulo_link_list):
            temp ={
                'image': w,
                'name': x,
                'price': y,
                'link': z
            }
            marketthulo_data.append(temp)
        return marketthulo_data

class Muncha(Thread):
    def run(self):
        browser = webdriver.PhantomJS()
        browser.get('https://muncha.com/Shop/Search?merchantID=1&CategoryID=0&q='+ searchd['data'])
        c7 = browser.page_source
        soup7 = BeautifulSoup(c7, "html.parser")

        muncha_product_name = soup7.find_all('h5', class_='product-caption-title-sm')
        muncha_product_price = soup7.find_all('span', class_='product-caption-price-new')
        muncha_product_image = soup7.find_all('img', class_='product-img-primary')
        muncha_product_link = soup7.find_all('div', class_='product')

        muncha_name_list = []
        muncha_price_list = []
        muncha_image_list = []
        muncha_link_list = []

        for i in muncha_product_name:
            items = i.text
            muncha_name_list.append(items)

        for j in muncha_product_price:
            pric = j.text
            nprice = pric.replace("Rs.", '')
            price = nprice.replace(',', '')
            muncha_price_list.append(price)

        for k in muncha_product_image:
            image = k.get('src')
            muncha_image_list.append(image)

        for l in muncha_product_link:
            for k in l.find_all('a'):
                link = k.get('href')
                muncha_link_list.append(link)


        muncha_data = []

        for i, n, p, l in zip(muncha_image_list, muncha_name_list, muncha_price_list, muncha_link_list):
            temp = {
                'image': i,
                'name': n,
                'price': p,
                'link': l
            }
            muncha_data.append(temp)
        return muncha_data


class Esewapasal(Thread):
    def run(self):
        browser = webdriver.PhantomJS()
        browser.delete_all_cookies()
        browser.get('https://www.bhatbhatenionline.com/catalogsearch/result/?q='+searchd['data'])
        c9 = browser.page_source
        soup9 = BeautifulSoup(c9, "html.parser")
        esewapasal_product_name = soup9.select('.item-wrap .title')
        esewapasal_product_link = soup9.select('.item-wrap a')
        esewapasal_product_price = soup9.select('.green')
        esewapasal_product_image = soup9.select('.product-image-photo')

        esewapasal_name_list = []
        esewapasal_price_list = []
        esewapasal_image_list = []
        esewapasal_link_list = []
        esewa_data =[]

        for i in esewapasal_product_name:
            items = i.text
            j = re.sub(r"\s", "", items)
            esewapasal_name_list.append(j)

        for j in esewapasal_product_price:
            item = j.text
            p = item.replace(',', '')
            nprice = p.replace("रु.", '')
            price = nprice[:-3]
            esewapasal_price_list.append(price)

        for k in esewapasal_product_image:
            image = k.get('src')
            esewapasal_image_list.append(image)

        for l in esewapasal_product_link:
            link = (l.get('href'))
            esewapasal_link_list.append(link)

        for w,x, y, z in zip(esewapasal_image_list, esewapasal_name_list, esewapasal_price_list, esewapasal_link_list):
            temp ={
                'image': w,
                'name': x,
                'price': y,
                'link': z
            }
            esewa_data.append(temp)
        return esewa_data


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

        sastodeals = list(dict.fromkeys(sastodeal_link_list))


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
        for w,x,y,z in zip(sastodeal_image_list,sastodeal_name_list, sastodeal_price_list, sastodeals):
            temp ={
                'image': w,
                'name': x,
                'price': y,
                'link': z
            }
            sastodeal_data.append(temp)
        return (sastodeal_data)

@csrf_exempt
def feedback(request):
    return render(request, 'feedback.html')

@csrf_exempt
def feedback_data(request):
    email = request.POST['email']
    question_1 = request.POST['ques_1']
    question_2 = request.POST['question2']
    question_3 = request.POST['question3']
    question_4 = request.POST['question4']
    feedback = request.POST['feedback']
    ip= random.randint(100, 200)
    if (ip == 100 or ip == 160):
        prize = '50 rupee'
    elif (ip >= 101 and ip <= 140):
        prize = '10 rupee'
    elif (ip >= 150 and ip <= 155):
        prize = '20 rupee'
    else:
        prize = 'Try Again'
    number = Feedback.objects.filter(email= email).count()
    if (number > 0):
        context = {'emdup': True}
        return render(request, 'feedback.html', context)

    feed = Feedback.objects.create(email= email,question_1=question_1, question_2=question_2, question_3=question_3, question_4=question_4, feedback=feedback, prize=prize)
    feed.save()
    context = {"prize": prize}
    return render(request, 'compare.html', context)

@csrf_exempt
def feedback_list(request):
    c1 = Feedback.objects.values('question_1').annotate(
        c=Count('question_1')).order_by('-c')
    c2 = Feedback.objects.values('question_2').annotate(
        c=Count('question_2')).order_by('-c')
    c3 = Feedback.objects.values('question_3').annotate(
        c=Count('question_3')).order_by('-c')
    c4 = Feedback.objects.values('question_4').annotate(
        c=Count('question_4')).order_by('-c')
    feed = Feedback.objects.filter(feedback__isnull=False).values('feedback')
    email = Feedback.objects.filter(email__isnull=False).values('email')
    result = Feedback.objects.filter(email__isnull=False).values('email', 'prize')
    ip_count = IP.objects.count()
    return render(request, 'feedback_list.html', {'feed': feed,'c1': c1, 'c2': c2, 'c3': c3, 'c4': c4, 'email' : email, 'result':result, 'ip_count': ip_count})

count =0

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def won(request):
    return render(request, 'won.html')