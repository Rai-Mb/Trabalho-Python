# 4. (Prog. Orientado Objetos) Elabore um programa em Python que Crie a classe “Produto” e derive (Herança) as 3
# subclasses abaixo. Seu programa deve ter no mínimo 3 atributos e no mínimo 2 métodos (e garantir o Polimorfismo).
# O programa deve ter um menu que escolha qual classe o usuário quer instanciar.

class Produto:
    def __init__(self, nome, preco, descricao):
        self.nome = nome
        self.preco = preco
        self.descricao = descricao

    def calcularTotal(self, quantidade):
        return self.preco * quantidade

    def detalhes(self):
        raise NotImplementedError('Método "detalhes" precisa ser implementado.')

class Livro(Produto):
    def __init__(self, nome, preco, descricao, autor):
        super().__init__(nome, preco, descricao)
        self.autor = autor

    def detalhes(self):
        return f'Livro: {self.nome}\nAutor: {self.autor}\nDescrição: {self.descricao}'

class CD(Produto):
    def __init__(self, nome, preco, descricao, artista):
        super().__init__(nome, preco, descricao)
        self.artista = artista

    def detalhes(self):
        return f'CD: {self.nome}\nArtista: {self.artista}\nDescrição: {self.descricao}'

class DVD(Produto):
    def __init__(self, nome, preco, descricao, diretor):
        super().__init__(nome, preco, descricao)
        self.diretor = diretor

    def detalhes(self):
        return f'DVD: {self.nome}\nDiretor: {self.diretor}\nDescrição: {self.descricao}'

def selecionar():
    print('Escolha um produto:')
    print('0. Sair')
    print('1. Livro')
    print('2. CD')
    print('3. DVD')
    opcao = input('Digite a opção desejada: ')
    return opcao

def criarProduto(classe):
    if classe == '0':
        return None

    nome = input('Digite o nome do produto: ')
    preco = float(input('Digite o preço do produto: '))
    descricao = input('Digite a descrição do produto: ')

    if classe == '1':
        autor = input('Digite o autor do livro: ')
        produto = Livro(nome, preco, descricao, autor)
    elif classe == '2':
        artista = input('Digite o artista do CD: ')
        produto = CD(nome, preco, descricao, artista)
    elif classe == '3':
        diretor = input('Digite o diretor do DVD: ')
        produto = DVD(nome, preco, descricao, diretor)
    else:
        print('Opção inválida.')
        return None

    return produto

while True:
    opcao = selecionar()

    if opcao == '0':
        print('Programa encerrado.')
        break
    if opcao == '1' or opcao == '2' or opcao == '3':
        produto = criarProduto(opcao)
        if produto:
            print('Detalhes do produto:')
            print(produto.detalhes())
            quantidade = int(input('Digite a quantidade: '))
            total = produto.calcularTotal(quantidade)
            print(f'Total a pagar: R${total}')
            break
    else:
        print('Digite uma opção valida.')
