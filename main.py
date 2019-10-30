from math import factorial, e
import sympy as sp
import re


class Teste:
    x = sp.symbols("x")
    infinity = sp.oo

    def integral(self, funcao: str):
        funcao = funcao.replace('e', str(e))
        print("Função:", funcao)  #

        res_integral = sp.integrate(funcao, (self.x, 1, self.infinity))
        print("Integral:", res_integral)  #

        res_limite = sp.limit(res_integral, self.x, self.infinity)
        print("Limite: ", res_limite)  #

        if res_limite != self.infinity:
            print("Convergente")
        else:
            print("Divergente")

    def comparacao(self, an: str, bn: str):
        an = an.replace('e', str(e))
        bn = bn.replace('e', str(e))

        limite_an = sp.limit(an, self.x, self.infinity)
        limite_bn = sp.limit(bn, self.x, self.infinity)
        print(limite_an)  #
        print(limite_bn)  #

        if (limite_bn != self.infinity) and (limite_an <= limite_bn):
            print("An converge")
        else:
            if limite_bn == self.infinity and limite_bn <= limite_an:
                print("An diverge")

    def limite_comparacao(self, an: str, bn: str):
        an = an.replace('e', str(e))
        bn = bn.replace('e', str(e))

        funcao = F"({an})/({bn})"
        limite_funcao = sp.limit(funcao, self.x, self.infinity)
        limite_bn = sp.limit(bn, self.x, self.infinity)
        resposta = []

        if limite_funcao > 1:
            resposta.append("As funções tem o mesmo comportamento")
            if limite_bn == 0:
                resposta.append(" e ambas convergem")
            else:
                resposta.append(" e ambas divergem")
        else:
            resposta.append("As funções não possuem o mesmo comportamento")

        for resp in resposta:
            print(resp, end='')

    def razao(self, an: str, bn: str):
        an = an.replace('e', str(e))
        bn = bn.replace('e', str(e))
        pass


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
            teste.razao(input("Digite a função An: "), input("Digite a função Bn: "))
        else:
            print("Entrada inválida. Tente novamente!")
    except SyntaxError as e:
        for erro in e.args:
            print(erro)
