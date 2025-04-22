#Trabalhando com Matrizes em Python
#Matrizes podem ser representadas como listas de listas, onde cada sublista é uma linha da mastriz

#Criando uma Matriz
matriz = [
    [1, 2, 3], # Primeira linha
    [4, 5, 6]  # Segunda linha
]
# Matriz 2x3 (2 linhas e 3 colunas)

#Acessando elementos de uma matriz 

print(matriz [0][1]) # Acessa o elemento da linha 0, coluna 1 (Saída: 2)
print(matriz [1][0]) # Acessa o elemento da linha 1, coluna 0 (Saída: 4)

#Alterando um valor da matriz
matriz [0][1] = 10
print(matriz) # Saída: [[1, 10, 3]], [4, 5, 6]

#Iterando sobre matriz (linha por linha)
for linha in matriz:
    print (linha)

#iterando sobre todos os elementos da matriz (indice linha e coluna)
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(f"Elemento ({i},{j}):{matriz[i][j]}")

#Criando uma matriz de zeros (3x3)
matriz_zero = [[0 for _ in range (3)] for _ in range (3)]
print(matriz_zero) 

#Transpondo uma matriz (trocando linhas por colunas)
transposta = [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]
print(transposta)  

#Criando uma matriz com NumPy
import numpy as np
matriz_np = np.array([[1, 2, 3,], [4, 5, 6]])
print(matriz_np)

#acessando um elemento com NumPy
print (matriz_np[0, 1])

#Funções úteis com NumPy:
#Somando duas matrizes
matriz_sum = matriz_np + matriz_np
print (matriz_sum)

matriz_mult = matriz_np * 2
print (matriz_mult)

"""Observação> Matrizes em Python são geralmente representadas como listas de listas,
mas para operações matemáticas eficientes, a blibioteca NumPY e altamente recomendada"""