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
        self.assertEqual("Jorge", hawa.funcionarios[0].nome)
        self.assertEqual("123", hawa.funcionarios[0].cpf)
        self.assertEqual("Matheus", hawa.funcionarios[1].nome)
        self.assertEqual("456", hawa.funcionarios[1].cpf)

    def testAdicionaMatheus123Repetido(self):
        jorge = Funcionario("Jorge", "123")
        matheus = Funcionario("Matheus", "456")
        hawa = Projeto("Hawa", jorge)
        hawa.adicionaFuncionario(matheus)
        self.assertRaises(RuntimeError, hawa.adicionaFuncionario, matheus)

    def testAdicionaMaria789(self):
        jorge = Funcionario("Jorge", "123")
        maria = Funcionario("Maria", "789")
        hawa = Projeto("Hawa", jorge)
        hawa.adicionaFuncionario(maria)
        self.assertEqual("Jorge", hawa.funcionarios[0].nome)
        self.assertEqual("123", hawa.funcionarios[0].cpf)
        self.assertEqual("Maria", hawa.funcionarios[1].nome)
        self.assertEqual("789", hawa.funcionarios[1].cpf)

    def testAdicionaFuncionariosJornadaJorge123Maria789(self):
        jorge = Funcionario("Jorge", "123")
        matheus = Funcionario("Matheus", "456")
        maria = Funcionario("Maria", "789")
        jornada = Projeto("Jornada", jorge)
        jornada.adicionaFuncionario(matheus)
        jornada.adicionaFuncionario(maria)
        self.assertEqual("Jorge", jornada.funcionarios[0].nome)
        self.assertEqual("123", jornada.funcionarios[0].cpf)
        self.assertEqual("Matheus", jornada.funcionarios[1].nome)
        self.assertEqual("456", jornada.funcionarios[1].cpf)
        self.assertEqual("Maria", jornada.funcionarios[2].nome)
        self.assertEqual("789", jornada.funcionarios[2].cpf)
        self.assertEqual(3, len(jornada.funcionarios))

    def testVerificaFuncionarioVerdadeiro(self):
        jorge = Funcionario("Jorge", "123")
        matheus = Funcionario("Matheus", "456")
        jornada = Projeto("Jornada", jorge)
        jornada.adicionaFuncionario(matheus)
        self.assertEqual(True, jornada.verificaFuncionario(jorge))
        self.assertEqual(True, jornada.verificaFuncionario(matheus))

    def testVerificaFuncionarioVerdadeiro(self):
        jorge = Funcionario("Jorge", "123")
        matheus = Funcionario("Matheus", "456")
        jornada = Projeto("Jornada", jorge)
        self.assertEqual(True, jornada.verificaFuncionario(jorge))
        self.assertEqual(False, jornada.verificaFuncionario(matheus))

    def testAdicionaOcorrenciaValida(self):
        jorge = Funcionario("Jorge", "123")
        jornada = Projeto("Jornada", jorge)
        ocorrencia = Ocorrencia(1, "Bug", jorge, "Baixa", "Teste")
        jornada.adicionaOcorrencia(ocorrencia)
        self.assertEqual(ocorrencia, jornada.ocorrencias[0])

    def testAdicionaOcorrenciaFuncionarioForaDoProjeto(self):
        jorge = Funcionario("Jorge", "123")
        jornada = Projeto("Jornada", jorge)
        matheus = Funcionario("Matheus", "456")
        ocorrencia = Ocorrencia(1, "Bug", matheus, "Baixa", "Teste")
        self.assertRaises(RuntimeError, jornada.adicionaOcorrencia, ocorrencia)

    def testAdicionaOcorrenciaRepetida(self):
        jorge = Funcionario("Jorge", "123")
        jornada = Projeto("Jornada", jorge)
        ocorrencia = Ocorrencia(1, "Bug", jorge, "Baixa", "Teste")
        jornada.adicionaOcorrencia(ocorrencia)
        self.assertRaises(RuntimeError, jornada.adicionaOcorrencia, ocorrencia)

if __name__ == '__main__':
    unittest.main()