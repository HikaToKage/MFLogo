import os
from PIL import Image
from transliterate import translit
from urls import get_urls


def square_logo(url):
    im = Image.open(url)
    (width, height) = im.size

    if width != height:
        im.close()
        os.remove(url)

list = get_urls()
try:    
    for url in list:
            for i in range(1000001, 1001000):
                try:
                    square_logo(f'../Logo/bing_{translit(url, reversed=True)}/bing_{translit(url, reversed=True)}_{i}.png')
                    print(f'{url}-{i}')
                except FileNotFoundError:
                    i = i + 1
                except :
                     os.remove(f'../Logo/bing_{translit(url, reversed=True)}/bing_{translit(url, reversed=True)}_{i}.png')
except FileNotFoundError:
    list.pop(0)
