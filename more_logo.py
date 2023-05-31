import os
import imutils
import cv2
from transliterate import translit
from urls import get_urls

def more_logo(url):
    # загрузите изображение, смените цвет на оттенки серого и уменьшите резкость
    image = cv2.imread(url)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (3, 3), 0)

    # распознавание контуров
    edged = cv2.Canny(gray, 10, 250)

    # создайте и примените закрытие
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
    closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)

    # найдите контуры в изображении и подсчитайте количество книг
    cnts = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    total = 0

    # цикл по контурам
    for c in cnts:
        # аппроксимируем (сглаживаем) контур
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.005 * peri, True)

        # определяем количество логотипов
        if len(approx) < 360:
            cv2.drawContours(image, [approx], -1, (0, 255, 0), 2)
            total += 1

    if total > 6:
        os.remove(url)


list = get_urls()
try:    
    for url in list:
            for i in range(1000001, 1001000):
                try:
                    more_logo(f'../Logo/bing_{translit(url, reversed=True)}/bing_{translit(url, reversed=True)}_{i}.png')
                    print(f'{url}-{i}')
                except FileNotFoundError:
                    i = i + 1
                except :
                     os.remove(f'../Logo/bing_{translit(url, reversed=True)}/bing_{translit(url, reversed=True)}_{i}.png')
except FileNotFoundError:
    list.pop(0)