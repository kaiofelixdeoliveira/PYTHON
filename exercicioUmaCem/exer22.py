nome=input('digite algo')
print('qual o tipo primitivo?',type(nome))
print('é numerico?',nome.isnumeric())
print('é alfanumerico?',nome.isalnum())
print('é alfabético?',nome.isalpha())
print('é maiuscula?',nome.upper())
print('é minuscula?',nome.lower())
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))