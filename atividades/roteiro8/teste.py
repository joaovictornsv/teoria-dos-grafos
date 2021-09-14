from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from meu_grafo import *

grafo = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
grafo.adicionaAresta('a1', 'A', 'B', 1)
grafo.adicionaAresta('a2', 'B', 'C', 2)
grafo.adicionaAresta('a3', 'C', 'G', 2)
grafo.adicionaAresta('a4', 'G', 'F', 3)
grafo.adicionaAresta('a5', 'E', 'F', 4)
grafo.adicionaAresta('a6', 'E', 'G', 1)
grafo.adicionaAresta('a7', 'E', 'D', 2)
grafo.adicionaAresta('a8', 'A', 'D', 3)
grafo.adicionaAresta('a9', 'B', 'G', 5)
grafo.adicionaAresta('a10', 'D', 'G', 3)
print(grafo.kruskal())
