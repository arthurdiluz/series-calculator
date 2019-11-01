from math import factorial, e
import sympy as sp
import re


class Teste:
    n = sp.symbols('n')
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
        res_an = eval(an.replace('n', '2'))
        res_bn = eval(bn.replace('n', '2'))
        is_especifico = self.identificar_serie(bn)

        if bool(is_especifico) and (is_especifico == "convergem") and (res_an <= res_bn):
            print("an converge")
            return
        elif bool(is_especifico) and (is_especifico == "divergem") and (res_bn <= res_an):
            print("an diverge")
            return
        else:
            pass

        limite_bn = sp.limit(bn, self.n, self.infinity)

        if (res_an <= res_bn) and limite_bn == 0:
            print("An converge")
        elif (limite_bn != 0) and (res_bn <= res_an):
            print("An diverge")
        else:
            print("Não satisfaz o Teste da Comparação")

    def limite_comparacao(self, an: str, bn: str):
        an = an.replace('e', str(e))
        bn = bn.replace('e', str(e))

        if not bn:
            print("A função não se a aplica ao teste de limite de comparação")
            return

        funcao = F"({an})/({bn})"
        limite_funcao = sp.limit(funcao, self.n, self.infinity)
        resposta = []

        if limite_funcao > 0:
            resposta.append("As funções tem o mesmo comportamento")
        else:
            print("As funções não possuem o mesmo comportamento")
            return

        is_especifico = self.identificar_serie(funcao)

        if bool(is_especifico):
            resposta.append(F"e ambas {is_especifico}")
            for resp in resposta:
                print(resp, end='')
            return

        limite_bn = sp.limit(bn, self.n, self.infinity)

        if limite_bn == 0:
            resposta.append(" e ambas convergem")
        else:
            resposta.append(" e ambas divergem")

        for resp in resposta:
            print(resp, end='')

    def razao(self, an: str, an1: str):
        an = an.replace('e', str(e))
        an1 = an1.replace('e', str(e))

        if not ('!' in an) and not('!' in an1):
            is_especifico = self.identificar_serie(F"{an1}/{an}")

            if is_especifico:
                print(is_especifico)
                return
            else:
                res_limite = sp.limit(F"{an1}/{an}", self.n, self.infinity)
                print("Limite:", res_limite)

                if res_limite > 1:
                    print("A série diverge")
                elif res_limite < 1:
                    print("A série converge")
                else:
                    print("A série é inconclusiva")
                return
        else:
            #an+1
            for i in range(len(an1)):
                if an1[i] == '!' and an1[i-1] == ')':
                    print('O Sistema não é capaz de resolver fatorial com expressões.')
                    return
            else:
                an1 = an1.replace(
                    re.findall("\d+!", an1)[0],
                    str(factorial(int((re.findall(r"\d+", (re.findall(r"\d+!", an1))[0]))[0])))
                )

            # an
            for i in range(len(an)):
                if an[i] == '!' and an[i-1] == ')':
                    print('O Sistema não é capaz de resolver fatorial com expressões.')
                    return
            else:
                an = an.replace(
                    re.findall("\d+!", an)[0],
                    str(factorial(int((re.findall(r"\d+", (re.findall(r"\d+!", an))[0]))[0])))
                )

            limite = sp.limit(F"{an1}/{an}", self.n, self.infinity)

            if limite < 1:
                print("A série converge")
            elif limite > 1:
                print("A série diverge")
            else:
                print("A série é inconclusiva")

    def identificar_serie(self, funcao) -> str:

        def is_harmonica(regex: list) -> str:
            if regex:
                print("Regex harmonica:", regex)
                p = regex[0]
                if '/' in p:
                    p = re.findall(r"\d+", p)
                    p = float(float(p[0]) / float(p[1]))
                else:
                    p = int(p[0])

                if p > 1:
                    return "convergem"
                elif p < 1:
                    return "divergem"
                else:
                    return F"divergem porque a função é hiperarmônica"
            else:
                return ""

        def is_geometrico(regex: list) -> str:
            if regex:

                print("Regex geometrico:", regex)
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

        def is_telescopica(regex: list) -> str:
            print("Regex0 teles:", regex[0])
            print("Regex1 teles:", regex[1])

            if regex[0] or regex[1]:
                print(F"Regex: {regex} => {type(regex[0])} e {type(regex[1])}")
                return "convergem"
            else:
                return ""

        # MAIN

        try:
            harmonica = is_harmonica(
                (re.findall(r"\d+\/?\d*", (re.findall(r"\*{2}\s?\(?\d+\/?\d?\){2,}", funcao))[-1]))[0]
            )
            if harmonica:
                return harmonica
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

        try:
            telescopica = is_telescopica([
                (re.findall(r"1\s?\/\s?\(\s?n\s?\*\s?\(\s?n\s?\+\s?1?\s?\)\s?\)", funcao))[0],
                (re.findall(r"ln\(\s?\(\s?n\s?\+\s?1\s?\)\s?\/\s?1\s?\)", funcao))[0]
            ])

            print("T:", telescopica, "bool:", bool(telescopica))

            if telescopica:
                return telescopica
        except IndexError:
            pass

        return ""
