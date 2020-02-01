from django.shortcuts import render
import urllib.request
import requests
from bs4 import BeautifulSoup
import re



# Create your views here.
def index(request):
    return render(request, 'index.html')

def scrap(request):
    if request.method == 'POST':
        item = request.POST['search_bar']

        # try:
        url = 'https://www.flipkart.com/search?q=mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=0&as-type=HISTORY'.format(item)

        page_mobile = urllib.request.urlopen(url).read().decode('utf8', 'ignore')
        soup = BeautifulSoup(page_mobile, "lxml")
        products = soup.find_all("div", {"class": "_1UoZlX"})
        result = []

        for p in products:
            link = p.find('a', {'class': '_31qSD5'})
            link1 = "https://www.flipkart.com/search?q=mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=0&as-type=HISTORY/{}".format(link.attrs['href'])
            mobile_name = p.find('div', {'class': '_3wU53n'}).text
            price = p.find('div', {'class': '_1vC4OE _2rQ-NK'}).text
            image = p.find('div', {'class': '_3SQWE6'})
            image = image.find('div', {'class': '_1OCn9C'})
            image = image.find('div', {'class': '_3BTv9X'})
            # image1 = image.find('img',{'src': re.compile('.jpeg')})
            # image = image.find('img', {'class': '_1Nyybr  _30XEf0'})
            image = image.find("img")
            image = image.get("src")

            data = {
                'mobilemodel': mobile_name,
                'price': price,
                'link': link1,
                "img": image,
            }
            result.append(data)
            print(result)


        return render(request, 'scrap_detail.html', {'result':result})





