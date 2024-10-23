import unittest

class TestFuncionario(unittest.TestCase):
    
    def testCriaJorge123(self):
        jorge = Funcionario("Jorge", "123")
    
if __name__ == '__main__':
    unittest.main()