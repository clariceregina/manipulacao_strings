# 1. Peça ao usuário para inserir o nome de um arquivo e verifique se ele tem uma extensão válida (.txt, .csv ou .py).

arquivo = input('Digite o nome do arquivo PDF: ')

if arquivo.endswith('.pdf'):
    print('Arquivo válido.')
else:
    print('Extensão de arquivo inválida.')

# 2. Peça à pessoa usuária uma URLs, crie um programa que exiba se o link é seguro (que começa com "https").

url = input('Insira uma URL (link): ')

if url.startswith('https'):
    print('URL segura.')
else:
    print('Esta URL pode não ser segura, atente-se à navegação.')