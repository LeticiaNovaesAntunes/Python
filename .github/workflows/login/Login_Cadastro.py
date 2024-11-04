def nome():
    nome = input("Insira o nome: ")

    return nome

def senha():
    senha = input('Senha: ')

    return senha

def autentica(senha, login):
    if senha == '123' and login == 'Lara':
        print('Bem Vinda!!')
    else:
        print('Erro')

senha = senha()
login = nome()

autentica(senha, login)
