class Pessoa:
    def __init__(self, *filhos, nome=None, idade=37):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    pedro = Pessoa(nome='Pedro', idade=6)
    carol = Pessoa(nome='Carol', idade=35)
    rafael1 = Pessoa(pedro, carol, nome='Rafael', idade=37)
    print(Pessoa.cumprimentar(pedro))
    print(id(pedro))
    print(pedro.cumprimentar())
    print(pedro.nome)
    print(pedro.idade)
    for filho in rafael1.filhos:
        print(f'{rafael1.nome} é o pai do {filho.nome}.')
