import sys

EOL, NUM, PLUS, MINUS, TIMES, DIV, ERROR = range(7)

TOKEN_NAMES = {
    EOL: "EOL",
    NUM: "NUM",
    PLUS: "PLUS",
    MINUS: "MINUS",
    TIMES: "TIMES",
    DIV: "DIV",
    ERROR: "ERROR",
}


class AnalisadorLexico:

    def __init__(self, linha_tratada=""):
        self.set_entrada(linha_tratada)

    def set_entrada(self, linha_tratada):
        self.linha_tratada = linha_tratada
        self.pos = 0
        self.erro_de_caractere = None

    def get_caractere(self):
        return self.linha_tratada[self.pos] if self.pos < len(self.linha_tratada) else ""

    def yylex(self):
        while self.get_caractere() in (" ", "\t"):
            self.pos += 1

        if self.pos >= len(self.linha_tratada):
            return (EOL, None)

        caractere = self.linha_tratada[self.pos]

        if caractere.isdigit():
            start = self.pos
            while self.get_caractere().isdigit():
                self.pos += 1
            if self.get_caractere() == ".":
                self.pos += 1
                while self.get_caractere().isdigit():
                    self.pos += 1
            return (NUM, self.linha_tratada[start:self.pos])

        if caractere == "+":
            self.pos += 1
            return (PLUS, None)
        if caractere == "-":
            self.pos += 1
            return (MINUS, None)
        if caractere == "*":
            self.pos += 1
            return (TIMES, None)
        if caractere == "/":
            self.pos += 1
            return (DIV, None)

        self.erro_de_caractere = caractere
        self.pos += 1
        return (ERROR, None)

    def executar(self):
        for linha in sys.stdin:
            linha_tratada = linha.rstrip("\n")
            self.set_entrada(linha_tratada)

            token = 'inicializar'
            while token != EOL:
                token, attrib = self.yylex()

                if token == EOL:
                    pass #nop
                elif token == ERROR:
                    print(f"lexical error, char {self.erro_de_caractere}")
                elif token == NUM:
                    print(f"<token: {token}, atrib: {attrib}>")
                else:
                    print(f"<token: {token}>")


def main():
    al = AnalisadorLexico()
    al.executar()


if __name__ == "__main__":
    main()
