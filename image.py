import re
import requests
from bs4 import BeautifulSoup
from PIL import ImageFile

site = 'https://cloud.google.com/blog/products/data-analytics/'

def get_images():
    response = requests.get(site)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles_tags = soup.find_all('a', attrs={'track-type': 'articlefeedblock'})
    articles = [a['href'] for a in articles_tags]

    # print(articles)
    needed_list = []
    for article in articles:
        response = requests.get(article)
        soup = BeautifulSoup(response.text, 'html.parser')
        img_tags = soup.find_all('img')
        # print(img_tags)
        urls = [img['src'] for img in img_tags]
        # print(urls)
        images = []
        for url in urls:
            images.append(url.rsplit('/', 1)[1])
        # print(images)
        res = ""
        counter = 0
        for image in images:
            if '1_' in image:
                res = res + image
                break
        if len(res) == 0:
            res = res + images[0]
        # print(res)
        for url in urls:
            if res in url:
                result = {
                "image": url,
                "site": article
            }

        # print(result)
        needed_list.append(result)

    return needed_list