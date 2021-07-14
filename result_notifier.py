from bs4 import BeautifulSoup
from lxml import etree
import requests
import datetime

def Scrape():
    now = datetime.datetime.now()

    time = now.strftime("%d-%m-%Y: %a (%I:%M:%S %p)")

    link = "http://cbseresults.nic.in/CBSEResults/Page/Page?PageId=19&LangId=P"

    headers = ({'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
                'Accept-Language': 'en-US, en;q=0.5', 'Cache-Control': 'no-cache'})

    webpage = requests.get(link, headers=headers)
    soup = BeautifulSoup(webpage.content, "html.parser")
    dom = etree.HTML(str(soup))
    result = dom.xpath("//a[contains(text(), 'Secondary School Examination')]")

    if len(result) > 0:
        link = result[0].get('href')

        with open('C:/Users/dhruvjadhav/PycharmProjects/ResultNotifier/log.txt', 'w+') as file:
            file.write(f"{time}: {link}: True")
            file.close()

        return 'True', link, time
    else:
        with open('C:/Users/dhruvjadhav/PycharmProjects/ResultNotifier/log.txt', 'w+') as file:
            file.write(f"{time}: False")
            file.close()

        return 'False'
