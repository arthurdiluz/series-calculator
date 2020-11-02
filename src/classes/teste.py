from math import factorial, e, log, log10
import math
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
        val_n = input("Insira o valor de n: ") or '3'
        is_especifico = self.identificar_serie(bn)

        res_an = eval(an.replace('n', val_n))
        res_bn = eval(bn.replace('n', val_n))

        if is_especifico:
            if (is_especifico == "convergem") and (res_an <= res_bn):
                print("an converge")
                return
            elif (is_especifico == "divergem") and (res_bn <= res_an):
                print("an diverge")
                return
            else:
                print("A série não satisfaz nenhuma condição")
                return

        limite_bn = sp.limit(bn, self.n, self.infinity)

        if (res_an <= res_bn) and (limite_bn == 0):
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
        an = an.replace('e', str(math.e))
        an1 = an1.replace('e', str(math.e))

        if not ('!' in an) and not('!' in an1):
            res_limite = sp.limit(F"{an1}/{an}", self.n, self.infinity)

            if res_limite > 1:
                print("A série diverge")
            elif res_limite < 1:
                print("A série converge")
            else:
                print("A série é inconclusiva")
            return
        else:
            try:
                limite = sp.limit(
                    F"{self.resolver_fatorial(an1)}/{self.resolver_fatorial(an)}", self.n, self.infinity
                )
            except ValueError as e:
                print("Erro:", e)
                return

            if limite < 1:
                print("A série converge")
            elif limite > 1:
                print("A série diverge")
            else:
                print("A série é inconclusiva")

    def resolver_fatorial(self, funcao: str):
        for i in range(len(funcao)):
            if funcao[i] == '!' and (funcao[i - 1] == ')' or funcao[i - 1] == 'n'):
                raise ValueError("O sistema não é capaz de resolver fatorial com expressões.")
        else:
            valor = funcao.replace(
                re.findall("\d+!", funcao)[0],
                str(factorial(int((re.findall(r"\d+", (re.findall(r"\d+!", funcao))[0]))[0])))
            )

            return valor

    def identificar_serie(self, funcao) -> str:
        try:
            hiperarmonica = self.is_hiperarmonica(
                re.findall(r"\d+\/?\d*", (re.findall(r"\*{2}\s?\(?\d+\/?\d?\){2,}", funcao))[-1])
            )

            if hiperarmonica:
                return hiperarmonica
        except IndexError:
            pass

        try:
            harmonica = self.is_harmonica(re.findall(r"1\s?\/\s?n", funcao))

            if harmonica:
                return harmonica
        except IndexError as e:
            pass

        try:
            geometrico = self.is_geometrico((re.findall(
                    r"\d+\/?\d*", (re.findall(r"\(\s*\d+\s*\/?\s*\d*\s*\)?\s*\*{2}\s*n{1}", funcao))[0]
                    ))[0])
            if geometrico:
                return geometrico
        except IndexError:
            pass

        try:
            telescopica = self.is_telescopica([
                (re.findall(r"1\s?\/\s?\(\s?n\s?\*\s?\(\s?n\s?\+\s?1?\s?\)\s?\)", funcao))[0],
                (re.findall(r"log\(\s?\(\s?n\s?\+\s?1\s?\)\s?\/\s?1\s?\)", funcao))[0]
            ])

            if telescopica:
                return telescopica
        except IndexError:
            pass

        return ""

    def is_hiperarmonica(self, regex: list) -> str:
        if regex:
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
                return ""

    def is_harmonica(self, regex: list) -> str:
        if regex:
            return "divergem"
        else:
            return ""

    def is_geometrico(self, regex: list) -> str:
        if regex:
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

    def is_telescopica(self, regex: list) -> str:
        if regex[0] or regex[1]:
            return "convergem"
        else:
            return ""
