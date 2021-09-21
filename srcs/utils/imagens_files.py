import numpy as np
import matplotlib.image as im


def file_to_matriz(nome_file: str) -> np.array:
    matriz_colorida = im.imread(nome_file)
    matriz_8bit = matriz_colorida * 255
    matriz_8bit = matriz_8bit.astype(np.uint8)
    return matriz_8bit


