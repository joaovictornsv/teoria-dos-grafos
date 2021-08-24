from bibgrafo.grafo_matriz_adj_dir import GrafoMatrizAdjacenciaDirecionado
from bibgrafo.grafo_exceptions import *
from copy import deepcopy
from time import sleep

class MeuGrafo(GrafoMatrizAdjacenciaDirecionado):
    def clone_matriz(self):
        matriz_clone = deepcopy(self.M)

        return matriz_clone

    def clone_grafo(self):
        grafo_clone = deepcopy(self)

        return grafo_clone


    def warshall(self):
        matriz_copia = self.clone_matriz()
        tamanho_matriz = len(matriz_copia)
        
        matriz_copia_uns_e_zeros = deepcopy(matriz_copia)
        
        for i in range(tamanho_matriz):
            for j in range(tamanho_matriz):
                if len(matriz_copia_uns_e_zeros[j][i]) >= 1:
                    matriz_copia_uns_e_zeros[j][i] = 1
                else:
                    matriz_copia_uns_e_zeros[j][i] = 0

        matriz_alcancabilidade = deepcopy(matriz_copia_uns_e_zeros)

        for i in range(tamanho_matriz):
            for j in range(tamanho_matriz):
                if matriz_alcancabilidade[j][i] == 1:
                    for k in range(tamanho_matriz):
                        item_jk = matriz_alcancabilidade[j][k]
                        item_ik = matriz_alcancabilidade[i][k]

                        if item_jk >= item_ik:
                            matriz_alcancabilidade[j][k] = item_jk

                        elif item_jk < item_ik:
                            matriz_alcancabilidade[j][k] = item_ik

        return matriz_alcancabilidade
