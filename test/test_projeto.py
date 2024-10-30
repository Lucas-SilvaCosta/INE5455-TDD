import unittest

from src.ocorrencia import Ocorrencia
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

    def testAdicionaMatheus123(self):
        jorge = Funcionario("Jorge", "123")
        matheus = Funcionario("Matheus", "456")
        hawa = Projeto("Hawa", jorge)
        hawa.adicionaFuncionario(matheus)
        self.assertEqual("Matheus", hawa.funcionarios[0].nome)
        self.assertEqual("456", hawa.funcionarios[0].cpf)

    def testAdicionaMatheus123Repetido(self):
        jorge = Funcionario("Jorge", "123")
        matheus = Funcionario("Matheus", "456")
        hawa = Projeto("Hawa", jorge)
        hawa.adicionaFuncionario(matheus)
        hawa.adicionaFuncionario(matheus)
        self.assertEqual("Matheus", hawa.funcionarios[0].nome)
        self.assertEqual("456", hawa.funcionarios[0].cpf)
        self.assertEqual(1, len(hawa.funcionarios))

    def testAdicionaMaria789(self):
        jorge = Funcionario("Jorge", "123")
        maria = Funcionario("Maria", "789")
        hawa = Projeto("Hawa", jorge)
        hawa.adicionaFuncionario(maria)
        self.assertEqual("Maria", hawa.funcionarios[0].nome)
        self.assertEqual("789", hawa.funcionarios[0].cpf)

    def testAdicionaFuncionariosJornadaJorge123Maria789(self):
        jorge = Funcionario("Jorge", "123")
        matheus = Funcionario("Matheus", "456")
        maria = Funcionario("Maria", "789")
        jornada = Projeto("Jornada", jorge)
        jornada.adicionaFuncionario(matheus)
        jornada.adicionaFuncionario(maria)
        self.assertEqual("Matheus", jornada.funcionarios[0].nome)
        self.assertEqual("456", jornada.funcionarios[0].cpf)
        self.assertEqual("Maria", jornada.funcionarios[1].nome)
        self.assertEqual("789", jornada.funcionarios[1].cpf)
        self.assertEqual(2, len(jornada.funcionarios))

if __name__ == '__main__':
    unittest.main()