import unittest

from src.funcionario import Funcionario

class TestFuncionario(unittest.TestCase):
    
    def testCriaJorge123(self):
        jorge = Funcionario("Jorge", "123")
        self.assertEqual("Jorge", jorge.nome)
        self.assertEqual("123", jorge.cpf)

    def testCriaMatheus456(self):
        matheus = Funcionario("Matheus", "456")
        self.assertEqual("Matheus", matheus.nome)
        self.assertEqual("456", matheus.cpf)
    
    
if __name__ == '__main__':
    unittest.main()