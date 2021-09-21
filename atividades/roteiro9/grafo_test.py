import unittest
from meu_grafo import *
from bibgrafo.grafo_exceptions import *

class TestGrafo(unittest.TestCase):

    def setUp(self):
        # Grafo do curso de Engenharia de Computação
        self.eng_comp = MeuGrafo(["11", "12", "13", "14", "15","16", "17",
                      "21", "22", "23","24", "25", "26", "27",
                      "31", "32", "33", "34", "35", "36",
                      "41", "42", "43", "44", "45",
                      "51", "52", "53", "54", "55",
                      "61", "62", "63", "64", "65",
                      "71", "72", "73", "74", "75",
                      "81", "82", "83", "84", "85",
                      "91", "92", "93", "94",
                      "101", "102", "103"])

        self.eng_comp.adicionaAresta("d1", "11", "21")
        self.eng_comp.adicionaAresta("d2", "14", "24")
        self.eng_comp.adicionaAresta("d3", "14", "25")
        self.eng_comp.adicionaAresta("d4", "14", "34")
        self.eng_comp.adicionaAresta("d5", "14", "35")
        self.eng_comp.adicionaAresta("d6", "15", "24")
        self.eng_comp.adicionaAresta("d7", "15", "25")
        self.eng_comp.adicionaAresta("d8", "15", "34")
        self.eng_comp.adicionaAresta("d9", "15", "35")
        self.eng_comp.adicionaAresta("d10", "16", "26")
        self.eng_comp.adicionaAresta("d11", "21", "31")
        self.eng_comp.adicionaAresta("d12", "21", "41")
        self.eng_comp.adicionaAresta("d13", "24", "33")
        self.eng_comp.adicionaAresta("d14", "24", "43")
        self.eng_comp.adicionaAresta("d15", "24", "44")
        self.eng_comp.adicionaAresta("d16", "24", "53")
        self.eng_comp.adicionaAresta("d17", "24", "54")
        self.eng_comp.adicionaAresta("d18", "24", "72")
        self.eng_comp.adicionaAresta("d19", "26", "36")
        self.eng_comp.adicionaAresta("d20", "31", "51")
        self.eng_comp.adicionaAresta("d21", "31", "52")
        self.eng_comp.adicionaAresta("d22", "31", "64")
        self.eng_comp.adicionaAresta("d23", "34", "63")
        self.eng_comp.adicionaAresta("d24", "35", "63")
        self.eng_comp.adicionaAresta("d25", "34", "81")
        self.eng_comp.adicionaAresta("d26", "35", "81")
        self.eng_comp.adicionaAresta("d27", "36", "44")
        self.eng_comp.adicionaAresta("d28", "36", "45")
        self.eng_comp.adicionaAresta("d29", "36", "55")
        self.eng_comp.adicionaAresta("d30", "43", "62")
        self.eng_comp.adicionaAresta("d31", "44", "55")
        self.eng_comp.adicionaAresta("d32", "44", "93")
        self.eng_comp.adicionaAresta("d33", "45", "93")
        self.eng_comp.adicionaAresta("d34", "51", "61")
        self.eng_comp.adicionaAresta("d35", "52", "75")
        self.eng_comp.adicionaAresta("d36", "54", "81")
        self.eng_comp.adicionaAresta("d37", "55", "65")
        self.eng_comp.adicionaAresta("d38", "61", "84")
        self.eng_comp.adicionaAresta("d39", "61", "94")
        self.eng_comp.adicionaAresta("d40", "63", "73")
        self.eng_comp.adicionaAresta("d41", "64", "75")
        self.eng_comp.adicionaAresta("d42", "64", "84")
        self.eng_comp.adicionaAresta("d43", "73", "82")
        self.eng_comp.adicionaAresta("d44", "74", "83")
        self.eng_comp.adicionaAresta("d45", "75", "85")
        self.eng_comp.adicionaAresta("d46", "75", "94")
        self.eng_comp.adicionaAresta("d47", "83", "92")
        self.eng_comp.adicionaAresta("d48", "92", "103")
        self.eng_comp_gabarito = ['11', '12', '13', '14', 
        '15', '16', '17', '22', '23', '27', '32', '42', '71', '74', '91', '101', '102', 
        '21', '24', '25', '26', '34', '35', '83', '31', '33', '36', '41', '43', '53', 
        '54', '63', '72', '92', '44', '45', '51', '52', '62', '64', '73', '81', '103', 
        '55', '61', '75', '82', '93', '65', '84', '85', '94']

        # Grafo do curso de Construção de Edifícios
        self.construcao_edif = MeuGrafo([
            '11', '12', '13', '14', '15', '16', '17', '18',
            '21', '22', '23', '24', '25', '26', '27',
            '31', '32', '33', '34', '35', '36', '37', '38',
            '41', '42', '43', '44', '45', '46', '47',
            '51', '52', '53', '54', '55', '56', '57', '58',
            '61', '62', '63', '64', '65', '66', '67', '68',
            '71', '72', '73'])

        self.construcao_edif.adicionaAresta('d1', '15', '21')
        self.construcao_edif.adicionaAresta('d2', '14', '23')
        self.construcao_edif.adicionaAresta('d3', '11', '24')
        self.construcao_edif.adicionaAresta('d4', '17', '24')
        self.construcao_edif.adicionaAresta('d5', '15', '25')
        self.construcao_edif.adicionaAresta('d6', '17', '26')
        self.construcao_edif.adicionaAresta('d7', '17', '27')
        self.construcao_edif.adicionaAresta('d8', '15', '32')
        self.construcao_edif.adicionaAresta('d9', '21', '32')
        self.construcao_edif.adicionaAresta('d10', '21', '33')
        self.construcao_edif.adicionaAresta('d11', '25', '33')
        self.construcao_edif.adicionaAresta('d12', '15', '34')
        self.construcao_edif.adicionaAresta('d13', '11', '35')
        self.construcao_edif.adicionaAresta('d14', '27', '35')
        self.construcao_edif.adicionaAresta('d15', '26', '36')
        self.construcao_edif.adicionaAresta('d16', '23', '37')
        self.construcao_edif.adicionaAresta('d17', '24', '38')
        self.construcao_edif.adicionaAresta('d18', '17', '41')
        self.construcao_edif.adicionaAresta('d29', '21', '41')
        self.construcao_edif.adicionaAresta('d20', '17', '42')
        self.construcao_edif.adicionaAresta('d21', '21', '42')
        self.construcao_edif.adicionaAresta('d22', '23', '43')
        self.construcao_edif.adicionaAresta('d23', '24', '44')
        self.construcao_edif.adicionaAresta('d24', '36', '45')
        self.construcao_edif.adicionaAresta('d25', '37', '45')
        self.construcao_edif.adicionaAresta('d26', '17', '46')
        self.construcao_edif.adicionaAresta('d27', '32', '46')
        self.construcao_edif.adicionaAresta('d28', '11', '47')
        self.construcao_edif.adicionaAresta('d29', '37', '47')
        self.construcao_edif.adicionaAresta('d30', '37', '51')
        self.construcao_edif.adicionaAresta('d31', '43', '51')
        self.construcao_edif.adicionaAresta('d32', '45', '51')
        self.construcao_edif.adicionaAresta('d33', '46', '51')
        self.construcao_edif.adicionaAresta('d34', '41', '52')
        self.construcao_edif.adicionaAresta('d35', '42', '52')
        self.construcao_edif.adicionaAresta('d36', '45', '52')
        self.construcao_edif.adicionaAresta('d37', '46', '52')
        self.construcao_edif.adicionaAresta('d38', '17', '53')
        self.construcao_edif.adicionaAresta('d39', '32', '53')
        self.construcao_edif.adicionaAresta('d40', '47', '54')
        self.construcao_edif.adicionaAresta('d41', '17', '55')
        self.construcao_edif.adicionaAresta('d42', '32', '55')
        self.construcao_edif.adicionaAresta('d43', '46', '56')
        self.construcao_edif.adicionaAresta('d44', '43', '57')
        self.construcao_edif.adicionaAresta('d45', '31', '62')
        self.construcao_edif.adicionaAresta('d46', '44', '62')
        self.construcao_edif.adicionaAresta('d47', '22', '64')
        self.construcao_edif.adicionaAresta('d48', '27', '64')
        self.construcao_edif.adicionaAresta('d49', '33', '64')
        self.construcao_edif.adicionaAresta('d50', '36', '64')
        self.construcao_edif.adicionaAresta('d51', '47', '65')
        self.construcao_edif.adicionaAresta('d52', '22', '66')
        self.construcao_edif.adicionaAresta('d53', '31', '67')

        self.construcao_edif_gabarito = [
            '11', '12', '13', '14', '15', '16', '17',
            '18', '22', '31', '58', '61', '63', '68',
            '71', '72', '73', '21', '23', '24', '25',
            '26', '27', '34', '66', '67', '32', '33',
            '35', '36', '37', '38', '41', '42', '43',
            '44', '45', '46', '47', '53', '55', '57',
            '62', '64', '51', '52', '54', '56', '65']

        # Grafo do curso de Telemátia
        self.telematica = MeuGrafo([
            '11','12','13','14','15','16','17',
            '21','22','23','24','25','26','27',
            '31','32','33','34','35','36','37',
            '41','42','43','44','45','46','47',
            '51','52','53','54','55','56',
            '61','62','63','64','65'
        ])

        self.telematica.adicionaAresta('d1', '11', '21')
        self.telematica.adicionaAresta('d2', '12', '22')
        self.telematica.adicionaAresta('d3', '16', '22')
        self.telematica.adicionaAresta('d4', '12', '23')
        self.telematica.adicionaAresta('d5', '16', '23')
        self.telematica.adicionaAresta('d6', '13', '24')
        self.telematica.adicionaAresta('d7', '16', '26')
        self.telematica.adicionaAresta('d8', '21', '31')
        self.telematica.adicionaAresta('d9', '26', '32')
        self.telematica.adicionaAresta('d10', '22', '33')
        self.telematica.adicionaAresta('d11', '23', '33')
        self.telematica.adicionaAresta('d12', '26', '33')
        self.telematica.adicionaAresta('d13', '14', '34')
        self.telematica.adicionaAresta('d14', '25', '35')
        self.telematica.adicionaAresta('d15', '21', '36')
        self.telematica.adicionaAresta('d16', '24', '36')
        self.telematica.adicionaAresta('d17', '31', '41')
        self.telematica.adicionaAresta('d18', '31', '42')
        self.telematica.adicionaAresta('d19', '32', '43')
        self.telematica.adicionaAresta('d20', '32', '44')
        self.telematica.adicionaAresta('d21', '33', '44')
        self.telematica.adicionaAresta('d22', '33', '45')
        self.telematica.adicionaAresta('d23', '21', '46')
        self.telematica.adicionaAresta('d24', '34', '46')
        self.telematica.adicionaAresta('d25', '41', '51')
        self.telematica.adicionaAresta('d26', '41', '52')
        self.telematica.adicionaAresta('d27', '44', '53')
        self.telematica.adicionaAresta('d28', '44', '54')
        self.telematica.adicionaAresta('d29', '37', '55')
        self.telematica.adicionaAresta('d30', '41', '55')
        self.telematica.adicionaAresta('d31', '44', '55')
        self.telematica.adicionaAresta('d32', '42', '61')
        self.telematica.adicionaAresta('d33', '51', '61')
        self.telematica.adicionaAresta('d34', '53', '62')

        self.telematica_gabarito = [
            '11', '12', '13', '14', '15', '16', '17',
            '25', '27', '37', '47', '56', '63', '64',
            '65', '21', '22', '23', '24', '26', '34',
            '35', '31', '32', '33', '36', '46', '41',
            '42', '43', '44', '45', '51', '52', '53',
            '54', '55', '61', '62']

        # Grafo do curso de Licenciatura em Matemática
        self.lic_matematica = MeuGrafo(["11", "12", "13", "14", "15","16", "17",
              "21", "22", "23","24", "25", "26", "27",
              "31", "32", "33", "34", "35", "36",
              "41", "42", "43", "44", "45", "46",
              "51", "52", "53", "54", "55", "56","57",
              "61", "62", "63", "64", "65", "66","67",
              "71", "72", "73", "74", "75", "77",
              "81", "82", "83", "84", "85", "87"])


        self.lic_matematica.adicionaAresta("d1", "11", "21")
        self.lic_matematica.adicionaAresta("d2", "11", "22")
        self.lic_matematica.adicionaAresta("d3", "13", "22")
        self.lic_matematica.adicionaAresta("d4", "16", "26")
        self.lic_matematica.adicionaAresta("d5", "21", "31")
        self.lic_matematica.adicionaAresta("d6", "22", "32")
        self.lic_matematica.adicionaAresta("d7", "12", "33")
        self.lic_matematica.adicionaAresta("d8", "12", "34")
        self.lic_matematica.adicionaAresta("d9", "21", "41")
        self.lic_matematica.adicionaAresta("d10", "23", "41")
        self.lic_matematica.adicionaAresta("d11", "23", "42")
        self.lic_matematica.adicionaAresta("d12", "32", "42")
        self.lic_matematica.adicionaAresta("d13", "36", "43")
        self.lic_matematica.adicionaAresta("d14", "34", "44")
        self.lic_matematica.adicionaAresta("d15", "27", "45")
        self.lic_matematica.adicionaAresta("d16", "33", "51")
        self.lic_matematica.adicionaAresta("d17", "12", "52")
        self.lic_matematica.adicionaAresta("d18", "32", "53")
        self.lic_matematica.adicionaAresta("d19", "44", "54")
        self.lic_matematica.adicionaAresta("d20", "44", "55")
        self.lic_matematica.adicionaAresta("d21", "44", "57")
        self.lic_matematica.adicionaAresta("d22", "51", "61")
        self.lic_matematica.adicionaAresta("d23", "52", "62")
        self.lic_matematica.adicionaAresta("d24", "32", "63")
        self.lic_matematica.adicionaAresta("d25", "54", "64")
        self.lic_matematica.adicionaAresta("d26", "46", "65")
        self.lic_matematica.adicionaAresta("d27", "57", "67")
        self.lic_matematica.adicionaAresta("d28", "42", "71")
        self.lic_matematica.adicionaAresta("d29", "22", "72")
        self.lic_matematica.adicionaAresta("d30", "41", "73")
        self.lic_matematica.adicionaAresta("d31", "42", "73")
        self.lic_matematica.adicionaAresta("d32", "64", "74")
        self.lic_matematica.adicionaAresta("d33", "65", "75")
        self.lic_matematica.adicionaAresta("d34", "67", "77")
        self.lic_matematica.adicionaAresta("d35", "62", "81")
        self.lic_matematica.adicionaAresta("d36", "75", "82")
        self.lic_matematica.adicionaAresta("d37", "32", "83")
        self.lic_matematica.adicionaAresta("d38", "74", "84")
        self.lic_matematica.adicionaAresta("d39", "77", "87")

        self.lic_matematica_gabarito = ['11', '12', '13', 
        '14', '15', '16', '17', '23', '24', '25', '27', '35', '36', '46', '56', '66', 
        '85', '21', '22', '26', '33', '34', '43', '45', '52', '65', '31', '32', '41', 
        '44', '51', '62', '72', '75', '42', '53', '54', '55', '57', '61', '63', '81', 
        '82', '83', '64', '67', '71', '73', '74', '77', '84', '87']


        # Grafo do curso de Licenciatura em Física
        self.lic_fisica = MeuGrafo(
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

        self.lic_fisica.adicionaAresta('d1', '11', '21')
        self.lic_fisica.adicionaAresta('d2', '12', '21')
        self.lic_fisica.adicionaAresta('d3', '11', '22')
        self.lic_fisica.adicionaAresta('d4', '12', '22')
        self.lic_fisica.adicionaAresta('d5', '12', '23')
        self.lic_fisica.adicionaAresta('d6', '12', '24')
        self.lic_fisica.adicionaAresta('d7', '14', '24')
        self.lic_fisica.adicionaAresta('d8', '15', '25')
        self.lic_fisica.adicionaAresta('d9', '21', '31')
        self.lic_fisica.adicionaAresta('d10', '23', '31')
        self.lic_fisica.adicionaAresta('d10', '21', '31')
        self.lic_fisica.adicionaAresta('d11', '22', '32')
        self.lic_fisica.adicionaAresta('d12', '23', '33')
        self.lic_fisica.adicionaAresta('d13', '31', '41')
        self.lic_fisica.adicionaAresta('d14', '31', '42')
        self.lic_fisica.adicionaAresta('d15', '32', '42')
        self.lic_fisica.adicionaAresta('d16', '33', '45')
        self.lic_fisica.adicionaAresta('d17', '31', '46')
        self.lic_fisica.adicionaAresta('d18', '41', '51')
        self.lic_fisica.adicionaAresta('d19', '45', '51')
        self.lic_fisica.adicionaAresta('d20', '41', '52')
        self.lic_fisica.adicionaAresta('d21', '42', '52')
        self.lic_fisica.adicionaAresta('d22', '45', '53')
        self.lic_fisica.adicionaAresta('d23', '31', '54')
        self.lic_fisica.adicionaAresta('d24', '43', '55')
        self.lic_fisica.adicionaAresta('d25', '21', '57')
        self.lic_fisica.adicionaAresta('d26', '43', '57')
        self.lic_fisica.adicionaAresta('d27', '51', '61')
        self.lic_fisica.adicionaAresta('d28', '51', '62')
        self.lic_fisica.adicionaAresta('d29', '52', '62')
        self.lic_fisica.adicionaAresta('d30', '21', '63')
        self.lic_fisica.adicionaAresta('d31', '53', '63')
        self.lic_fisica.adicionaAresta('d32', '51', '64')
        self.lic_fisica.adicionaAresta('d33', '56', '66')
        self.lic_fisica.adicionaAresta('d34', '31', '68')
        self.lic_fisica.adicionaAresta('d35', '57', '68')
        self.lic_fisica.adicionaAresta('d36', '61', '71')
        self.lic_fisica.adicionaAresta('d37', '41', '72')
        self.lic_fisica.adicionaAresta('d38', '45', '72')
        self.lic_fisica.adicionaAresta('d39', '66', '73')
        self.lic_fisica.adicionaAresta('d40', '31', '74')
        self.lic_fisica.adicionaAresta('d41', '43', '74')
        self.lic_fisica.adicionaAresta('d51', '41', '76')
        self.lic_fisica.adicionaAresta('d52', '68', '76')
        self.lic_fisica.adicionaAresta('d42', '65', '81')
        self.lic_fisica.adicionaAresta('d43', '74', '82')
        self.lic_fisica.adicionaAresta('d44', '73', '83')
        self.lic_fisica.adicionaAresta('d45', '54', '84')
        self.lic_fisica.adicionaAresta('d46', '71', '84')
        self.lic_fisica.adicionaAresta('d47', '16', '85')
        self.lic_fisica.adicionaAresta('d48', '25', '85')
        self.lic_fisica.adicionaAresta('d49', '51', '86')
        self.lic_fisica.adicionaAresta('d50', '76', '86')


        self.lic_fisica_gabarito = [
            '11', '12', '13', '14', '15', '16', '17', '26', '27',
            '34', '35', '36', '37', '43', '44', '56', '65', '21',
            '22', '23', '24', '25', '55', '66', '81', '31', '32',
            '33', '57', '73', '85', '41', '42', '45', '46', '54',
            '68', '74', '83', '51', '52', '53', '72', '76', '82',
            '61', '62', '63', '64', '86', '71', '84']


    def test_kahn(self):
        self.assertListEqual(self.lic_matematica.kahn(), self.lic_matematica_gabarito)
        self.assertListEqual(self.lic_fisica.kahn(), self.lic_fisica_gabarito)
        self.assertListEqual(self.telematica.kahn(), self.telematica_gabarito)
        self.assertListEqual(self.construcao_edif.kahn(), self.construcao_edif_gabarito)
        self.assertListEqual(self.eng_comp.kahn(), self.eng_comp_gabarito)