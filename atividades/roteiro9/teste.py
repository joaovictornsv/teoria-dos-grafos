from bibgrafo.grafo_matriz_adj_dir import GrafoMatrizAdjacenciaDirecionado
from meu_grafo import *

lic_letras = MeuGrafo(
  [
    '11', '12', '13', '14', '15', '16', '17',
    '21', '22', '23', '24', '25', '26', '27',
    '31', '32', '33', '34', '35', '36', '37',
    '41', '42', '43', '44', '45', '46', '47',
    '51', '52', '53', '54', '55', '56', '57',
    '61', '62', '63', '64', '65', '66', '67', '68',
    '71', '72', '73', '74', '75', '76', '77', '78',
    '81', '82', '83', '84', '85', '86', '87', '88'
  ]
)

lic_letras.adicionaAresta('d1', '11', '21')
lic_letras.adicionaAresta('d3', '11', '22')
lic_letras.adicionaAresta('d5', '12', '23')
lic_letras.adicionaAresta('d8', '12', '25')
lic_letras.adicionaAresta('d8', '17', '26')

lic_letras.adicionaAresta('d9', '21', '31')
lic_letras.adicionaAresta('d10', '21', '32')
lic_letras.adicionaAresta('d10', '21', '33')
lic_letras.adicionaAresta('d11', '24', '34')
lic_letras.adicionaAresta('d12', '25', '35')

lic_letras.adicionaAresta('d13', '31', '41')
lic_letras.adicionaAresta('d14', '33', '42')
lic_letras.adicionaAresta('d15', '25', '43')
lic_letras.adicionaAresta('d16', '25', '44')
lic_letras.adicionaAresta('d17', '36', '44')
lic_letras.adicionaAresta('d171', '23', '46')
lic_letras.adicionaAresta('d172', '35', '46')
lic_letras.adicionaAresta('d173', '37', '47')

lic_letras.adicionaAresta('d18', '31', '51')
lic_letras.adicionaAresta('d19', '35', '52')
lic_letras.adicionaAresta('d20', '13', '53')
lic_letras.adicionaAresta('d21', '45', '54')
lic_letras.adicionaAresta('d22', '35', '55')
lic_letras.adicionaAresta('d23', '22', '56')
lic_letras.adicionaAresta('d26', '43', '57')

lic_letras.adicionaAresta('d27', '31', '61')
lic_letras.adicionaAresta('d28', '31', '62')
lic_letras.adicionaAresta('d30', '35', '63')
lic_letras.adicionaAresta('d32', '54', '64')
lic_letras.adicionaAresta('d34', '37', '67')
lic_letras.adicionaAresta('d35', '54', '68')

lic_letras.adicionaAresta('d36', '31', '71')
lic_letras.adicionaAresta('d37', '31', '72')
lic_letras.adicionaAresta('d39', '31', '73')
lic_letras.adicionaAresta('d40', '64', '74')
lic_letras.adicionaAresta('d41', '35', '75')
lic_letras.adicionaAresta('d51', '45', '76')
lic_letras.adicionaAresta('d52', '27', '77')
lic_letras.adicionaAresta('d53', '53', '77')
lic_letras.adicionaAresta('d54', '64', '78')
lic_letras.adicionaAresta('d55', '68', '78')

lic_letras.adicionaAresta('d44', '17', '83')
lic_letras.adicionaAresta('d45', '74', '84')
lic_letras.adicionaAresta('d48', '77', '87')
lic_letras.adicionaAresta('d49', '74', '88')
lic_letras.adicionaAresta('d50', '78', '88')


print(lic_letras.kahn())

