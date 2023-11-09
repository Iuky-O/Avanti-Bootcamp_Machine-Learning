  #Importando Bibliotecas

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import cv2

  #Importando a Imagem do Computador

from google.colab import files
uploaded = files.upload()

  #Carregando A Imagem

image_path = 'cachorrinhos.jpg';
image2 = cv2.imread(image_path);

  #Convertendo BGR para RGB

image_rgb = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)

  #Exibindo a imagem

plt.imshow(image_rgb)
plt.axis('off')
plt.show()

  #Aplicando Filtros da Media, Mediana e Gaussiano

media_image = cv2.blur(image_rgb, (15,15))
mediana_image = cv2.medianBlur(image_rgb, 15)
gaussiano_image = cv2.GaussianBlur(image_rgb, (15, 15), 0)

  #Plotar as imagens - matplotlib

plt.subplot(2, 2, 1)
plt.imshow(image_rgb)
plt.axis('off')
plt.title('Imagem original')

plt.subplot(2, 2, 2)
plt.imshow(media_image)
plt.axis('off')
plt.title('Imagem com Filtro da Média')

plt.subplot(2, 2, 3)
plt.imshow(mediana_image)
plt.axis('off')
plt.title('Imagem com Filtro da Mediana')

plt.subplot(2, 2, 4)
plt.imshow(gaussiano_image)
plt.axis('off')
plt.title('Imagem com Filtro da Gaussiano')

plt.show()
