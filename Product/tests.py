
import re
import urllib.request
from bs4 import BeautifulSoup
import json

from selenium import webdriver

# urlpage = 'https://www.daraz.com.np/catalog/?q=earphone&_keyori=ss&from=input&spm=a2a0e.searchlist.search.go.545a77524tE5ep'
# page = urllib.request.urlopen(urlpage)
# soup = BeautifulSoup(page, 'html.parser')
# data = soup.select('script')
#
#
# list = []
# for i in data:
#     list.append(i)
#
# a = (str(list[3]))[24:-9]
# list1 = (json.loads(a))["mods"]["listItems"]
# daraz_data = [ {"image": x["image"], "name":x["name"],  "price":x["price"],"link": x["productUrl"]} for x in list1]
# print(json.dumps(daraz_data))
#
# browser = webdriver.PhantomJS()
# browser.delete_all_cookies()
# browser.get(
#     'https://hamrobazaar.com/search.php?do_search=Search&searchword=earphone&catid_search=0')
# c2 = browser.page_source
# soup2 = BeautifulSoup(c2, "html.parser")
#
# hamrobazar_name_list = []
# hamrobazar_price_list = []
# link_list = []
# hamrobazar_image_list = []
#
# hamrobazar_product_name = soup2.select("a font b")
# hamrobazar_product_price = soup2.select("td~ td+ td > b:nth-child(1)")
# image = soup2.select('center img')
# link = soup2.select('td:nth-child(3)')
#
# for product in hamrobazar_product_name:
#     hamrobazar_name_list.append(product.text)
# for price in hamrobazar_product_price:
#     pric = price.text
#     nprice = pric.replace("Rs.", '')
#     price = nprice.replace(',', '')
#     hamrobazar_price_list.append(price)
#
# for i in link:
#     for a in i.find_all('a'):
#         link = (a.get('href'))
#         link_list.append(link)
#
# hamrobazar_link_list = [i for i in link_list if i.startswith('i')]
#
# for i in image:
#     ima = (i.get('src'))
#     hamrobazar_image_list.append(ima)
#
# hamrobazar_data = []
# for w, x, y, z in zip(hamrobazar_image_list, hamrobazar_name_list, hamrobazar_price_list, hamrobazar_link_list):
#     temp = {
#         'image': w,
#         'name': x,
#         'price': y,
#         'link': z
#     }
#     hamrobazar_data.append(temp)
#
# print(hamrobazar_data)

# ip = 54
# if (ip == 0 or ip == 60):
#     prize = '50 rupee'
# elif (ip >= 10 and ip <=40):
#     prize = '10 rupee'
# elif (ip >= 50 and ip <=55):
#     prize = '20 rupee'
# else:
#     prize = 'Try Again'
#
# print(prize)

# import PyPDF2
# from PyPDF2 import PdfFileReader as r
# # pdf file object
# # you can find find the pdf file with complete code in below
# pdfFileObj = open('Kusal_Bista_0512_Final.pdf', 'rb')
# # pdf reader object
# pdfReader = r(pdfFileObj)
# # number of pages in pdf
# print(pdfReader.numPages)
# # a page object
# pageObj = pdfReader.getPage(0)
# # extracting text from page.
# # this will print the text you can also save that into String
# print(pageObj.extractText())
#
# from pdfrw import PdfReader, PdfWriter
# pages = PdfReader('/home/pramisha/Downloads/INTERN-MOCKUP DEFENSE (1).pdf').pages
# outdata = PdfWriter('First_page_pramisheeeee.pdf')
# outdata.addPage(pages[0])
# outdata.write()

# import re
# from collections import Counter
# class Daraz():
#     def run(self):
#         s = 'bean bag'
#         search_item = s.replace(" ", "")
#         urlpage = 'https://www.daraz.com.np/catalog/?q='+ search_item+ '&_keyori=ss&from=input&spm=a2a0e.searchlist.search.go.545a77524tE5ep'
#         page = urllib.request.urlopen(urlpage)
#         soup = BeautifulSoup(page, 'html.parser')
#         data = soup.select('script')
#
#         list = []
#         for i in data:
#             list.append(i)
#
#         a = (str(list[3]))[24:-9]
#         list1 = (json.loads(a))["mods"]["listItems"]
#         data = [{"name": x["name"], "link": x["productUrl"], "price": x["price"], "image": x["image"]} for x in
#                       list1]
#         daraz_data1 =json.dumps(data)
#         daraz_data = json.loads(daraz_data1)
#         print(bool(data))
#         return daraz_data
#
# d = Daraz()
# print(d.run())

