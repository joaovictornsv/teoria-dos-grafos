from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from meu_grafo import *

grafo = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
grafo.adicionaAresta('a1', 'A', 'B', 7)
grafo.adicionaAresta('a2', 'B', 'C', 8)
grafo.adicionaAresta('a3', 'C', 'E', 5)
grafo.adicionaAresta('a4', 'E', 'G', 9)
grafo.adicionaAresta('a5', 'G', 'F', 11)
grafo.adicionaAresta('a6', 'F', 'D', 6)
grafo.adicionaAresta('a7', 'D', 'A', 5)
grafo.adicionaAresta('a8', 'B', 'D', 9)
grafo.adicionaAresta('a9', 'D', 'E', 15)
grafo.adicionaAresta('a10', 'B', 'E', 7)
grafo.adicionaAresta('a11', 'F', 'E', 8)
print(grafo.prim_modified())
