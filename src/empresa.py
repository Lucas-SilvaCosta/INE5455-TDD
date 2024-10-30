class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []
        self.projetos = []

    def adicionaFuncionario(self, funcionario):
        funcionarioFilter = filter(lambda x: x.cpf == funcionario.cpf, self.funcionarios)
        if len(list(funcionarioFilter)) > 0:
            return
        self.funcionarios.append(funcionario)
    
    def adicionaProjeto(self, projeto):
        if projeto.responsavel not in self.funcionarios:
            return
        self.projetos.append(projeto)