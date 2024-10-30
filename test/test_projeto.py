import unittest

from src.projeto import Projeto
from src.funcionario import Funcionario

class TestProjeto(unittest.TestCase):
    
    def testCriaJornadaJorge(self):
        jorge = Funcionario("Jorge", "123")
        jornada = Projeto("Jornada", jorge)
        self.assertEqual("Jornada", jornada.nome)
        self.assertEqual(jorge.cpf, jornada.responsavel.cpf)

    def testCriaHawaMatheus(self):
        matheus = Funcionario("Matheus", "456")
        hawa = Projeto("Hawa", matheus)
        self.assertEqual("Hawa", hawa.nome)
        self.assertEqual(matheus.cpf, hawa.responsavel.cpf)

    def testAdicionaJorge123(self):
        jorge = Funcionario("Jorge", "123")
        matheus = Funcionario("Matheus", "456")
        hawa = Projeto("Hawa", jorge)
        hawa.adicionaFunciona(matheus)
        self.assertEqual("Matheus", hawa.funcionarios[0].nome)
        self.assertEqual("456", hawa.funcionarios[0].cpf)

if __name__ == '__main__':
    unittest.main()