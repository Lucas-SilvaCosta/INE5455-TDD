from src.funcionario import Funcionario

class Projeto:
    def __init__(self, nome, responsavel):
        self.nome = nome
        self.responsavel = responsavel
        self.funcionarios = []
        self.ocorrencias = []

    def adicionaFuncionario(self, funcionario):
        funcionarioFilter = filter(lambda x: x.cpf == funcionario.cpf, self.funcionarios)
        if len(list(funcionarioFilter)) > 0:
            return
        self.funcionarios.append(funcionario)

    def adicionaOcorrencia(self, ocorrencia):
        ocorrenciaFilter = filter(lambda x: x["identificador"] == ocorrencia["identificador"], self.ocorrencias)
        if len(list(ocorrenciaFilter)) > 0:
            return
        self.ocorrencias.append(ocorrencia)
