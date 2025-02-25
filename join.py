# 1. Crie um programa que peça ao usuário para inserir cinco palavras separadas por espaço. Em seguida, utilize o método join() para juntar essas palavras em uma única string separada por vírgulas.

palavras = input('Digite cinco palavras seperadas por espaço: ').split()
resultado = ", ".join(palavras)
print(resultado)