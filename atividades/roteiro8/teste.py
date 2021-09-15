from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from meu_grafo import *

grafo = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'])
grafo.adicionaAresta('a1', 'A', 'B', 4)
grafo.adicionaAresta('a2', 'B', 'C', 8)
grafo.adicionaAresta('a3', 'C', 'D', 7)
grafo.adicionaAresta('a4', 'D', 'E', 9)
grafo.adicionaAresta('a5', 'E', 'F', 10)
grafo.adicionaAresta('a6', 'F', 'G', 2)
grafo.adicionaAresta('a7', 'G', 'H', 1)
grafo.adicionaAresta('a8', 'H', 'A', 8)
grafo.adicionaAresta('a9', 'H', 'B', 11)
grafo.adicionaAresta('a10', 'H', 'I', 7)
grafo.adicionaAresta('a12', 'I', 'G', 6)
grafo.adicionaAresta('a13', 'I', 'C', 2)
grafo.adicionaAresta('a14', 'C', 'F', 4)
grafo.adicionaAresta('a15', 'F', 'D', 14)

print(grafo.kruskal_modified())
