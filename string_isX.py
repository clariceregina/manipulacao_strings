# 1. Crie um programa que leia uma string do usuário e verifique se ela contém apenas letras (sem números ou caracteres especiais).

palavra = input('Insira uma palavra: ')

if palavra.isalpha():
    print('A frase contém somente letras.')
else:
    print('A frase contém caracteres diferentes de letras.')

# 2. Solicite ao usuário que digite uma string e verifique se ela contém apenas letras e números (sem espaços ou caracteres especiais).

palavra_2 = input('Insira uma palavra: ')

if palavra_2.isalnum():
    print('A frase contém somente letras e números.')
else:
    print('A frase contém caracteres especiais e/ou espaço.')

# 3. Peça ao usuário para digitar uma string e verifique se ela contém apenas dígitos decimais.

# isdecimal() verifica somente números inteiros positivos

numero = input('Insira um número decimal: ')

if numero.isdecimal():
    print('Recomendamos refazer. O número informado não é decimal. ')
else:
    print('Está correto! É um número decimal.')

# Crie um programa que leia uma string e verifique se ela contém apenas espaços em branco. Caso sim, imprima "A string contém apenas espaços"; caso contrário, "A string contém outros caracteres".

espaco = input('Insira um espaço em branco:')

if espaco.isspace():
    print('A string contém apenas espaços.')
else:
    print('A string contém outros caracteres.')

# Solicite ao usuário que digite uma frase e verifique se ela está no formato de título (primeira letra de cada palavra em maiúscula). Se estiver, imprima "A string está no formato título"; caso contrário, "A string não está no formato título".

titulo = input('Insira o título de um livro: ')

if titulo.istitle():
    print('O título está escrito no formato correto.')
else:
    print('Por favor, escreva em formato de título, primeira letra de cada palavra maiúscula.')