import unittest
from meu_grafo import *
from bibgrafo.grafo_exceptions import *

class TestGrafo(unittest.TestCase):

    def setUp(self):
        # Grafo da Paraíba
        self.g_p = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p.adicionaAresta('a1', 'J', 'C')
        self.g_p.adicionaAresta('a2', 'C', 'E')
        self.g_p.adicionaAresta('a3', 'C', 'E')
        self.g_p.adicionaAresta('a4', 'P', 'C')
        self.g_p.adicionaAresta('a5', 'P', 'C')
        self.g_p.adicionaAresta('a6', 'T', 'C')
        self.g_p.adicionaAresta('a7', 'M', 'C')
        self.g_p.adicionaAresta('a8', 'M', 'T')
        self.g_p.adicionaAresta('a9', 'T', 'Z')

        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_sem_paralelas.adicionaAresta('a1', 'J', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a2', 'C', 'E')
        self.g_p_sem_paralelas.adicionaAresta('a3', 'P', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a4', 'T', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a5', 'M', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a6', 'M', 'T')
        self.g_p_sem_paralelas.adicionaAresta('a7', 'T', 'Z')

        # Grafos completos
        self.g_c = MeuGrafo(['J', 'C', 'E', 'P'])
        self.g_c.adicionaAresta('a1','J','C')
        self.g_c.adicionaAresta('a2', 'J', 'E')
        self.g_c.adicionaAresta('a3', 'J', 'P')
        self.g_c.adicionaAresta('a4', 'E', 'C')
        self.g_c.adicionaAresta('a5', 'P', 'C')
        self.g_c.adicionaAresta('a6', 'P', 'E')

        self.g_c2 = MeuGrafo(['Nina', 'Maria'])
        self.g_c2.adicionaAresta('amiga', 'Nina', 'Maria')

        self.g_c3 = MeuGrafo(['J'])

        # Grafos com laco
        self.g_l1 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l1.adicionaAresta('a1', 'A', 'A')
        self.g_l1.adicionaAresta('a2', 'A', 'B')
        self.g_l1.adicionaAresta('a3', 'A', 'A')

        self.g_l2 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l2.adicionaAresta('a1', 'A', 'B')
        self.g_l2.adicionaAresta('a2', 'B', 'B')
        self.g_l2.adicionaAresta('a3', 'B', 'A')

        self.g_l3 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l3.adicionaAresta('a1', 'C', 'A')
        self.g_l3.adicionaAresta('a2', 'C', 'C')
        self.g_l3.adicionaAresta('a3', 'D', 'D')
        self.g_l3.adicionaAresta('a4', 'D', 'D')

        self.g_l4 = MeuGrafo(['D'])
        self.g_l4.adicionaAresta('a1', 'D', 'D')

        self.g_l5 = MeuGrafo(['C', 'D'])
        self.g_l5.adicionaAresta('a1', 'D', 'C')
        self.g_l5.adicionaAresta('a2', 'C', 'C')

        # Grafos desconexos
        self.g_d = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_d.adicionaAresta('asd', 'A', 'B')

        # Grafo adicionado por João Victor
        # Grafo com arestas paralelas onde os vértices estão "invertidos"
        # Exemplo: a1=(A-B) e a2=(B-A)
        self.g_a_p = MeuGrafo(['A', 'B'])
        self.g_a_p.adicionaAresta('a1', 'A', 'B')
        self.g_a_p.adicionaAresta('a2', 'B', 'A')


        # Grafos gabaritos DFS
        self.g_p_dfs_J = MeuGrafo(['J', 'C', 'E', 'P', 'T', 'M', 'Z'])
        self.g_p_dfs_J.adicionaAresta('a1', 'J', 'C')
        self.g_p_dfs_J.adicionaAresta('a2', 'C', 'E')
        self.g_p_dfs_J.adicionaAresta('a4', 'P', 'C')
        self.g_p_dfs_J.adicionaAresta('a6', 'T', 'C')
        self.g_p_dfs_J.adicionaAresta('a8', 'M', 'T')
        self.g_p_dfs_J.adicionaAresta('a9', 'T', 'Z')

        self.g_c_dfs_J = MeuGrafo(['J', 'C', 'E', 'P'])
        self.g_c_dfs_J.adicionaAresta('a1', 'J', 'C')
        self.g_c_dfs_J.adicionaAresta('a4', 'E', 'C')
        self.g_c_dfs_J.adicionaAresta('a6', 'P', 'E')

        self.g_a_p_dfs_A = MeuGrafo(['A', 'B'])
        self.g_a_p_dfs_A.adicionaAresta('a1', 'A', 'B')

        self.g_l1_dfs_A = MeuGrafo(['A', 'B'])
        self.g_l1_dfs_A.adicionaAresta('a2', 'A', 'B')
        
        self.g_c2_dfs_Nina = MeuGrafo(['Nina', 'Maria'])
        self.g_c2_dfs_Nina.adicionaAresta('amiga', 'Nina', 'Maria')

        
        self.g_p_sem_paralelas_dfs_J = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_sem_paralelas_dfs_J.adicionaAresta('a1', 'J', 'C')
        self.g_p_sem_paralelas_dfs_J.adicionaAresta('a2', 'C', 'E')
        self.g_p_sem_paralelas_dfs_J.adicionaAresta('a3', 'P', 'C')
        self.g_p_sem_paralelas_dfs_J.adicionaAresta('a4', 'T', 'C')
        self.g_p_sem_paralelas_dfs_J.adicionaAresta('a6', 'M', 'T')
        self.g_p_sem_paralelas_dfs_J.adicionaAresta('a7', 'T', 'Z')

        # Grafos gabaritos BFS
        self.g_p_bfs_J = MeuGrafo(['J', 'C', 'E', 'P', 'T', 'M', 'Z'])
        self.g_p_bfs_J.adicionaAresta('a1', 'J', 'C')
        self.g_p_bfs_J.adicionaAresta('a2', 'C', 'E')
        self.g_p_bfs_J.adicionaAresta('a4', 'P', 'C')
        self.g_p_bfs_J.adicionaAresta('a6', 'T', 'C')
        self.g_p_bfs_J.adicionaAresta('a7', 'M', 'C')
        self.g_p_bfs_J.adicionaAresta('a9', 'T', 'Z')

        self.g_c_bfs_J = MeuGrafo(['J', 'C', 'E', 'P'])
        self.g_c_bfs_J.adicionaAresta('a1','J','C')
        self.g_c_bfs_J.adicionaAresta('a2', 'J', 'E')
        self.g_c_bfs_J.adicionaAresta('a3', 'J', 'P')

        self.g_l1_bfs_A = MeuGrafo(['A', 'B'])
        self.g_l1_bfs_A.adicionaAresta('a2', 'A', 'B')

        self.g_a_p_bfs_A = MeuGrafo(['A', 'B'])
        self.g_a_p_bfs_A.adicionaAresta('a1', 'A', 'B')

        self.g_c2_bfs_Nina = MeuGrafo(['Nina', 'Maria'])
        self.g_c2_bfs_Nina.adicionaAresta('amiga', 'Nina', 'Maria')

        self.g_p_sem_paralelas_bfs_J = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_sem_paralelas_bfs_J.adicionaAresta('a1', 'J', 'C')
        self.g_p_sem_paralelas_bfs_J.adicionaAresta('a2', 'C', 'E')
        self.g_p_sem_paralelas_bfs_J.adicionaAresta('a3', 'P', 'C')
        self.g_p_sem_paralelas_bfs_J.adicionaAresta('a4', 'T', 'C')
        self.g_p_sem_paralelas_bfs_J.adicionaAresta('a5', 'M', 'C')
        self.g_p_sem_paralelas_bfs_J.adicionaAresta('a7', 'T', 'Z')


        # Grafos desconexos
        self.g_desconexo_1 = MeuGrafo(['A', 'B', 'C'])
        self.g_desconexo_1.adicionaAresta('a1', 'A', 'B')

        self.g_desconexo_2 = MeuGrafo(['A', 'B'])


        # Grafos sem ciclo
        self.g_sem_ciclo_1 = MeuGrafo(['A', 'B', 'C'])
        self.g_sem_ciclo_1.adicionaAresta('a1', 'A', 'B')
        self.g_sem_ciclo_1.adicionaAresta('a2', 'B', 'C')

        self.g_sem_ciclo_2 = MeuGrafo(['D', 'E', 'F'])
        self.g_sem_ciclo_2.adicionaAresta('a1', 'D', 'E')
        self.g_sem_ciclo_2.adicionaAresta('a2', 'D', 'F')



    def test_adiciona_aresta(self):
        self.assertTrue(self.g_p.adicionaAresta('a10', 'J', 'C'))
        with self.assertRaises(ArestaInvalidaException):
            self.assertTrue(self.g_p.adicionaAresta('b1', '', 'C'))
        with self.assertRaises(ArestaInvalidaException):
            self.assertTrue(self.g_p.adicionaAresta('b1', 'A', 'C'))
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('')
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('aa-bb')
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('x', 'J', 'V')
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('a1', 'J', 'C')

    def test_vertices_nao_adjacentes(self):
        self.assertEqual(self.g_p.vertices_nao_adjacentes(), ['J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-Z', 'E-P', 'E-M', 'E-T', 'E-Z', 'P-M', 'P-T', 'P-Z', 'M-Z'])
        self.assertEqual(self.g_c.vertices_nao_adjacentes(), [])
        self.assertEqual(self.g_c3.vertices_nao_adjacentes(), [])

    def test_ha_laco(self):
        self.assertFalse(self.g_p.ha_laco())
        self.assertFalse(self.g_p_sem_paralelas.ha_laco())
        self.assertFalse(self.g_c2.ha_laco())
        self.assertTrue(self.g_l1.ha_laco())
        self.assertTrue(self.g_l2.ha_laco())
        self.assertTrue(self.g_l3.ha_laco())
        self.assertTrue(self.g_l4.ha_laco())
        self.assertTrue(self.g_l5.ha_laco())

    def test_grau(self):
        # Paraíba
        self.assertEqual(self.g_p.grau('J'), 1)
        self.assertEqual(self.g_p.grau('C'), 7)
        self.assertEqual(self.g_p.grau('E'), 2)
        self.assertEqual(self.g_p.grau('P'), 2)
        self.assertEqual(self.g_p.grau('M'), 2)
        self.assertEqual(self.g_p.grau('T'), 3)
        self.assertEqual(self.g_p.grau('Z'), 1)
        with self.assertRaises(VerticeInvalidoException):
            self.assertEqual(self.g_p.grau('G'), 5)

        self.assertEqual(self.g_d.grau('A'), 1)
        self.assertEqual(self.g_d.grau('C'), 0)
        self.assertNotEqual(self.g_d.grau('D'), 2)

        # Completos
        self.assertEqual(self.g_c.grau('J'), 3)
        self.assertEqual(self.g_c.grau('C'), 3)
        self.assertEqual(self.g_c.grau('E'), 3)
        self.assertEqual(self.g_c.grau('P'), 3)

        # Com laço. Lembrando que cada laço conta 2 vezes por vértice para cálculo do grau
        self.assertEqual(self.g_l1.grau('A'), 5)
        self.assertEqual(self.g_l2.grau('B'), 4)
        self.assertEqual(self.g_l4.grau('D'), 2)

    def test_ha_paralelas(self):
        self.assertTrue(self.g_p.ha_paralelas())
        self.assertFalse(self.g_p_sem_paralelas.ha_paralelas())
        self.assertFalse(self.g_c.ha_paralelas())
        self.assertFalse(self.g_c2.ha_paralelas())
        self.assertFalse(self.g_c3.ha_paralelas())
        self.assertTrue(self.g_l1.ha_paralelas())

        # Teste adicionado por João Victor
        self.assertTrue(self.g_a_p.ha_paralelas())

    def test_arestas_sobre_vertice(self):
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('J')), set(['a1']))
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('C')), set(['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7']))
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('M')), set(['a7', 'a8']))
        self.assertEqual(set(self.g_l2.arestas_sobre_vertice('B')), set(['a1', 'a2', 'a3']))
        self.assertEqual(set(self.g_d.arestas_sobre_vertice('C')), set())
        self.assertEqual(set(self.g_d.arestas_sobre_vertice('A')), set(['asd']))
        with self.assertRaises(VerticeInvalidoException):
            self.g_p.arestas_sobre_vertice('A')

    def test_eh_completo(self):
        self.assertFalse(self.g_p.eh_completo())
        self.assertFalse((self.g_p_sem_paralelas.eh_completo()))
        self.assertTrue((self.g_c.eh_completo()))
        self.assertTrue((self.g_c2.eh_completo()))
        self.assertTrue((self.g_c3.eh_completo()))
        self.assertFalse((self.g_l1.eh_completo()))
        self.assertFalse((self.g_l2.eh_completo()))
        self.assertFalse((self.g_l3.eh_completo()))
        self.assertFalse((self.g_l4.eh_completo()))
        self.assertFalse((self.g_l5.eh_completo()))

    def test_dfs(self):
        self.assertEqual(self.g_p.dfs('J'), self.g_p_dfs_J)
        self.assertEqual(set(self.g_p.dfs('J').N), set(self.g_p.N[:]))
        self.assertEqual(set(self.g_p.dfs('J').A.keys()), set(['a1', 'a2', 'a4', 'a6', 'a8', 'a9']))

        self.assertEqual(self.g_c.dfs('J'), self.g_c_dfs_J)
        self.assertEqual(set(self.g_c.dfs('J').N), set(self.g_c.N[:]))
        self.assertEqual(set(self.g_c.dfs('J').A.keys()), set(['a1', 'a4', 'a6']))

        self.assertEqual(self.g_c2_dfs_Nina.dfs('Nina'), self.g_c2_dfs_Nina)
        self.assertEqual(set(self.g_c2_dfs_Nina.dfs('Nina').N), set(self.g_c2_dfs_Nina.N[:]))
        self.assertEqual(set(self.g_c2_dfs_Nina.dfs('Nina').A.keys()), set(['amiga']))

        self.assertEqual(self.g_p_sem_paralelas.dfs('J'), self.g_p_sem_paralelas_dfs_J)
        self.assertEqual(set(self.g_p_sem_paralelas.dfs('J').N), set(self.g_p_sem_paralelas.N[:]))
        self.assertEqual(set(self.g_p_sem_paralelas.dfs('J').A.keys()), set(['a1', 'a2', 'a3', 'a4', 'a6', 'a7']))

        self.assertEqual(self.g_a_p.dfs('A'), self.g_a_p_dfs_A)
        self.assertEqual(set(self.g_a_p.dfs('A').N), set(self.g_a_p_dfs_A.N[:]))
        self.assertEqual(set(self.g_a_p.dfs('A').A.keys()), set(['a1']))

        self.assertEqual(self.g_l1.dfs('A'), self.g_l1_dfs_A)
        self.assertEqual(set(self.g_l1.dfs('A').N), set(['A', 'B']))
        self.assertEqual(set(self.g_l1.dfs('A').A.keys()), set(['a2']))

    
    def test_bfs(self):
        self.assertEqual(self.g_p.bfs('J'), self.g_p_bfs_J)
        self.assertEqual(set(self.g_p.bfs('J').N), set(self.g_p.N[:]))
        self.assertEqual(set(self.g_p.bfs('J').A.keys()), set(['a1', 'a2', 'a4', 'a6', 'a7', 'a9']))

        self.assertEqual(self.g_c.bfs('J'), self.g_c_bfs_J)
        self.assertEqual(set(self.g_c.bfs('J').N), set(self.g_c.N[:]))
        self.assertEqual(set(self.g_c.bfs('J').A.keys()), set(['a1', 'a2', 'a3']))

        self.assertEqual(self.g_c2_bfs_Nina.bfs('Nina'), self.g_c2_bfs_Nina)
        self.assertEqual(set(self.g_c2_bfs_Nina.bfs('Nina').N), set(self.g_c2_bfs_Nina.N[:]))
        self.assertEqual(set(self.g_c2_bfs_Nina.bfs('Nina').A.keys()), set(['amiga']))

        self.assertEqual(self.g_p_sem_paralelas.bfs('J'), self.g_p_sem_paralelas_bfs_J)
        self.assertEqual(set(self.g_p_sem_paralelas.bfs('J').N), set(self.g_p_sem_paralelas.N[:]))
        self.assertEqual(set(self.g_p_sem_paralelas.bfs('J').A.keys()), set(['a1', 'a2', 'a3', 'a4', 'a5', 'a7']))

        self.assertEqual(self.g_a_p.bfs('A'), self.g_a_p_bfs_A)
        self.assertEqual(set(self.g_a_p.bfs('A').N), set(self.g_a_p_bfs_A.N[:]))
        self.assertEqual(set(self.g_a_p.bfs('A').A.keys()), set(['a1']))

        self.assertEqual(self.g_l1.bfs('A'), self.g_l1_bfs_A)
        self.assertEqual(set(self.g_l1.bfs('A').N), set(['A', 'B']))
        self.assertEqual(set(self.g_l1.bfs('A').A.keys()), set(['a2']))

    
    def test_caminho_dois_vertices(self):
        self.assertTrue(self.g_p.caminho_dois_vertices('J', 'M')[0])
        self.assertTrue(self.g_p.caminho_dois_vertices('J', 'M')[1] == 2)

        self.assertTrue(self.g_c.caminho_dois_vertices('J', 'E')[0])
        self.assertTrue(self.g_c.caminho_dois_vertices('J', 'E')[1] == 1)

        self.assertTrue(self.g_desconexo_1.caminho_dois_vertices('A', 'B')[0])
        self.assertTrue(self.g_desconexo_1.caminho_dois_vertices('A', 'B')[1] == 1)

        self.assertFalse(self.g_desconexo_1.caminho_dois_vertices('A', 'C')[0])
        self.assertTrue(self.g_desconexo_1.caminho_dois_vertices('A', 'C')[1] == 0)

        self.assertFalse(self.g_desconexo_2.caminho_dois_vertices('A', 'B')[0])
        self.assertTrue(self.g_desconexo_2.caminho_dois_vertices('A', 'B')[1] == 0)

        self.assertTrue(self.g_a_p.caminho_dois_vertices('A', 'B')[0])
        self.assertTrue(self.g_a_p.caminho_dois_vertices('A', 'B')[1] == 1)

    
    def test_conexo(self):
        self.assertTrue(self.g_p.conexo())
        self.assertTrue(self.g_c.conexo())
        self.assertTrue(self.g_a_p.conexo())

        self.assertFalse(self.g_desconexo_1.conexo())
        self.assertFalse(self.g_desconexo_2.conexo())
        self.assertFalse(self.g_d.conexo())

    
    def test_caminho(self):
        self.assertListEqual(self.g_c.caminho(3), ['J', 'a1', 'C', 'a4', 'E', 'a6', 'P'])
        self.assertListEqual(self.g_c.caminho(2), ['J', 'a1', 'C', 'a4', 'E'])
        self.assertListEqual(self.g_c.caminho(1), ['J', 'a1', 'C'])

        self.assertListEqual(self.g_p.caminho(3), ['J', 'a1', 'C', 'a6', 'T', 'a8', 'M'])
        self.assertListEqual(self.g_p.caminho(2), ['J', 'a1', 'C', 'a2', 'E'])
        self.assertListEqual(self.g_p.caminho(1), ['J', 'a1', 'C'])

        self.assertListEqual(self.g_p_sem_paralelas.caminho(3), ['J', 'a1', 'C', 'a4', 'T', 'a6', 'M'])
        self.assertListEqual(self.g_p_sem_paralelas.caminho(2), ['J', 'a1', 'C', 'a2', 'E'])
        self.assertListEqual(self.g_p_sem_paralelas.caminho(1), ['J', 'a1', 'C'])


    def test_ha_ciclo(self):
        self.assertListEqual(self.g_p.ha_ciclo(), ['C', 'a2', 'E', 'a3', 'C'])
        self.assertListEqual(self.g_p_sem_paralelas.ha_ciclo(), ['C', 'a4', 'T', 'a6', 'M', 'a5', 'C'])
        self.assertListEqual(self.g_c.ha_ciclo(), ['J', 'a1', 'C', 'a4', 'E', 'a2', 'J'])
        self.assertListEqual(self.g_a_p.ha_ciclo(), ['A', 'a1', 'B', 'a2', 'A'])
        self.assertListEqual(self.g_l1.ha_ciclo(), ['A', 'a1', 'A'])
        self.assertListEqual(self.g_a_p.ha_ciclo(), ['A', 'a1', 'B', 'a2', 'A'])

        self.assertFalse(self.g_desconexo_1.ha_ciclo())
        self.assertFalse(self.g_desconexo_2.ha_ciclo())
        self.assertFalse(self.g_sem_ciclo_1.ha_ciclo())
        self.assertFalse(self.g_sem_ciclo_2.ha_ciclo())