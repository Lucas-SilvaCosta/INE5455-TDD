
class Projeto:
    def __init__(self, nome, responsavel):
        self.nome = nome
        self.responsavel = responsavel
        self.funcionarios = [responsavel]
        self.ocorrencias = []

    def adicionaFuncionario(self, funcionario):
        funcionarioFilter = filter(lambda x: x.cpf == funcionario.cpf, self.funcionarios)
        if len(list(funcionarioFilter)) > 0:
            raise RuntimeError("Funcionário já existe no projeto")
        self.funcionarios.append(funcionario)

    def adicionaOcorrencia(self, ocorrencia):
        ocorrenciaFilter = filter(lambda x: x.identificador == ocorrencia.identificador, self.ocorrencias)
        if len(list(ocorrenciaFilter)) > 0:
            raise RuntimeError("Ocorrencia ja existe")
        if ocorrencia.responsavel not in self.funcionarios:
            raise RuntimeError("Funcionário não está no projeto")
        self.ocorrencias.append(ocorrencia)

    def verificaFuncionario(self, funcionario):
        return len(list(filter(lambda x: x.cpf == funcionario.cpf, self.funcionarios)))
