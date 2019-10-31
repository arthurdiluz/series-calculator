from math import factorial, e
import sympy as sp
import re


class Teste:
    n = sp.symbols("n")
    infinity = sp.oo

    def integral(self, funcao: str):

        funcao = funcao.replace('e', str(e))
        res_integral = sp.integrate(funcao, (self.n, 1, self.infinity))
        res_limite = sp.limit(res_integral, self.n, self.infinity)

        if res_limite != self.infinity:
            print("Convergente")
        else:
            print("Divergente")

    def comparacao(self, an: str, bn: str):
        an = an.replace('e', str(e))
        bn = bn.replace('e', str(e))

        limite_an = sp.limit(an, self.n, self.infinity)
        limite_bn = sp.limit(bn, self.n, self.infinity)
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
        resposta = []
        print(funcao)  #

        limite_funcao = sp.limit(funcao, self.n, self.infinity)
        print("Limite função:", limite_funcao)  #

        if limite_funcao > 0:
            resposta.append("As funções tem o mesmo comportamento")
        else:
            print("As funções não possuem o mesmo comportamento")
            return

        if bn == '1':
            is_especifico = self.identificar_serie(an)
        else:
            is_especifico = self.identificar_serie(bn)

        if bool(is_especifico):
            resposta.append(F"e ambas {is_especifico}")
            for resp in resposta:
                print(resp, end='')
            return
        else:
            print("moiô")  #

        # GENÉRICO

        limite_bn = sp.limit(bn, self.n, self.infinity)
        print("Limite bn:", limite_bn)  #

        if limite_bn == 0:
            resposta.append(" e ambas convergem")
        else:
            resposta.append(" e ambas divergem")

        for resp in resposta:
            print(resp, end='')

    def razao(self, an: str, bn: str):
        an = an.replace('e', str(e))
        bn = bn.replace('e', str(e))
        pass

    def identificar_serie(self, funcao) -> str:

        def is_hiper_harmonica(regex: list) -> str:
            if regex:
                print("Regex:", regex)
                p = regex[0]
                if '/' in p:
                    p = re.findall(r"\d+", p)
                    p = float(float(p[0]) / float(p[1]))
                else:
                    p = int(p[0])

                if p > 1:
                    return "convergem"
                else:
                    return "divergem"
            else:
                return ""

        def is_geometrico(regex: list) -> str:
            if regex:

                print("Regex:", regex)
                p = regex[0]

                if '/' in p:
                    p = re.findall(r"\d+", p)
                    p = float(float(p[0]) / float(p[1]))
                else:
                    p = int(p[0])

                if p > 1:
                    return "convergem"
                else:
                    return "divergem"
            else:
                return ""

        # MAIN

        try:
            hiper_harmonica = is_hiper_harmonica(
                (re.findall(r"\d+\/?\d*", (re.findall(r"\*{2}\s?\(?\d+\/?\d?\){2,}", funcao))[-1]))[0]
            )
            if hiper_harmonica:
                return hiper_harmonica
        except IndexError:
            pass

        try:
            geometrico = is_geometrico(
                (re.findall(r"\d+\/?\d*", (re.findall(r"\(\s*\d+\s*\/?\s*\d*\s*\)?\s*\*{2}\s*n{1}", funcao))[0]))[0]
            )
            if geometrico:
                return geometrico
        except IndexError:
            pass

        return ""


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
