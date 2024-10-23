import unittest

from src.projeto import Projeto
from src.funcionario import Funcionario

class TestProjeto(unittest.TestCase):
    
    def setUp(self):
        self.jorge = Funcionario("Jorge", "123")

    def testCriaJornadaJorge(self):
        jornada = Projeto("Jornada", self.jorge)
        self.assertEqual("Jornada", jornada.nome)
        self.assertEqual(self.jorge.cpf, jornada.responsavel.cpf)
    
if __name__ == '__main__':
    unittest.main()