class CabineTelefonica:
    def __init__(self):
        self.saldo = 0.0
        self.estado = 'INATIVO'
        self.numero = ''
        self.valor_moedas_validas = ["10c", "20c", "50c", "1e", "2"]
        self.moedas_inseridas = []

    def valida_moedas(self, lista_moedas):
        for moeda in lista_moedas:
            if moeda not in self.valor_moedas_validas:
                return False
        return True

    def retorna_moedas(self):
        total_moedas = sum(self.moedas_inseridas)
        self.moedas_inseridas = []
        self.saldo = 0.0
        self.estado = 'INATIVO'
        return f"Valor a ser devolvido: {total_moedas:.2f} euros"

    def inativo(self, comando):
        if comando == 'LEVANTAR':
            self.estado = 'AGUARDANDO_MOEDAS'
            return "Insira as moedas para a chamada."
        else:
            return "O telefone está inativo. Levante o auscultador para iniciar uma chamada."

    def aguardando_moedas(self, comando):
        if comando.startswith('MOEDA'):
            lista_moedas = comando.split()[1:]
            if self.valida_moedas([float(moeda) for moeda in lista_moedas]):
                self.moedas_inseridas.extend([float(moeda) for moeda in lista_moedas])
                self.saldo = sum(self.moedas_inseridas)
                return f"Saldo atual: {self.saldo:.2f} euros. Digite o número de telefone ou comandos como 'POUSAR' ou 'ABORTAR'."
            else:
                return "Moedas inválidas. Insira apenas moedas de 10, 20, 50 centavos, 1 ou 2 euros."
        elif comando == 'ABORTAR':
            return self.retorna_moedas()
        else:
            return "Aguarde a inserção das moedas para realizar uma chamada."

    def chamada_bloqueada(self):
        self.estado = 'AGUARDANDO_MOEDAS'
        return "Chamada bloqueada. Insira mais moedas ou desista da chamada."

    def chamada_nacional(self):
        custo = 0.25
        if self.saldo >= custo:
            self.saldo -= custo
            self.estado = 'INATIVO'
            return f"Chamada realizada. Saldo atual: {self.saldo:.2f} euros."
        else:
            self.estado = 'AGUARDANDO_MOEDAS'
            return f"Saldo insuficiente para realizar a chamada. Insira mais {custo - self.saldo:.2f} euros ou desista da chamada."

    def chamada_internacional(self):
        custo = 1.5
        if self.saldo >= custo:
            self.saldo -= custo
            self.estado = 'INATIVO'
            return f"Chamada realizada. Saldo atual: {self.saldo:.2f} euros."
        else:
            self.estado = 'AGUARDANDO_MOEDAS'
            return f"Saldo insuficiente para realizar a chamada!"
