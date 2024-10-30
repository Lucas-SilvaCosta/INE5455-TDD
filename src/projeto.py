from src.funcionario import Funcionario

class Projeto:
    def __init__(self, nome, responsavel):
        self.nome = nome
        self.responsavel = responsavel
        self.funcionarios = []
        self.ocorrencias = []

    def adicionaFuncionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def adicionaOcorrencia(self, ocorrencia):
        self.ocorrencias.append(ocorrencia)
