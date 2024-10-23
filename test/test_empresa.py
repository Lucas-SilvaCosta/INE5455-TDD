import unittest

from src.funcionario import Funcionario
from src.empresa import Empresa
from src.projeto import Projeto

class TestEmpresa(unittest.TestCase):
    
    def testCriaAmbev(self):
        ambev = Empresa("Ambev")
        self.assertEqual("Ambev", ambev.nome)
    
    def testCriaFord(self):
        ford = Empresa("Ford")
        self.assertEqual("Ford", ford.nome)

    def testAdicionaJorgeAmbev(self):
        jorge = Funcionario("Jorge", "123")
        ambev = Empresa("Ambev")
        ambev.adicionaFuncionario(jorge)
        self.assertEqual(len(ambev.funcionarios), 1)
        self.assertEqual(ambev.funcionarios[0].cpf, "123")

    def testAdicionaMatheusFord(self):
        matheus = Funcionario("Matheus", "456")
        ford = Empresa("Ford")
        ford.adicionaFuncionario(matheus)
        self.assertEqual(len(ford.funcionarios), 1)
        self.assertEqual(ford.funcionarios[0].cpf, "456")

    def testAdicionaJornadaAmbev(self):
        jorge = Funcionario("Jorge", "123")
        jornada = Projeto("Jornada", jorge)
        ambev = Empresa("Ambev")
        ambev.adicionaProjeto(jornada)
        self.assertEqual(len(ambev.projetos), 1)
        self.assertEqual(ambev.projetos[0].nome, "Jornada")



    
if __name__ == '__main__':
    unittest.main()