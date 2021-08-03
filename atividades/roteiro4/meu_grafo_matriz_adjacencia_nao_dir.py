from bibgrafo.grafo_matriz_adj_nao_dir import GrafoMatrizAdjacenciaNaoDirecionado
from bibgrafo.grafo_exceptions import *


class MeuGrafo(GrafoMatrizAdjacenciaNaoDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''
        lista_nao_adjacentes = []

        for i in range(len(self.M)):
          for j in range(len(self.M)):
            if j > i:
              if len(self.M[i][j]) == 0:
                teste_dupla1 = f'{self.N[i]}-{self.N[j]}'
                teste_dupla2 = f'{self.N[j]}-{self.N[i]}'
                if teste_dupla1 not in lista_nao_adjacentes and teste_dupla2 not in lista_nao_adjacentes:
                  lista_nao_adjacentes.append(f'{self.N[i]}-{self.N[j]}')

        return lista_nao_adjacentes



    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        for i in range(len(self.M)):
          if len(self.M[i][i]) > 0:
            return True
        
        return False


    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        vertice_index = 0
        if V in self.N:
          vertice_index = self.N.index(V)
        else:
          raise VerticeInvalidoException(f'\'{V}\' is not in list')

        grau = 0
        for i in range(len(self.M)):
          if i < vertice_index:
            grau += len(self.M[i][vertice_index])

          if i == vertice_index:
            grau += len(self.M[i][vertice_index]) * 2

          if i > vertice_index:
            grau += len(self.M[vertice_index][i])

        return grau


    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        for i in range(len(self.M)):
          for j in range(len(self.M)):
            if j >= i:
              if len(self.M[i][j]) > 1:
                
                return True

        return False



    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        vertice_index = 0
        if V in self.N:
          vertice_index = self.N.index(V)
        else:
          raise VerticeInvalidoException(f'\'{V}\' is not in list')

        lista_arestas_incidentes = []
        for i in range(len(self.M)):
          if i <= vertice_index:
            if len(self.M[i][vertice_index]) > 0:
              for k in self.M[i][vertice_index].keys():
                if k not in lista_arestas_incidentes:
                  lista_arestas_incidentes.append(k)
          
          if i > vertice_index:
            if len(self.M[vertice_index][i]) > 0:
              for k in self.M[vertice_index][i].keys():
                if k not in lista_arestas_incidentes:
                  lista_arestas_incidentes.append(k)


        return lista_arestas_incidentes


    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        return self.grau(self.N[0]) == (len(self.N) - 1)

