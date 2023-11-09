    #Importando bibliotecas

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import cv2

    #Importando a imagem do computador

from google.colab import files
uploaded = files.upload()

    #Carregando a imagem

image_path = 'gatinhos1.jpg';
image = cv2.imread(image_path);

    #Convertendo BGR para RGB

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    #Exibindo a imagem

plt.imshow(image_rgb)
plt.axis('off')
plt.show()

    #Buscando e exibindo dados da imagem

if image is not None:
  height, width, channels = image.shape

  for i in range(3):
    pixel = image[i, i]
    print(f'Pixel {i + 1}: Valor BGR: {pixel}')

    properties = [
        ('Altura', image.shape[0]),
        ('Largura', image.shape[1]),
        ('Canais de Cor', image.shape[2]),
        ('Tipo de Dado', image.dtype),
        ('Máximo tom de cinza', image.max()),
        ('Médio tom de cinza', image.mean()),
        ('Mínimo tom de cinza', image.min())
    ]

  for prop_name, prop_values in properties:
    print(f"{prop_name} : {prop_values}")

