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
        hawa.adicionaFuncionario(matheus)
        self.assertEqual("Matheus", hawa.funcionarios[0].nome)
        self.assertEqual("456", hawa.funcionarios[0].cpf)

    def testAdicionaMaria789(self):
        jorge = Funcionario("Jorge", "123")
        maria = Funcionario("Maria", "789")
        hawa = Projeto("Hawa", jorge)
        hawa.adicionaFuncionario(maria)
        self.assertEqual("Maria", hawa.funcionarios[0].nome)
        self.assertEqual("789", hawa.funcionarios[0].cpf)

    def criaOcorrenciaJorge123(self):
        jorge = Funcionario("Jorge", "123")
        jornada = Projeto("Jornada", jorge)
        ocorrencia = {"identificador": "Bug 1", "responsavel": jorge, "estado": "Aberta"}
        jornada.adicionaOcorrencia(ocorrencia)


if __name__ == '__main__':
    unittest.main()