from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_exceptions import *
from copy import deepcopy
from time import sleep
from math import floor

class MeuGrafo(GrafoListaAdjacencia):

    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''
        vertices_nao_adjacentes = []

        for v in self.N:
            vertices_adjacentes = []
            for a in self.A:
                v1 = self.A[a].getV1()
                v2 = self.A[a].getV2()
                if v1 == v:
                    vertices_adjacentes.append(v2)
                elif v2 == v:
                    vertices_adjacentes.append(v1)

            for vt in self.N:
                if vt != v and vt not in vertices_adjacentes:
                    a_test_1 = f'{v}-{vt}'
                    a_test_2 = f'{vt}-{v}'
                    if a_test_1 not in vertices_nao_adjacentes and a_test_2 not in vertices_nao_adjacentes:
                        vertices_nao_adjacentes.append(f'{v}-{vt}')

            vertices_adjacentes = []

        return vertices_nao_adjacentes

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        for a in self.A:
            if self.A[a].getV1() == self.A[a].getV2():
                return True

        return False


    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''


        vertices_adjacentes = []

        verticeExiste = False

        for vt in self.N:
            if vt == V:
                verticeExiste = True
                vertices_adjacentes = []
                for a in self.A:
                    v1 = self.A[a].getV1()
                    v2 = self.A[a].getV2()
                    if v1 == vt:
                        vertices_adjacentes.append(v2)
                    if v2 == vt:
                        vertices_adjacentes.append(v1)

        if len(vertices_adjacentes) == 0 and verticeExiste == False:
            raise VerticeInvalidoException('O vértice ' + V + ' não existe no grafo')
        else:
            return len(vertices_adjacentes)



    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        
        for a1 in self.A:
            v1_a1 = self.A[a1].getV1()
            v2_a1 = self.A[a1].getV2()
            
            a1_str = f'{v1_a1}-{v2_a1}'
            a1_str_swap = f'{v2_a1}-{v1_a1}'

            for a2 in self.A:
                if a1 != a2:
                    v1_a2 = self.A[a2].getV1()
                    v2_a2 = self.A[a2].getV2()
                    a2_str = f'{v1_a2}-{v2_a2}'
                    a2_str_swap = f'{v2_a2}-{v1_a2}'

                    if a1_str == a2_str or a1_str == a2_str_swap or a2_str == a1_str_swap:
                        return True

        return False

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        arestas_adjacentes = []

        verticeExiste = False

        for vt in self.N:
            if vt == V:
                verticeExiste = True
                for a in self.A:
                    v1 = self.A[a].getV1()
                    v2 = self.A[a].getV2()
                    if v1 == vt or v2 == vt:
                        if a not in arestas_adjacentes:
                            arestas_adjacentes.append(a)

        if len(arestas_adjacentes) == 0 and verticeExiste == False:
            raise VerticeInvalidoException('O vértice ' + V + ' não existe no grafo')
        else:
            return arestas_adjacentes


    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        if self.ha_laco() or self.ha_paralelas():
            return False

        else:
            totalVertices = len(self.N)
            for v in self.N:
                if self.grau((v)) == totalVertices-1:
                    continue
                else:
                    return False

            return True


    

    def caminho_dois_vertices(self, x, y):
        '''
        Realiza uma verificação se existe um caminho entre os dois vértices passados nos parâmetros
        :return: Uma lista contendo um valor booleano que representa se existe caminho ou não,
        e o tamanho do caminho (caso exista)

        Exemplo:
        grafo.caminho_dois_vertices('x', 'y')
        :return: [true, 4]
        '''
        finalizada = False

        vertices_examinados = {}

        for vt in self.N:
            vertices_examinados[vt] = {
                'examinado': False,
                'root': False,
                'pai': False,
                'temPai': False,
                'arestaPai': ''
            }

        vertices_examinados[x] = {
            'examinado': True,
            'root': True,
            'pai': x,
            'temPai': True,
            'arestaPai': ''
        }
        

        vertice_atual = x
        vertice_final = y
        comeco = True   

        existeCaminho = False
        tamanhoCaminho = 0
        fila_vertices = []

        while (finalizada == False):
            arestas_incidentes = self.arestas_sobre_vertice(vertice_atual)
            if len(arestas_incidentes) == 0:
                finalizada = True
                break
            
            for a in arestas_incidentes:
                v1 = self.A[a].getV1()
                v2 = self.A[a].getV2()
                if v1 == vertice_atual:
                    if not vertices_examinados[v2]['temPai']:
                        vertices_examinados[v2]['pai'] = v1
                        vertices_examinados[v2]['temPai'] = True
                        vertices_examinados[v2]['arestaPai'] = a

                    if vertices_examinados[v2]['examinado'] == False and v2 not in fila_vertices:
                        fila_vertices.append(v2)

                if v2 == vertice_atual:
                    if not vertices_examinados[v1]['temPai']:
                        vertices_examinados[v1]['pai'] = v2
                        vertices_examinados[v1]['temPai'] = True
                        vertices_examinados[v1]['arestaPai'] = a

                    if vertices_examinados[v1]['examinado'] == False and v1 not in fila_vertices:
                        fila_vertices.append(v1)

                if vertice_atual == y:
                    finalizada = True
                    existeCaminho = True
                    break

            vertices_examinados[vertice_atual]['examinado'] = True

            

            if vertices_examinados[vertice_atual]['root'] == False:
                v_pai = vertices_examinados[vertice_atual]['pai']
                aresta_do_pai = vertices_examinados[vertice_atual]['arestaPai']



            if vertice_atual in fila_vertices:
               fila_vertices.remove(vertice_atual)
               if len(fila_vertices) == 0:
                   finalizada = True
                   break
            
            
            vertice_atual = fila_vertices[0]

        
        lista_final = []
        if (existeCaminho):
            lista_preenchida = False
            lista_aux = []
            v_atual = vertice_final
            while(not lista_preenchida):
                if v_atual == x:
                    lista_preenchida = True
                    break
                lista_aux.append(vertices_examinados[v_atual]['arestaPai'])
                v_atual = vertices_examinados[v_atual]['pai']

            for i in range(len(lista_aux)-1, -1, -1):
                lista_final.append(lista_aux[i])


        return [existeCaminho, len(lista_final)]



    def vertice_menor_peso(self):
        grafo_copia = deepcopy(self)
        arestas = list(grafo_copia.A.keys())

        aresta_menor_peso = arestas[0]
        for i in arestas:
            if (grafo_copia.A[i].getPeso() < grafo_copia.A[aresta_menor_peso].getPeso()):
                aresta_menor_peso = i

        return [
            grafo_copia.A[aresta_menor_peso].getV1(),
            grafo_copia.A[aresta_menor_peso].getV2(),
            aresta_menor_peso,
            grafo_copia.A[aresta_menor_peso].getPeso()
        ]


    def aresta_menor_peso(self, dict_arestas):
        arestas = list(dict_arestas.keys())

        aresta_menor_peso = arestas[0]
        for i in arestas:
            if (dict_arestas[i].getPeso() < dict_arestas[aresta_menor_peso].getPeso()):
                aresta_menor_peso = i

        return aresta_menor_peso

    
    def prim_modified(self):
        grafo_copia = deepcopy(self)
        arestas = list(grafo_copia.A.keys())
        vertices = deepcopy(grafo_copia.N)


        v1, v2, a, p = grafo_copia.vertice_menor_peso()
        
        # pis = {}
        # for v in vertices:
        #     pis[v] = NULL

        grafo_prim = MeuGrafo([v1, v2])
        grafo_prim.adicionaAresta(a, v1, v2, p)
        vertices_analisados = []

        fim_algoritmo = False
        
        arestas_para_ignorar = []

        while(not fim_algoritmo):
            vertices_na_arvore = grafo_prim.N
            vertices_nao_estao_na_arvore = []

            for v in vertices:
                if v not in vertices_na_arvore:
                    vertices_nao_estao_na_arvore.append(v)

            if len(vertices_nao_estao_na_arvore) == 0:
                fim_algoritmo = True
                break


            arestas_adjacentes_a_arvore = []
            for v in vertices_na_arvore:
                arestas_sobre_v = grafo_copia.arestas_sobre_vertice(v)
                for a in arestas_sobre_v:
                    if a not in arestas_adjacentes_a_arvore:
                        arestas_adjacentes_a_arvore.append(a)



            arestas_fora_da_arvore = {}

            for aresta in list(grafo_copia.A.keys()):
                if aresta not in list(grafo_prim.A.keys()):
                    if aresta in arestas_adjacentes_a_arvore:
                        if aresta not in arestas_para_ignorar:
                            arestas_fora_da_arvore[aresta] = deepcopy(grafo_copia.A[aresta])
            
            aresta_menor_peso = grafo_copia.aresta_menor_peso(arestas_fora_da_arvore)

            v1 = grafo_copia.A[aresta_menor_peso].getV1()
            v2 = grafo_copia.A[aresta_menor_peso].getV2()

            if v1 not in grafo_prim.N:
                grafo_prim.adicionaVertice(v1)
                grafo_prim.adicionaAresta(aresta_menor_peso, v2, v1, grafo_copia.A[aresta_menor_peso].getPeso())
            else:
                if v2 not in grafo_prim.N:
                    grafo_prim.adicionaVertice(v2)
                    grafo_prim.adicionaAresta(aresta_menor_peso, v1, v2, grafo_copia.A[aresta_menor_peso].getPeso())
                arestas_para_ignorar.append(aresta_menor_peso)


        return grafo_prim
                

                
    def ordenar_arestas(self, dict_arestas):
        arestas = list(dict_arestas.keys())

        arestas_ordenadas = []

        finalizou_ordenacao = False
        while(not finalizou_ordenacao):
            aresta_menor_peso = dict_arestas[arestas[0]]
            index_aresta_menor_peso = 0
            for i in range(len(arestas)):
                if (dict_arestas[arestas[i]].getPeso() < aresta_menor_peso.getPeso()):
                    aresta_menor_peso = dict_arestas[arestas[i]]
                    index_aresta_menor_peso = i
                    arestas_ordenadas.append(aresta_menor_peso)
                    break
            
            if aresta_menor_peso == dict_arestas[arestas[0]]: arestas_ordenadas.append(aresta_menor_peso)
            del arestas[index_aresta_menor_peso]
            if len(arestas) == 0:
                finalizou_ordenacao = True
                break

        return arestas_ordenadas

    def kruskal(self):
        grafo_copia = deepcopy(self)
        vertices = deepcopy(grafo_copia.N)
        arestas_ordenadas = grafo_copia.ordenar_arestas(grafo_copia.A)
        arvores = {}
        for v in vertices:
            arvores[v] = MeuGrafo([v])

        minimum_spanning_tree = MeuGrafo()

        fim_algoritmo = False
        while(not fim_algoritmo):
            aresta_para_deletar = ''

            for a in range(len(arestas_ordenadas)):
                v1 = arestas_ordenadas[a].getV1()
                v2 = arestas_ordenadas[a].getV2()

                arvores_existentes = list(arvores.keys())

                adicionou = False

                aresta_para_deletar = a

                for avs in arvores_existentes:

                    if v1 in arvores[avs].N and v2 in arvores[avs].N:
                        continue
                    
                    elif v1 in arvores[avs].N and v2 not in arvores[avs].N:
                        arvores[avs].adicionaVertice(v2)
                        if v2 not in minimum_spanning_tree.N:
                            minimum_spanning_tree.adicionaVertice(v2)
                        if v1 not in minimum_spanning_tree.N:
                            minimum_spanning_tree.adicionaVertice(v1)
                        arvores[avs].adicionaAresta(arestas_ordenadas[a].getRotulo(), v1, v2, arestas_ordenadas[a].getPeso())
                        minimum_spanning_tree.adicionaAresta(arestas_ordenadas[a].getRotulo(), v1, v2, arestas_ordenadas[a].getPeso())

                        adicionou = True
                        arvore_alterada = v2

                        if arvore_alterada not in list(arvores.keys()):
                            for arvs in list(arvores.keys()):
                                if arvs != avs and arvore_alterada in arvores[arvs].N:
                                    arvore_alterada = arvs
                                    break
                        
                        for vertice_arvore_alterada in arvores[arvore_alterada].N:
                            if vertice_arvore_alterada not in arvores[avs].N:
                                arvores[avs].adicionaVertice(vertice_arvore_alterada)

                        for aresta_arvore_alterada in list(arvores[arvore_alterada].A.keys()):
                            if aresta_arvore_alterada not in list(arvores[avs].A.keys()):
                                arvores[avs].adicionaAresta(
                                    arvores[arvore_alterada].A[aresta_arvore_alterada].getRotulo(),
                                    arvores[arvore_alterada].A[aresta_arvore_alterada].getV1(),
                                    arvores[arvore_alterada].A[aresta_arvore_alterada].getV2(),
                                    arvores[arvore_alterada].A[aresta_arvore_alterada].getPeso(),
                                )

                        break

                    
                    elif v2 in arvores[avs].N and v1 not in arvores[avs].N:
                        arvores[avs].adicionaVertice(v1)
                        if v2 not in minimum_spanning_tree.N:
                            minimum_spanning_tree.adicionaVertice(v2)
                        if v1 not in minimum_spanning_tree.N:
                            minimum_spanning_tree.adicionaVertice(v1)

                        arvores[avs].adicionaAresta(arestas_ordenadas[a].getRotulo(), v1, v2, arestas_ordenadas[a].getPeso())
                        minimum_spanning_tree.adicionaAresta(arestas_ordenadas[a].getRotulo(), v1, v2, arestas_ordenadas[a].getPeso())

                        adicionou = True
                        arvore_alterada = v1

                        if arvore_alterada not in list(arvores.keys()):
                            for arvs in list(arvores.keys()):
                                if arvs != avs and arvore_alterada in arvores[arvs].N:
                                    arvore_alterada = arvs
                                    break
                        
                        for vertice_arvore_alterada in arvores[arvore_alterada].N:
                            if vertice_arvore_alterada not in arvores[avs].N:
                                arvores[avs].adicionaVertice(vertice_arvore_alterada)

                        for aresta_arvore_alterada in list(arvores[arvore_alterada].A.keys()):
                            if aresta_arvore_alterada not in list(arvores[avs].A.keys()):
                                arvores[avs].adicionaAresta(
                                    arvores[arvore_alterada].A[aresta_arvore_alterada].getRotulo(),
                                    arvores[arvore_alterada].A[aresta_arvore_alterada].getV1(),
                                    arvores[arvore_alterada].A[aresta_arvore_alterada].getV2(),
                                    arvores[arvore_alterada].A[aresta_arvore_alterada].getPeso(),
                                )

                        break


                    elif v1 not in arvores[avs].N and v2 not in arvores[avs].N:
                        continue

                if arvore_alterada in list(arvores.keys()): del arvores[arvore_alterada]
                if adicionou: break
                    
                 

            arestas_ordenadas.pop(aresta_para_deletar)
            if len(arestas_ordenadas) == 0:
                fim_algoritmo = True
                break

        
        return minimum_spanning_tree


    def criar_baldes_de_arestas(self, qtd_baldes: int):
        grafo_copia = deepcopy(self)
        lista_de_arestas = grafo_copia.ordenar_arestas(grafo_copia.A)

        baldes = []
        for i in range(qtd_baldes):
            baldes.append([])

        menor_peso = 0
        maior_peso = 0
        for aresta in lista_de_arestas:
            if aresta.getPeso() < menor_peso:
                menor_peso = aresta.getPeso()
            if aresta.getPeso() > maior_peso:
                maior_peso = aresta.getPeso()


        def selecionaBalde(peso: int):
            balde = floor((peso - menor_peso)/(maior_peso - menor_peso)*(qtd_baldes - 2) + 1)
            return balde


        for aresta in lista_de_arestas:
            balde_para_adicionar = selecionaBalde(aresta.getPeso())
            baldes[balde_para_adicionar].append(aresta)

        return baldes



    def kruskal_modified(self):
            grafo_copia = deepcopy(self)
            vertices = deepcopy(grafo_copia.N)
            baldes_de_arestas = grafo_copia.criar_baldes_de_arestas(8)

            arvores = {}
            for v in vertices:
                arvores[v] = MeuGrafo([v])

            minimum_spanning_tree = MeuGrafo()

            fim_algoritmo = False
            aresta_para_deletar = ''


            for balde in baldes_de_arestas:
                baldeVazio = False
                if len(balde) == 0:
                    baldeVazio = True
                
                while(not baldeVazio):
                    for a in range(len(balde)):
                        v1 = balde[a].getV1()
                        v2 = balde[a].getV2()

                        arvores_existentes = list(arvores.keys())

                        adicionou = False

                        aresta_para_deletar = a

                        for avs in arvores_existentes:

                            if v1 in arvores[avs].N and v2 in arvores[avs].N:
                                continue
                            
                            elif v1 in arvores[avs].N and v2 not in arvores[avs].N:
                                arvores[avs].adicionaVertice(v2)
                                if v2 not in minimum_spanning_tree.N:
                                    minimum_spanning_tree.adicionaVertice(v2)
                                if v1 not in minimum_spanning_tree.N:
                                    minimum_spanning_tree.adicionaVertice(v1)
                                arvores[avs].adicionaAresta(balde[a].getRotulo(), v1, v2, balde[a].getPeso())
                                minimum_spanning_tree.adicionaAresta(balde[a].getRotulo(), v1, v2, balde[a].getPeso())

                                adicionou = True
                                arvore_alterada = v2

                                if arvore_alterada not in list(arvores.keys()):
                                    for arvs in list(arvores.keys()):
                                        if arvs != avs and arvore_alterada in arvores[arvs].N:
                                            arvore_alterada = arvs
                                            break
                                
                                for vertice_arvore_alterada in arvores[arvore_alterada].N:
                                    if vertice_arvore_alterada not in arvores[avs].N:
                                        arvores[avs].adicionaVertice(vertice_arvore_alterada)

                                for aresta_arvore_alterada in list(arvores[arvore_alterada].A.keys()):
                                    if aresta_arvore_alterada not in list(arvores[avs].A.keys()):
                                        arvores[avs].adicionaAresta(
                                            arvores[arvore_alterada].A[aresta_arvore_alterada].getRotulo(),
                                            arvores[arvore_alterada].A[aresta_arvore_alterada].getV1(),
                                            arvores[arvore_alterada].A[aresta_arvore_alterada].getV2(),
                                            arvores[arvore_alterada].A[aresta_arvore_alterada].getPeso(),
                                        )

                                break

                            
                            elif v2 in arvores[avs].N and v1 not in arvores[avs].N:
                                arvores[avs].adicionaVertice(v1)
                                if v2 not in minimum_spanning_tree.N:
                                    minimum_spanning_tree.adicionaVertice(v2)
                                if v1 not in minimum_spanning_tree.N:
                                    minimum_spanning_tree.adicionaVertice(v1)

                                arvores[avs].adicionaAresta(balde[a].getRotulo(), v1, v2, balde[a].getPeso())
                                minimum_spanning_tree.adicionaAresta(balde[a].getRotulo(), v1, v2, balde[a].getPeso())

                                adicionou = True
                                arvore_alterada = v1

                                if arvore_alterada not in list(arvores.keys()):
                                    for arvs in list(arvores.keys()):
                                        if arvs != avs and arvore_alterada in arvores[arvs].N:
                                            arvore_alterada = arvs
                                            break
                                
                                for vertice_arvore_alterada in arvores[arvore_alterada].N:
                                    if vertice_arvore_alterada not in arvores[avs].N:
                                        arvores[avs].adicionaVertice(vertice_arvore_alterada)

                                for aresta_arvore_alterada in list(arvores[arvore_alterada].A.keys()):
                                    if aresta_arvore_alterada not in list(arvores[avs].A.keys()):
                                        arvores[avs].adicionaAresta(
                                            arvores[arvore_alterada].A[aresta_arvore_alterada].getRotulo(),
                                            arvores[arvore_alterada].A[aresta_arvore_alterada].getV1(),
                                            arvores[arvore_alterada].A[aresta_arvore_alterada].getV2(),
                                            arvores[arvore_alterada].A[aresta_arvore_alterada].getPeso(),
                                        )

                                break


                            elif v1 not in arvores[avs].N and v2 not in arvores[avs].N:
                                continue

                        if arvore_alterada in list(arvores.keys()): del arvores[arvore_alterada]
                        if adicionou: break
                    

                    balde.pop(aresta_para_deletar)
                    if len(balde) == 0:
                        baldeVazio = True
                        break
            
            return minimum_spanning_tree