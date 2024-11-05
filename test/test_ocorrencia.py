import unittest

from src.funcionario import Funcionario
from src.ocorrencia import Ocorrencia


class TestOcorrencia(unittest.TestCase):

    def testCriaOcorrencia(self):
        jorge = Funcionario("Jorge", "123")
        ocorrencia = Ocorrencia(1, "Bug", jorge, "Baixa", "Descricao")
        self.assertEqual(1, ocorrencia.identificador)
        self.assertEqual("Bug", ocorrencia.tipo)
        self.assertEqual(jorge, ocorrencia.responsavel)
        self.assertEqual("Baixa", ocorrencia.prioridade)
        self.assertEqual(True, ocorrencia.estado)
        self.assertEqual("Descricao", ocorrencia.descricao)

    def testFechaOcorrenciaBug1(self):
        jorge = Funcionario("Jorge", "123")
        ocorrencia = Ocorrencia(1, "Bug", jorge, "Baixa", "Descricao")
        ocorrencia.fechar()
        self.assertEqual(False, ocorrencia.estado)

    def testMudaResponsavelBug1Aberto(self):
        jorge = Funcionario("Jorge", "123")
        matheus = Funcionario("Matheus", "456")
        ocorrencia = Ocorrencia(1, "Bug", jorge, "Baixa", "Descricao")
        ocorrencia.changeResponsavel(matheus)
        self.assertEqual(matheus, ocorrencia.responsavel)

    def testMudaResponsavelBug1Fechado(self):
        jorge = Funcionario("Jorge", "123")
        matheus = Funcionario("Matheus", "456")
        ocorrencia = Ocorrencia(1, "Bug", jorge, "Baixa", "Descricao")
        ocorrencia.fechar()
        self.assertRaises(RuntimeError, ocorrencia.changeResponsavel, matheus)

    def testMudaPrioridadeBug1Aberto(self):
        jorge = Funcionario("Jorge", "123")
        ocorrencia = Ocorrencia(1, "Bug", jorge, "Baixa", "Descricao")
        ocorrencia.changePrioridade("Alta")
        self.assertEqual("Alta", ocorrencia.prioridade)

    def testMudaPrioridadelBug1Fechado(self):
        jorge = Funcionario("Jorge", "123")
        ocorrencia = Ocorrencia(1, "Bug", jorge, "Baixa", "Descricao")
        ocorrencia.fechar()
        self.assertRaises(RuntimeError, ocorrencia.changePrioridade, "Alta")

if __name__ == '__main__':
    unittest.main()