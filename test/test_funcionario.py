import unittest

from src.funcionario import Funcionario

class TestFuncionario(unittest.TestCase):
    
    def testCriaJorge123(self):
        jorge = Funcionario("Jorge", "123")
        self.assertEquals("Jorge", jorge.name)
        self.assertEquals("123", jorge.cpf)

    
    
if __name__ == '__main__':
    unittest.main()