from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from meu_grafo import *

g_l1 = MeuGrafo(['A', 'B', 'C', 'D'])
g_l1.adicionaAresta('a1', 'A', 'B')
g_l1.adicionaAresta('a2', 'B', 'C')
g_l1.adicionaAresta('a3', 'C', 'D')
g_l1.adicionaAresta('a4', 'D', 'A')
g_l1.adicionaAresta('a5', 'A', 'C')


final = g_l1.caminho_euleriano()
print(final)