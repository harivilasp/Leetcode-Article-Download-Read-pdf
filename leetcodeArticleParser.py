import requests
import convertapi
from bs4 import BeautifulSoup
import warnings
import os
warnings.filterwarnings("ignore", category=UserWarning, module='bs4')

def getURL(page):
    """

    :param page: html of web page (here: Python home page) 
    :return: urls in that page 
    """
    start_link = page.find(" href")
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1: end_quote]
    return url, end_quote

for i in range(2,10):
    url = "https://leetcode.com/articles/?page="+str(i)
    response = requests.get(url)
    # parse html
    page = str(BeautifulSoup(response.content))

    while True:
        url, n = getURL(page)
        page = page[n:]
        if url:
            if(url[:3]=="/ar"):
                name=url[10:-2];
                url="https://leetcode.com"+url;
                convertapi.api_secret = 'vW90GpchjOqpihf7'
                convertapi.convert('pdf', {
                                'Url': url
                                    }, from_format = 'web').save_files('parsed/'+name+'.pdf')
                if(os.path.getsize(os.getcwd()+"\\parsed\\"+name+".pdf")<101400):
                    os.remove(os.getcwd()+"\\parsed\\"+name+".pdf")
                print(url)
        else:
            break
