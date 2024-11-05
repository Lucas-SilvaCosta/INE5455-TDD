class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []
        self.projetos = []

    def adicionaFuncionario(self, funcionario):
        funcionarioFilter = filter(lambda x: x.cpf == funcionario.cpf, self.funcionarios)
        if len(list(funcionarioFilter)) > 0:
            raise RuntimeError("Funcionário já existe na empresa")
        self.funcionarios.append(funcionario)
    
    def adicionaProjeto(self, projeto):
        if projeto.responsavel not in self.funcionarios:
            raise RuntimeError("Responsável não existe na empresa")
        if projeto in self.projetos:
            raise RuntimeError("Projeto já existe na empresa")
        self.projetos.append(projeto)

    def adicionaFuncionarioProjeto(self, funcionario, projeto):
        funcionarioFilter = filter(lambda x: x.cpf == funcionario.cpf, self.funcionarios)
        if len(list(funcionarioFilter)) == 0:
            raise RuntimeError("Funcionário não existe na empresa")
        if projeto not in self.projetos:
            raise RuntimeError("Projeto não existe na empresa.")
        projeto.adicionaFuncionario(funcionario)

    def adicionaOcorrenciaProjeto(self, ocorrencia, projeto):
        ocorrenciasFuncionario = 0
        if projeto not in self.projetos:
            raise RuntimeError("Projeto não existe na empresa")
        for p in self.projetos:
            for ocorrenciaProjeto in p.ocorrencias:
                if ocorrenciaProjeto.responsavel.cpf == ocorrencia.responsavel.cpf and ocorrenciaProjeto.estado:
                    ocorrenciasFuncionario += 1
        if ocorrenciasFuncionario >= 10:
            raise RuntimeError("Funcionário já possui 10 ocorrências")
        projeto.adicionaOcorrencia(ocorrencia)

    def modificaResponsavelOcorrencia(self, projeto, ocorrencia, novoResponsavel):
        ocorrenciasFuncionario = 0
        if projeto not in self.projetos:
            raise RuntimeError("Projeto não existe na empresa")
        if not projeto.verificaFuncionario(novoResponsavel):
            raise RuntimeError("Funcionário não está no projeto")
        if novoResponsavel not in self.funcionarios:
            raise RuntimeError("Funcionário não está na empresa")
        for projeto in self.projetos:
            for ocorrenciaProjeto in projeto.ocorrencias:
                if ocorrenciaProjeto.responsavel.cpf == novoResponsavel.cpf and ocorrenciaProjeto.estado:
                    ocorrenciasFuncionario += 1
        if ocorrenciasFuncionario >= 10:
            raise RuntimeError("Funcionário já possui 10 ocorrências")
        ocorrencia.responsavel = novoResponsavel
