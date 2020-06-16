class Pessoa:
    def __init__(self, *filhos, nome=None, idade=38):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    filipe = Pessoa(nome='Filipe')
    ribeiro = Pessoa(filipe, nome='Ribeiro')
    print(Pessoa.cumprimentar(ribeiro))
    print(id(ribeiro))
    print(ribeiro.cumprimentar())
    print (ribeiro.nome)
    print(ribeiro.idade)
    for filho in ribeiro.filhos:
        print(filho.nome)
    ribeiro.sobrenome = 'Simoes'
    del ribeiro.filhos
    print(ribeiro.__dict__)
    print(filipe.__dict__)