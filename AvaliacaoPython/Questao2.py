# 2. (Dados Aglomerados) Considere um sistema Python onde os dados são armazenados em dicionários. Nesse sistema existe
# um dicionario principal e o dicionário de backup. Cada vez que o dicionário principal atinge tamanho 5, ele imprime os
# dados na tela e apaga o seu conteúdo. Crie um programa que insira dados em um dicionário, realizando o backup a cada
# dado e excluindo os dados do dicionário principal quando ele atingir tamanho 5.

dicionarioPrincipal = {}

dicionarioBackup = {}

def imprimirLimparDicionario(dicionario):
    print('Informações registradas:')
    for chave, valor in dicionario.items():
        print(f'Chave: {chave}, Valor: {valor}')
    dicionario.clear()

while True:
    chave = input('Digite uma chave ou "sair" para encerrar: ')
    if chave == 'sair':
        break
    valor = input('Digite um valor: ')

    dicionarioPrincipal[chave] = valor

    dicionarioBackup[chave] = valor

    if len(dicionarioPrincipal) == 5:
        imprimirLimparDicionario(dicionarioPrincipal)

print('\nBackup realizado:')
for chave, valor in dicionarioBackup.items():
    print(f'Chave: {chave}, Valor: {valor}')
