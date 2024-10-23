import unittest

from src.funcionario import Funcionario
from src.empresa import Empresa

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

    
if __name__ == '__main__':
    unittest.main()