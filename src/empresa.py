from src.projeto import Projeto

class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []
        self.projetos = []

    def adicionaFuncionario(self, funcionario):
        self.funcionarios.append(funcionario)
    
    def adicionaProjeto(self, projeto):
        self.projetos.append(projeto)