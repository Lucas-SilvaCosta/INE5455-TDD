import unittest

from src.funcionario import Funcionario
from src.ocorrencia import Ocorrencia


class TestOcorrencia(unittest.TestCase):

    def testCriaOcorrencia(self):
        jorge = Funcionario("Jorge", "123")
        ocorrencia = Ocorrencia("Bug 1", "Bug", jorge, "Baixa", True)
        self.assertEqual("Bug 1", ocorrencia.identificador)
        self.assertEqual("Bug", ocorrencia.tipo)
        self.assertEqual(jorge, ocorrencia.responsavel)
        self.assertEqual("Baixa", ocorrencia.prioridade)
        self.assertEqual(True, ocorrencia.estado)
if __name__ == '__main__':
    unittest.main()