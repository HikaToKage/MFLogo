from pars_logo_icrawler import pars
from square_logo import square_logo
from resize import resize
from faces import faces
from more_logo import more_logo
from transliterate import translit
from urls import get_urls
from threading import Thread
import os

list = get_urls()


# def clear_img(dir, url):
#     for i in range(1000001, 1001000):
#         direction = f'../Logo/{dir}_{translit(url, reversed=True)}/{dir}_{translit(url, reversed=True)}_{i}.png'

#         try:
#             square_logo(direction) # удаляет прямоугольники
#             resize(direction)
#             # faces(direction)
#             # more_logo(direction)

#         except FileNotFoundError:
#             while len(list) > 0:
#                 list.pop(0)

def clear_img(dir, url):
    try:    
        for url in list:
            try:
                for i in range(1000001, 1001000):
                    direction = f'../Logo/{dir}_{translit(url, reversed=True)}/{dir}_{translit(url, reversed=True)}_{i}.png'
                    square_logo(direction)
                    resize(direction)
                    # more_logo(direction)
                    print(f'{url}-{i}')
            except FileNotFoundError:
                i = i + 1
            except :
                os.remove(direction)
    except FileNotFoundError:
        list.pop(0)


def main():
    # # скачиваем изображения по запросам
    # for url in list:
        # pars(url, translit(url, reversed=True))

    print('Скачивание завершено!\nИдет обработка изображений..')

    for url in list:
        clear_img('bing', url)


if __name__ == "__main__":
    try:
        main()
    except Exception as ex:
        print(f'----------------------\nError: {ex}\n----------------------')
    finally:
        print('Программа завершена!')
