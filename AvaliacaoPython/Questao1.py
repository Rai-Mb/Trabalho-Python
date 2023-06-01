# 1. (Dados Aglomerados) Desenvolva um programa em Python que cadastre informações de várias pessoas (nome, idade e CPF)
# e depois coloque em um dicionário. Depois remova todas as pessoas menores de 18 anos do dicionário e coloque em outro dicionário.
pessoas = {}

menoresDe18 = {}

def cadastrarPessoa():
    nome = input('Digite o nome da pessoa: ')
    idade = int(input('Digite a idade da pessoa: '))
    cpf = input('Digite o CPF da pessoa: ')

    pessoas[cpf] = {'nome': nome, 'idade': idade, 'cpf': cpf}

numPessoas = int(input('Quantas pessoas deseja cadastrar?\n'))
for i in range(numPessoas):
    cadastrarPessoa()

for cpf, pessoa in pessoas.items():
    if pessoa['idade'] < 18:
        menoresDe18[cpf] = pessoa

print('\nDicionário de todas as pessoas:')
for cpf, pessoa in pessoas.items():
    print(f'Nome: {pessoa["nome"]}, Idade: {pessoa["idade"]}, CPF: {cpf}')

print('\nDicionário das pessoas menores de 18 anos:')
for cpf, pessoa in menoresDe18.items():
    print(f'Nome: {pessoa["nome"]}, Idade: {pessoa["idade"]}, CPF: {cpf}')
