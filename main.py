from teste import Teste

if __name__ == '__main__':
    print("[1] Teste da Integral")
    print("[2] Teste da Comparação")
    print("[3] Teste do Limite da Comparação")
    print("[4] Teste da Razão")

    res, teste = None, Teste()

    try:
        res = int(input("Escolha uma método de teste: "))
    except ValueError as e:
        for erro in e.args:
            print(erro)

    try:
        if res == 1:
            teste.integral(input("Insira sua função: "))
        elif res == 2:
            teste.comparacao(input("Digite a função An: "), input("Digite a função Bn: "))
        elif res == 3:
            teste.limite_comparacao(input("Digite a função An: "), input("Digite a função Bn: "))
        elif res == 4:
            teste.razao(input("Digite a função An: "), input("Digite a função An+1: "))
        else:
            print("Entrada inválida. Tente novamente!")
    except SyntaxError as e:
        for erro in e.args:
            print(erro)
