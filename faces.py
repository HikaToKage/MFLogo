import os
import cv2
from os import path
from transliterate import translit
from urls import get_urls
import numpy as np


def faces(url):
    prototxt_path = "weights/deploy.prototxt.txt"
    model_path = "weights/res10_300x300_ssd_iter_140000_fp16.caffemodel"

    # загрузим модель Caffe
    model = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)

    # url = "E:\ing_emblema istoricheskogo fakul'teta_1000029.png"
    # читаем изображение
    image = cv2.imread(url)
    # получаем ширину и высоту изображения
    h, w = image.shape[:2]  

    # предварительная обработка: изменение размера и вычитание среднего
    blob = cv2.dnn.blobFromImage(image, 1.0, (300, 300), (104.0, 177.0, 123.0))

    # устанавливаем на вход нейронной сети изображение
    model.setInput(blob)
    # выполняем логический вывод и получаем результат
    output = np.squeeze(model.forward())

    font_scale = 1.0
    for i in range(0, output.shape[0]):
        # получить уверенность
        confidence = output[i, 2]
        # если достоверность выше 50%, то нарисуйте окружающий прямоугольник
        if confidence > 0.5:
            os.remove(url)

list = get_urls()
try:    
    for url in list:
            for i in range(1000001, 1001000):
                try:
                    faces(f'../Logo/bing_{translit(url, reversed=True)}/bing_{translit(url, reversed=True)}_{i}.png')
                    print(f'{url}-{i}')
                except :
                    i = i + 1
except :
    list.pop(0)