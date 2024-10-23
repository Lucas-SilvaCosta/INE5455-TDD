from src.funcionario import Funcionario

class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def adicionaFuncionario(self, funcionario):
        self.funcionarios.append(funcionario)