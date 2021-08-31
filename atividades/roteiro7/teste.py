from bibgrafo.grafo_matriz_adj_dir import GrafoMatrizAdjacenciaDirecionado
from meu_grafo import *

g_p = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
g_p.adicionaAresta('a1', 'J', 'C')
g_p.adicionaAresta('a2', 'C', 'E')
g_p.adicionaAresta('a3', 'E', 'C')
g_p.adicionaAresta('a4', 'P', 'C')
g_p.adicionaAresta('a5', 'C', 'P')
g_p.adicionaAresta('a6', 'C', 'T')
g_p.adicionaAresta('a7', 'M', 'C')
g_p.adicionaAresta('a8', 'M', 'T')
g_p.adicionaAresta('a9', 'T', 'Z')

print(g_p.dijkstra('J', 'Z'))

