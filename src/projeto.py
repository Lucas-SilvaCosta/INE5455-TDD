from src.funcionario import Funcionario

class Projeto:
    def __init__(self, nome, responsavel):
        self.nome = nome
        self.responsavel = responsavel
        self.funcionarios = []

    def adicionaFuncionario(self, funcionario):
        self.funcionarios.append(Funcionario("Matheus", "456"))