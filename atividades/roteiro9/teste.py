from bibgrafo.grafo_matriz_adj_dir import GrafoMatrizAdjacenciaDirecionado
from meu_grafo import *

lic_fisica = MeuGrafo(
  [
    '11', '12', '13', '14', '15', '16', '17',
    '21', '22', '23', '24', '25', '26', '27',
    '31', '32', '33', '34', '35', '36', '37',
    '41', '42', '43', '44', '45', '46',
    '51', '52', '53', '54', '55', '56', '57',
    '61', '62', '63', '64', '65', '66', '68',
    '71', '72', '73', '74', '76',
    '81', '82', '83', '84', '85', '86'
  ]
)

lic_fisica.adicionaAresta('d1', '11', '21')
lic_fisica.adicionaAresta('d2', '12', '21')
lic_fisica.adicionaAresta('d3', '11', '22')
lic_fisica.adicionaAresta('d4', '12', '22')
lic_fisica.adicionaAresta('d5', '12', '23')
lic_fisica.adicionaAresta('d6', '12', '24')
lic_fisica.adicionaAresta('d7', '14', '24')
lic_fisica.adicionaAresta('d8', '15', '25')

lic_fisica.adicionaAresta('d9', '21', '31')
lic_fisica.adicionaAresta('d10', '23', '31')
lic_fisica.adicionaAresta('d10', '21', '31')
lic_fisica.adicionaAresta('d11', '22', '32')
lic_fisica.adicionaAresta('d12', '23', '33')

lic_fisica.adicionaAresta('d13', '31', '41')
lic_fisica.adicionaAresta('d14', '31', '42')
lic_fisica.adicionaAresta('d15', '32', '42')
lic_fisica.adicionaAresta('d16', '33', '45')
lic_fisica.adicionaAresta('d17', '31', '46')

lic_fisica.adicionaAresta('d18', '41', '51')
lic_fisica.adicionaAresta('d19', '45', '51')
lic_fisica.adicionaAresta('d20', '41', '52')
lic_fisica.adicionaAresta('d21', '42', '52')
lic_fisica.adicionaAresta('d22', '45', '53')
lic_fisica.adicionaAresta('d23', '31', '54')
lic_fisica.adicionaAresta('d24', '43', '55')
lic_fisica.adicionaAresta('d25', '21', '57')
lic_fisica.adicionaAresta('d26', '43', '57')

lic_fisica.adicionaAresta('d27', '51', '61')
lic_fisica.adicionaAresta('d28', '51', '62')
lic_fisica.adicionaAresta('d29', '52', '62')
lic_fisica.adicionaAresta('d30', '21', '63')
lic_fisica.adicionaAresta('d31', '53', '63')
lic_fisica.adicionaAresta('d32', '51', '64')
lic_fisica.adicionaAresta('d33', '56', '66')
lic_fisica.adicionaAresta('d34', '31', '68')
lic_fisica.adicionaAresta('d35', '57', '68')

lic_fisica.adicionaAresta('d36', '61', '71')
lic_fisica.adicionaAresta('d37', '41', '72')
lic_fisica.adicionaAresta('d38', '45', '72')
lic_fisica.adicionaAresta('d39', '66', '73')
lic_fisica.adicionaAresta('d40', '31', '74')
lic_fisica.adicionaAresta('d41', '43', '74')
lic_fisica.adicionaAresta('d51', '41', '76')
lic_fisica.adicionaAresta('d52', '68', '76')

lic_fisica.adicionaAresta('d42', '65', '81')
lic_fisica.adicionaAresta('d43', '74', '82')
lic_fisica.adicionaAresta('d44', '73', '83')
lic_fisica.adicionaAresta('d45', '54', '84')
lic_fisica.adicionaAresta('d46', '71', '84')
lic_fisica.adicionaAresta('d47', '16', '85')
lic_fisica.adicionaAresta('d48', '25', '85')
lic_fisica.adicionaAresta('d49', '51', '86')
lic_fisica.adicionaAresta('d50', '76', '86')



print(lic_fisica.kahn())

