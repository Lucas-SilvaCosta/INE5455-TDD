import unittest

from src.funcionario import Funcionario
from src.empresa import Empresa
from src.ocorrencia import Ocorrencia
from src.projeto import Projeto

class TestEmpresa(unittest.TestCase):

    def testCriaAmbev(self):
        ambev = Empresa("Ambev")
        self.assertEqual("Ambev", ambev.nome)

    def testAdicionaJorgeAmbev(self):
        jorge = Funcionario("Jorge", "123")
        ambev = Empresa("Ambev")
        ambev.adicionaFuncionario(jorge)
        self.assertEqual(len(ambev.funcionarios), 1)
        self.assertEqual(ambev.funcionarios[0].cpf, "123")


    def testAdicionaMatheusFord(self):
        matheus = Funcionario("Matheus", "456")
        ford = Empresa("Ford")
        ford.adicionaFuncionario(matheus)
        self.assertEqual(len(ford.funcionarios), 1)
        self.assertEqual(ford.funcionarios[0].cpf, "456")

    def testAdicionaHawaAmbev(self):
        jorge = Funcionario("Jorge", "123")
        ambev = Empresa("Ambev")
        ambev.adicionaFuncionario(jorge)
        hawa = Projeto("Hawa", jorge)
        ambev.adicionaProjeto(hawa)
        self.assertEqual(len(ambev.projetos), 1)
        self.assertEqual(ambev.projetos[0].nome, "Hawa")

    # Adiciona jorge ao hawa duas vezes
    def testAdicionaJorgeHawaRepetido(self):
        jorge = Funcionario("Jorge", "123")
        ambev = Empresa("Ambev")
        ambev.adicionaFuncionario(jorge)
        hawa = Projeto("Hawa", jorge)
        ambev.adicionaProjeto(hawa)
        self.assertRaises(RuntimeError, ambev.adicionaFuncionarioProjeto, jorge, hawa)

    # Adiciona matheus duas vezes
    def testAdicionaMatheusFordRepetido(self):
        matheus = Funcionario("Matheus", "456")
        ford = Empresa("Ford")
        ford.adicionaFuncionario(matheus)
        self.assertRaises(RuntimeError, ford.adicionaFuncionario, matheus)

    # Adiciona jorge duas vezes
    def testAdicionaJorgeAmbevRepetido(self):
        jorge = Funcionario("Jorge", "123")
        ambev = Empresa("Ambev")
        ambev.adicionaFuncionario(jorge)
        self.assertRaises(RuntimeError, ambev.adicionaFuncionario, jorge)

    # Adiciona projeto repetido
    def testAdicionaHawaAmbevRepetido(self):
        jorge = Funcionario("Jorge", "123")
        ambev = Empresa("Ambev")
        ambev.adicionaFuncionario(jorge)
        hawa = Projeto("Hawa", jorge)
        ambev.adicionaProjeto(hawa)
        self.assertRaises(RuntimeError, ambev.adicionaProjeto, hawa)

    # Adiciona projeto repetido
    def testAdicionaHawaAmbevRepetido(self):
        jorge = Funcionario("Jorge", "123")
        ambev = Empresa("Ambev")
        ambev.adicionaFuncionario(jorge)
        hawa = Projeto("Hawa", jorge)
        ambev.adicionaProjeto(hawa)
        self.assertRaises(RuntimeError, ambev.adicionaProjeto, hawa)

    # Testa adicionar funcionário ao projeto com funcionario fora da empresa
    def testAdicionaJorgeForaEmpresa(self):
        matheus = Funcionario("Matheus", "456")
        jorge = Funcionario("Jorge", "123")
        ambev = Empresa("Ambev")
        ambev.adicionaFuncionario(matheus)
        hawa = Projeto("Hawa", matheus)
        ambev.adicionaProjeto(hawa)
        self.assertRaises(RuntimeError, ambev.adicionaFuncionarioProjeto, jorge, hawa)

    # Testa adicionar funcionário ao projeto com projeto fora da empresa
    def testAdicionaHawaForaEmpresa(self):
        matheus = Funcionario("Matheus", "456")
        jorge = Funcionario("Jorge", "123")
        ambev = Empresa("Ambev")
        ambev.adicionaFuncionario(matheus)
        hawa = Projeto("Hawa", matheus)
        self.assertRaises(RuntimeError, ambev.adicionaFuncionarioProjeto, jorge, hawa)

    # Adiciona projeto com responsável fora da empresa
    def testAdicionaJornadaAmbevJorgeForaEmpresa(self):
        jorge = Funcionario("Jorge", "123")
        jornada = Projeto("Jornada", jorge)
        ambev = Empresa("Ambev")
        self.assertRaises(RuntimeError, ambev.adicionaProjeto, jornada)

    # Adiciona funcionario a empresa fora do projeto
    def testAdicionaJorgeAoJornadaForaEmpresa(self):
        jorge = Funcionario("Jorge", "123")
        jornada = Projeto("Jornada", jorge)
        ambev = Empresa("Ambev")
        ambev.adicionaFuncionario(jorge)
        self.assertRaises(RuntimeError, ambev.adicionaFuncionarioProjeto, jorge, jornada)

    def testAdicionaOcorrencia(self):
        jorge = Funcionario("Jorge", "123")
        ambev = Empresa("Ambev")
        ambev.adicionaFuncionario(jorge)
        hawa = Projeto("Hawa", jorge)
        ambev.adicionaProjeto(hawa)
        ocorrencia = Ocorrencia(1, "Bug", jorge, "Baixa", "Descricao")
        ambev.adicionaOcorrenciaProjeto(ocorrencia, hawa)
        self.assertEqual(hawa.ocorrencias[0], ocorrencia)

    def testAdicionaOcorrenciaProjetoForaEmpresa(self):
        jorge = Funcionario("Jorge", "123")
        matheus = Funcionario("Matheus", "456")
        ambev = Empresa("Ambev")
        ambev.adicionaFuncionario(jorge)
        hawa = Projeto("Hawa", jorge)
        ocorrencia = Ocorrencia(1, "Bug", matheus, "Baixa", "Descricao")
        self.assertRaises(RuntimeError, ambev.adicionaOcorrenciaProjeto, ocorrencia, hawa)

    def testAdiciona10Ocorrencias(self):
        jorge = Funcionario("Jorge", "123")
        ambev = Empresa("Ambev")
        ambev.adicionaFuncionario(jorge)
        hawa = Projeto("Hawa", jorge)
        ambev.adicionaProjeto(hawa)
        ocorrenciasTeste = []
        for i in range(10):
            ocorrencia = Ocorrencia(i, "Bug", jorge, "Baixa", "Descricao " + str(i))
            ocorrenciasTeste.append(ocorrencia)
            ambev.adicionaOcorrenciaProjeto(ocorrencia, hawa)
        self.assertListEqual(ocorrenciasTeste, hawa.ocorrencias)

    def testAdiciona11Ocorrencias(self):
        jorge = Funcionario("Jorge", "123")
        ambev = Empresa("Ambev")
        ambev.adicionaFuncionario(jorge)
        hawa = Projeto("Hawa", jorge)
        ambev.adicionaProjeto(hawa)
        for i in range(10):
            ocorrencia = Ocorrencia(i, "Bug", jorge, "Baixa", "Descricao " + str(i))
            ambev.adicionaOcorrenciaProjeto(ocorrencia, hawa)
        ocorrencia11 = Ocorrencia(11, "Bug", jorge, "Baixa", "Descricao 11")
        self.assertRaises(RuntimeError, ambev.adicionaOcorrenciaProjeto, ocorrencia11, hawa)

    def testAdiciona11Ocorrencias2Projetos(self):
        jorge = Funcionario("Jorge", "123")
        ambev = Empresa("Ambev")
        ambev.adicionaFuncionario(jorge)
        hawa = Projeto("Hawa", jorge)
        jornada = Projeto("Jornada", jorge)
        ambev.adicionaProjeto(hawa)
        ambev.adicionaProjeto(jornada)
        for i in range(5):
            ocorrencia = Ocorrencia(i, "Bug", jorge, "Baixa", "Descricao " + str(i))
            ambev.adicionaOcorrenciaProjeto(ocorrencia, hawa)
        for i in range(5):
            ocorrencia = Ocorrencia(i, "Bug", jorge, "Baixa", "Descricao " + str(i))
            ambev.adicionaOcorrenciaProjeto(ocorrencia, jornada)
        ocorrencia11 = Ocorrencia(11, "Bug", jorge, "Baixa", "Descricao 11")
        self.assertRaises(RuntimeError, ambev.adicionaOcorrenciaProjeto, ocorrencia11, hawa)

    def testAdiciona11OcorrenciasFechandoUma(self):
        jorge = Funcionario("Jorge", "123")
        ambev = Empresa("Ambev")
        ambev.adicionaFuncionario(jorge)
        hawa = Projeto("Hawa", jorge)
        ambev.adicionaProjeto(hawa)
        ocorrenciasTeste = []
        for i in range(10):
            ocorrencia = Ocorrencia(i, "Bug", jorge, "Baixa", "Descricao " + str(i))
            ocorrenciasTeste.append(ocorrencia)
            ambev.adicionaOcorrenciaProjeto(ocorrencia, hawa)
        hawa.ocorrencias[0].fechar()
        ocorrencia11 = Ocorrencia(11, "Bug", jorge, "Baixa", "Descricao 11")
        ocorrenciasTeste.append(ocorrencia11)
        ambev.adicionaOcorrenciaProjeto(ocorrencia11, hawa)
        self.assertListEqual(ocorrenciasTeste, hawa.ocorrencias)

    def testModificaResponsavel(self):
        jorge = Funcionario("Jorge", "123")
        matheus = Funcionario("Matheus", "456")
        ambev = Empresa("Ambev")
        ambev.adicionaFuncionario(jorge)
        ambev.adicionaFuncionario(matheus)
        hawa = Projeto("Hawa", jorge)
        hawa.adicionaFuncionario(matheus)
        ambev.adicionaProjeto(hawa)
        ocorrencia = Ocorrencia(1, "Bug", jorge, "Baixa", "Descricao")
        ambev.adicionaOcorrenciaProjeto(ocorrencia, hawa)
        ambev.modificaResponsavelOcorrencia(hawa, ocorrencia, matheus)
        self.assertEqual(matheus, ocorrencia.responsavel)

    def testModificaResponsavelProjetoForaEmpresa(self):
        jorge = Funcionario("Jorge", "123")
        matheus = Funcionario("Matheus", "456")
        ambev = Empresa("Ambev")
        ambev.adicionaFuncionario(jorge)
        hawa = Projeto("Hawa", jorge)
        hawa.funcionarios.append(matheus)
        ambev.adicionaProjeto(hawa)
        ocorrencia = Ocorrencia(1, "Bug", jorge, "Baixa", "Descricao")
        ambev.adicionaOcorrenciaProjeto(ocorrencia, hawa)
        self.assertRaises(RuntimeError, ambev.modificaResponsavelOcorrencia, hawa, ocorrencia, matheus)

    def testModificaResponsavelForaDoProjeto(self):
        jorge = Funcionario("Jorge", "123")
        matheus = Funcionario("Matheus", "456")
        ambev = Empresa("Ambev")
        ambev.adicionaFuncionario(jorge)
        ambev.adicionaFuncionario(matheus)
        hawa = Projeto("Hawa", jorge)
        ambev.adicionaProjeto(hawa)
        ocorrencia = Ocorrencia(1, "Bug", jorge, "Baixa", "Descricao")
        self.assertRaises(RuntimeError, ambev.modificaResponsavelOcorrencia, hawa, ocorrencia, matheus)

    def testModificaResponsavelForaDaEmpresa(self):
        jorge = Funcionario("Jorge", "123")
        matheus = Funcionario("Matheus", "456")
        ambev = Empresa("Ambev")
        ambev.adicionaFuncionario(jorge)
        hawa = Projeto("Hawa", jorge)
        ocorrencia = Ocorrencia(1, "Bug", jorge, "Baixa", "Descricao")
        self.assertRaises(RuntimeError, ambev.modificaResponsavelOcorrencia, hawa, ocorrencia, matheus)

    def testModificaResponsavel11Ocorrencias(self):
        jorge = Funcionario("Jorge", "123")
        matheus = Funcionario("Matheus", "456")
        ambev = Empresa("Ambev")
        ambev.adicionaFuncionario(jorge)
        ambev.adicionaFuncionario(matheus)
        hawa = Projeto("Hawa", jorge)
        hawa.adicionaFuncionario(matheus)
        ambev.adicionaProjeto(hawa)
        for i in range(10):
            ocorrencia = Ocorrencia(i, "Bug", jorge, "Baixa", "Descricao " + str(i))
            ambev.adicionaOcorrenciaProjeto(ocorrencia, hawa)
        ocorrenciaMatheus = Ocorrencia(11, "Bug", matheus, "Baixa", "Descricao 11")
        ambev.adicionaOcorrenciaProjeto(ocorrenciaMatheus, hawa)
        self.assertRaises(RuntimeError, ambev.modificaResponsavelOcorrencia, hawa, ocorrenciaMatheus, jorge)





if __name__ == '__main__':
    unittest.main()