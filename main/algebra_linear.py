from typing import List

Vector = List[float]

def add(v: Vector, w: Vector) -> Vector:
    """Adds corresponding elements"""
    
    assert len(v) == len(w), "Os vetores apresentam tamanhos diferentes"
    return [v_i + w_i for v_i, w_i in zip(v, w)] # combinando os elementos em tuplas e somando eles

assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9], "erro na adicao"


def subtract(v: Vector, w: Vector) -> Vector:
    """Subtracts corresponding elements"""

    assert len(v) == len(w), "vetores apresenta tamanhos diferentes"
    return [v_i - w_i for v_i, w_i in zip(v, w)]

assert subtract([5, 7, 9], [4, 5, 6]) ==  [1, 2, 3]


def vector_sum(vectors: List[Vector]) -> Vector:
    """ sum of vectors """

    assert vectors, "no provided vectors"

    # verifica se todos os vetores apresentam o mesmo tamanho
    num_elements = len(vectors[0]) 
    assert all(len(v) ==  num_elements for v in vectors), "tamanhos diferentes"

    # Realizo a soma de cada coordenada do vetor para gerar o vetor resultante
    return [sum(vector[i] for vector in vectors)
           for i in range(num_elements)]

assert vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]


def scalar_multiply(c: float, v: Vector) -> Vector:
    """Multiplies every element by c"""
    return [c* v_i for v_i in v]

assert scalar_multiply(2, [1, 2, 3]) == [2, 4, 6]


def vector_mean(vectors: List[Vector]) -> Vector:
    """ Retorna o vetor medio, calculando a media das coordenadas para os vetores envolvidos """
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

assert vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4]

def dot(v: Vector, w: Vector) -> float:
    """ calcula o produto interno de vetores: v_1 * w_1 + ... + v_n * w_n """

    assert len(v) == len(w), "Não possuem mesmo tamanho"
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

assert dot([1, 2, 3], [4, 5, 6]) == 32 # 1*4 + 2*5 + 3*6

def sum_of_squares(v: Vector) -> float:
    """Retorna v_1 * v_1 + ... + v_n * v_n = v²"""

    return dot(v, v)

assert sum_of_squares([1, 2, 3]) == 14 

import math

def magnitude(v: Vector) -> float:
    """retorna a maginitude ou tamanho do vetor """

    return math.sqrt(sum_of_squares(v)) 
assert magnitude([3, 4]) == 5

def squared_distance(v: Vector, w: Vector) -> float:
    """Calcula entre dois vetores: (v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2"""

    return sum_of_squares(subtract(v, w))

def distance(v: Vector, w: Vector) -> float:
    """ Utiliza a função squared_dist para calcular a distance entre dois vetores """
    
    return math.sqrt(squared_distance(v, w))

def distance(v: Vector, w: Vector) -> float:
    return magnitude(subtract(v, w))




## Trabalhando com Matrizes

Matrix = List[List[float]]

A = [[1, 2, 3],  # A: 2 linhas e 3 colunas
     [4, 5, 6]]

B = [[1, 2],     # B: 3 linhas e 2 colunas
     [3, 4],
     [5, 6]]

from typing import Tuple

def shape(A: Matrix) -> Tuple[int, int]:
    """ retorna o numero de linhas e colunas da matriz """

    num_rows = len(A)
    num_colums = len(A[0])
    return num_rows, num_colums

assert shape([[1, 2, 3], [4, 5, 6]]) == (2, 3)  # 2 rows, 3 columns

def get_row(A: Matrix, i:int) -> Matrix:
    """ retorna a linha i da matriz """

    return A[i]

def get_column(A: Matrix, j:int) -> Matrix:
    """ retorna a a coluna correspondente a linha j da matriz """

    return [A_i[j] for A_i in A]

from typing import Callable

def make_matrix(num_row,
               num_columns,
               entry_fn: Callable[[int, int], float]) -> Matrix:

        return [
            [entry_fn(i, j)           
             for j in range(num_columns)]  
             for i in range(num_row)
        ]   

def identity_matrix(n: int) -> Matrix:
    """ Retorna uma matriz identidade n x n """

    return make_matrix(n, n, lambda i, j: 1 if i == j else 0)

assert identity_matrix(3) == [[1, 0, 0], 
                              [0, 1, 0],
                              [0, 0, 1]]
