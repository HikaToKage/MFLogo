from PIL import Image
from urls import get_urls
from transliterate import translit
import os

list = get_urls()


def resize(dir):
    img = Image.open(dir)
    rgb_img = img.convert('RGB')
    resized_img = rgb_img.resize((256, 256), Image.ANTIALIAS)
    resized_img.save(dir)
    img.close()

list = get_urls()
try:    
    for url in list:
            for i in range(1000001, 1001000):
                try:
                    resize(f'../Logo/bing_{translit(url, reversed=True)}/bing_{translit(url, reversed=True)}_{i}.png')
                    print(f'{url}-{i}')
                except FileNotFoundError:
                    i = i + 1
                except :
                     os.remove(f'../Logo/bing_{translit(url, reversed=True)}/bing_{translit(url, reversed=True)}_{i}.png')
except FileNotFoundError:
    list.pop(0)