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


        # Grafos para prim e kruskal
        self.g_pk1 = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
        self.g_pk1.adicionaAresta('a1', 'A', 'B', 1)
        self.g_pk1.adicionaAresta('a2', 'B', 'C', 2)
        self.g_pk1.adicionaAresta('a3', 'C', 'G', 2)
        self.g_pk1.adicionaAresta('a4', 'G', 'F', 3)
        self.g_pk1.adicionaAresta('a5', 'E', 'F', 4)
        self.g_pk1.adicionaAresta('a6', 'E', 'G', 1)
        self.g_pk1.adicionaAresta('a7', 'E', 'D', 2)
        self.g_pk1.adicionaAresta('a8', 'A', 'D', 3)
        self.g_pk1.adicionaAresta('a9', 'B', 'G', 5)
        self.g_pk1.adicionaAresta('a10', 'D', 'G', 3)

        self.g_pk1_gabarito = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
        self.g_pk1_gabarito.adicionaAresta('a1', 'A', 'B', 1)
        self.g_pk1_gabarito.adicionaAresta('a2', 'B', 'C', 2)
        self.g_pk1_gabarito.adicionaAresta('a3', 'C', 'G', 2)
        self.g_pk1_gabarito.adicionaAresta('a4', 'G', 'F', 3)
        self.g_pk1_gabarito.adicionaAresta('a6', 'E', 'G', 1)
        self.g_pk1_gabarito.adicionaAresta('a7', 'E', 'D', 2)

        self.g_pk2 = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
        self.g_pk2.adicionaAresta('a1', 'A', 'B', 7)
        self.g_pk2.adicionaAresta('a2', 'B', 'C', 8)
        self.g_pk2.adicionaAresta('a3', 'C', 'E', 5)
        self.g_pk2.adicionaAresta('a4', 'E', 'G', 9)
        self.g_pk2.adicionaAresta('a5', 'G', 'F', 11)
        self.g_pk2.adicionaAresta('a6', 'F', 'D', 6)
        self.g_pk2.adicionaAresta('a7', 'D', 'A', 5)
        self.g_pk2.adicionaAresta('a8', 'B', 'D', 9)
        self.g_pk2.adicionaAresta('a9', 'D', 'E', 15)
        self.g_pk2.adicionaAresta('a10', 'B', 'E', 7)
        self.g_pk2.adicionaAresta('a11', 'F', 'E', 8)

        self.g_pk2_gabarito = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
        self.g_pk2_gabarito.adicionaAresta('a1', 'A', 'B', 7)
        self.g_pk2_gabarito.adicionaAresta('a3', 'C', 'E', 5)
        self.g_pk2_gabarito.adicionaAresta('a4', 'E', 'G', 9)
        self.g_pk2_gabarito.adicionaAresta('a6', 'F', 'D', 6)
        self.g_pk2_gabarito.adicionaAresta('a7', 'D', 'A', 5)
        self.g_pk2_gabarito.adicionaAresta('a10', 'B', 'E', 7)

        self.g_pk3 = MeuGrafo(['0', '1', '2', '3', '4', '5'])
        self.g_pk3.adicionaAresta('a1', '1', '0', 1)
        self.g_pk3.adicionaAresta('a2', '0', '2', 5)
        self.g_pk3.adicionaAresta('a3', '2', '4', 2)
        self.g_pk3.adicionaAresta('a4', '4', '5', 4)
        self.g_pk3.adicionaAresta('a5', '5', '3', 2)
        self.g_pk3.adicionaAresta('a6', '3', '1', 5)
        self.g_pk3.adicionaAresta('a7', '1', '2', 2)
        self.g_pk3.adicionaAresta('a8', '1', '4', 2)
        self.g_pk3.adicionaAresta('a9', '3', '4', 1)

        self.g_pk3_gabarito = MeuGrafo(['0', '1', '2', '3', '4', '5'])
        self.g_pk3_gabarito.adicionaAresta('a1', '1', '0', 1)
        self.g_pk3_gabarito.adicionaAresta('a3', '2', '4', 2)
        self.g_pk3_gabarito.adicionaAresta('a5', '5', '3', 2)
        self.g_pk3_gabarito.adicionaAresta('a7', '1', '2', 2)
        self.g_pk3_gabarito.adicionaAresta('a9', '3', '4', 1)

        self.g_pk4 = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F'])
        self.g_pk4.adicionaAresta('a1', 'A', 'B', 4)
        self.g_pk4.adicionaAresta('a2', 'B', 'C', 8)
        self.g_pk4.adicionaAresta('a3', 'C', 'D', 2)
        self.g_pk4.adicionaAresta('a4', 'D', 'E', 6)
        self.g_pk4.adicionaAresta('a5', 'E', 'F', 1)
        self.g_pk4.adicionaAresta('a6', 'F', 'A', 8)
        self.g_pk4.adicionaAresta('a7', 'B', 'F', 11)
        self.g_pk4.adicionaAresta('a8', 'F', 'D', 7)

        self.g_pk4_gabarito = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F'])
        self.g_pk4_gabarito.adicionaAresta('a1', 'A', 'B', 4)
        self.g_pk4_gabarito.adicionaAresta('a2', 'B', 'C', 8)
        self.g_pk4_gabarito.adicionaAresta('a3', 'C', 'D', 2)
        self.g_pk4_gabarito.adicionaAresta('a4', 'D', 'E', 6)
        self.g_pk4_gabarito.adicionaAresta('a5', 'E', 'F', 1)

        self.g_pk5 = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F'])
        self.g_pk5.adicionaAresta('a1', 'A', 'B', 6)
        self.g_pk5.adicionaAresta('a2', 'B', 'E', 3)
        self.g_pk5.adicionaAresta('a3', 'E', 'F', 6)
        self.g_pk5.adicionaAresta('a4', 'F', 'D', 2)
        self.g_pk5.adicionaAresta('a5', 'D', 'A', 5)
        self.g_pk5.adicionaAresta('a6', 'C', 'A', 1)
        self.g_pk5.adicionaAresta('a7', 'C', 'B', 5)
        self.g_pk5.adicionaAresta('a8', 'C', 'D', 5)
        self.g_pk5.adicionaAresta('a9', 'C', 'E', 6)
        self.g_pk5.adicionaAresta('a10', 'C', 'F', 4)

        self.g_pk5_gabarito = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F'])
        self.g_pk5_gabarito.adicionaAresta('a2', 'B', 'E', 3)
        self.g_pk5_gabarito.adicionaAresta('a4', 'F', 'D', 2)
        self.g_pk5_gabarito.adicionaAresta('a6', 'C', 'A', 1)
        self.g_pk5_gabarito.adicionaAresta('a7', 'C', 'B', 5)
        self.g_pk5_gabarito.adicionaAresta('a10', 'C', 'F', 4)

        self.g_pk6 = MeuGrafo(['0', '1', '2', '3', '4', '5'])
        self.g_pk6.adicionaAresta('a1', '0', '1', 6)
        self.g_pk6.adicionaAresta('a2', '1', '4', 5)
        self.g_pk6.adicionaAresta('a3', '4', '5', 3)
        self.g_pk6.adicionaAresta('a4', '5', '3', 4)
        self.g_pk6.adicionaAresta('a5', '3', '0', 5)
        self.g_pk6.adicionaAresta('a6', '2', '0', 1)
        self.g_pk6.adicionaAresta('a7', '2', '1', 2)
        self.g_pk6.adicionaAresta('a8', '2', '3', 2)
        self.g_pk6.adicionaAresta('a9', '2', '4', 6)
        self.g_pk6.adicionaAresta('a10', '2', '5', 4)

        self.g_pk6_gabarito = MeuGrafo(['0', '1', '2', '3', '4', '5'])
        self.g_pk6_gabarito.adicionaAresta('a3', '4', '5', 3)
        self.g_pk6_gabarito.adicionaAresta('a4', '5', '3', 4)
        self.g_pk6_gabarito.adicionaAresta('a6', '2', '0', 1)
        self.g_pk6_gabarito.adicionaAresta('a7', '2', '1', 2)
        self.g_pk6_gabarito.adicionaAresta('a8', '2', '3', 2)

        self.g_pk7 = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'])
        self.g_pk7.adicionaAresta('a1', 'A', 'B', 4)
        self.g_pk7.adicionaAresta('a2', 'B', 'C', 8)
        self.g_pk7.adicionaAresta('a3', 'C', 'D', 7)
        self.g_pk7.adicionaAresta('a4', 'D', 'E', 9)
        self.g_pk7.adicionaAresta('a5', 'E', 'F', 10)
        self.g_pk7.adicionaAresta('a6', 'F', 'G', 2)
        self.g_pk7.adicionaAresta('a7', 'G', 'H', 1)
        self.g_pk7.adicionaAresta('a8', 'H', 'A', 8)
        self.g_pk7.adicionaAresta('a9', 'H', 'B', 11)
        self.g_pk7.adicionaAresta('a10', 'H', 'I', 7)
        self.g_pk7.adicionaAresta('a12', 'I', 'G', 6)
        self.g_pk7.adicionaAresta('a13', 'I', 'C', 2)
        self.g_pk7.adicionaAresta('a14', 'C', 'F', 4)
        self.g_pk7.adicionaAresta('a15', 'F', 'D', 14)

        self.g_pk7_gabarito = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'])
        self.g_pk7_gabarito.adicionaAresta('a1', 'A', 'B', 4)
        self.g_pk7_gabarito.adicionaAresta('a2', 'B', 'C', 8)
        self.g_pk7_gabarito.adicionaAresta('a3', 'C', 'D', 7)
        self.g_pk7_gabarito.adicionaAresta('a4', 'D', 'E', 9)
        self.g_pk7_gabarito.adicionaAresta('a6', 'F', 'G', 2)
        self.g_pk7_gabarito.adicionaAresta('a7', 'G', 'H', 1)
        self.g_pk7_gabarito.adicionaAresta('a13', 'I', 'C', 2)
        self.g_pk7_gabarito.adicionaAresta('a14', 'C', 'F', 4)


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

    
    
    def test_caminho_dois_vertices(self):
        self.assertTrue(self.g_p.caminho_dois_vertices('J', 'M')[0])
        self.assertTrue(self.g_p.caminho_dois_vertices('J', 'M')[1] == 2)

        self.assertTrue(self.g_c.caminho_dois_vertices('J', 'E')[0])
        self.assertTrue(self.g_c.caminho_dois_vertices('J', 'E')[1] == 1)

        self.assertTrue(self.g_a_p.caminho_dois_vertices('A', 'B')[0])
        self.assertTrue(self.g_a_p.caminho_dois_vertices('A', 'B')[1] == 1)


    def test_kruskal_modified(self):
        self.assertEqual(self.g_pk1.kruskal_modified(), self.g_pk1_gabarito)
        self.assertEqual(self.g_pk2.kruskal_modified(), self.g_pk2_gabarito)
        self.assertEqual(self.g_pk3.kruskal_modified(), self.g_pk3_gabarito)
        self.assertEqual(self.g_pk4.kruskal_modified(), self.g_pk4_gabarito)
        self.assertEqual(self.g_pk5.kruskal_modified(), self.g_pk5_gabarito)
        self.assertEqual(self.g_pk6.kruskal_modified(), self.g_pk6_gabarito)
        self.assertEqual(self.g_pk7.kruskal_modified(), self.g_pk7_gabarito)


    def test_prim_modified(self):
        self.assertEqual(self.g_pk1.prim_modified(), self.g_pk1_gabarito)
        self.assertEqual(self.g_pk2.prim_modified(), self.g_pk2_gabarito)
        self.assertEqual(self.g_pk3.prim_modified(), self.g_pk3_gabarito)
        self.assertEqual(self.g_pk4.prim_modified(), self.g_pk4_gabarito)
        self.assertEqual(self.g_pk5.prim_modified(), self.g_pk5_gabarito)
        self.assertEqual(self.g_pk6.prim_modified(), self.g_pk6_gabarito)
        self.assertEqual(self.g_pk7.prim_modified(), self.g_pk7_gabarito)