class Ocorrencia:
    def __init__(self, identificador, tipo, responsavel, prioridade, estado):
        self.identificador = identificador
        self.tipo = tipo
        self.responsavel = responsavel
        self.prioridade = prioridade
        self.estado = estado

    def changeResponsavel(self, responsavel):
        if not self.estado:
            return
        self.responsavel = responsavel

    def changePrioridade(self, prioridade):
        if not self.estado:
            return
        self.responsavel = prioridade