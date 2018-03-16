class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def getNome(self):
        return self.nome

class Fisica(Pessoa):
    
    def __init__(self, nome, idade, cpf):
        Pessoa.__init__(self, nome, idade)
        self.cpf = cpf

    def getCpf(self):
        return self.cpf

class Juridica(Pessoa):
    
    def __init__(self, nome, idade, cnpj):
        Pessoa.__init__(self, nome, idade)
        self.cnpj = cnpj

    def getCnpj(self):
        return self.cnpj

p = Fisica('fabio', 31, 132123)
print(p.getCpf())