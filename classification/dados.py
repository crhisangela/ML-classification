import csv

def carregar_acessos():
    X = []
    Y = []

    arquivo = open('acesso.csv')
    leitor = csv.reader(arquivo)

    next(leitor)

    for acessou_home,acessou_como_funciona,acessou_contato, comprou in leitor:

        X.append([int(acessou_home),int(acessou_como_funciona)
            ,int(acessou_contato)])
        Y.append(int(comprou))

    return X, Y

def carregar_buscas():
    X = []
    Y = []

    arquivo = open('buscas.csv')
    leitor = csv.reader(arquivo)
    next(leitor)

    for home, busca, logado, comprou in leitor:
        dado = [int(home), busca, int(logado)]
        X.append(dado)
        Y.append(int(comprou))

        return X, Y