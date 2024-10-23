import unittest

from src.funcionario import Funcionario
from src.empresa import Empresa

class TestEmpresa(unittest.TestCase):
    
    def testCriaAmbev(self):
        ambev = Empresa("Ambev")
        self.assertEqual("Ambev", ambev)    
    
if __name__ == '__main__':
    unittest.main()