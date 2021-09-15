from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from meu_grafo import *

grafo = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F'])
grafo.adicionaAresta('a1', 'A', 'B', 4)
grafo.adicionaAresta('a2', 'B', 'C', 8)
grafo.adicionaAresta('a3', 'C', 'D', 2)
grafo.adicionaAresta('a4', 'D', 'E', 6)
grafo.adicionaAresta('a5', 'E', 'F', 1)
grafo.adicionaAresta('a6', 'F', 'A', 8)
grafo.adicionaAresta('a7', 'B', 'F', 11)
grafo.adicionaAresta('a8', 'F', 'D', 7)

print(grafo.kruskal_modified())
