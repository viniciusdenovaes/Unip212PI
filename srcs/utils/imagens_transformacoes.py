import numpy as np


def imagem_to_cinza(matrix_colorida: np.array) -> np.array:
    linhas = matrix_colorida.shape[0]
    colunas = matrix_colorida.shape[1]

    matrix_gray = np.zeros((linhas, colunas))

    for i in range(linhas):
        for j in range(colunas):
            r, g, b = matrix_colorida[i, j]
            matrix_gray[i, j] = int((r + g + b) / 3)

    return matrix_gray


