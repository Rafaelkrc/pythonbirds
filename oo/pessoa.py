class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=37):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_statico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return  f'{cls} - olhos {cls.olhos}'


class Homen(Pessoa):
    pass

class Mutante(Pessoa):
    olhos = 3


if __name__ == '__main__':
    pedro = Mutante(nome='Pedro', idade=6)
    carol = Homen(nome='Carol', idade=35)
    rafael = Pessoa(pedro, carol, nome='Rafael', idade=37)
    print(Pessoa.cumprimentar(pedro))
    print(id(pedro))
    print(pedro.cumprimentar())
    print(pedro.nome)
    print(pedro.idade)
    for filho in rafael.filhos:
        print(f'{rafael.nome} é o pai do {filho.nome}.')
    rafael.sobrenome = 'Coelho'
    del rafael.filhos
    rafael.olhos = 1
    del rafael.olhos
    print(rafael.__dict__)
    print(pedro.__dict__)
    print(Pessoa.olhos)
    print(pedro.olhos)
    print(rafael.olhos)
    print(id(Pessoa.olhos), id(pedro.olhos), id(rafael.olhos))
    print(Pessoa.metodo_statico(), pedro.metodo_statico())
    print(Pessoa.nome_e_atributos_de_classe(), pedro.nome_e_atributos_de_classe())
    pessoa = Pessoa()
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homen))
    print(isinstance(pedro, Pessoa))
    print(isinstance(pedro, Homen))
    print(pedro.olhos)
