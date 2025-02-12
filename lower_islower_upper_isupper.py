#1. Convertendo Nome para Maiúsculas
#Peça para o usuário digitar o nome dele e exiba o nome todo em maiúsculas.

nome = input('Nome: ')
print(f'''Este é o nome inserido em letras maiúsculas:
      
      {nome.upper()}''')

#2. Contador de Letras Maiúsculas
#Peça ao usuário para inserir um texto e conte quantas letras são maiúsculas.

paragrafo = input('Insira o parágrafo para contar as letras maiúsculas: ')

contador = sum(1 for letra in paragrafo if letra.isupper())

print(f'Há {contador} letras maiúsculas neste trecho.')

#3. Verificando se o Texto Está Todo em Minúsculas
#Peça ao usuário para digitar um texto e verifique se ele já está completamente em letras minúsculas

frase = input('Insira uma frase: ')

if frase.islower():
    print('A frase possui somente letras em minúsculo.')
else:
    print('A frase contém letra maiúscula.')

#4. Verificador de letra minúscula
#Peça ao usuário para inserir uma frase sem letras maiúsculas, verifique se a condição foi atendida. Caso não tenha sido, printe o modo correto.

minuscula = input('Insira uma frase sem letras maiúsculas: ')

if minuscula.islower():
    print('Parabéns, a condição foi atendida, a frase não tem letras maiúsculas.')
else:
    print(f'Para atender à condição, a frase deveria ser: {minuscula.lower()}')