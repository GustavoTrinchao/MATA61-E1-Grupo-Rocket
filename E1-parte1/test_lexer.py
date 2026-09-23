import io
import unittest
from unittest.mock import patch

from lexer import EOL, NUM, PLUS, MINUS, TIMES, DIV, ERROR, AnalisadorLexico, main


class TestYylex(unittest.TestCase):
    def test_integer(self):
        lx = AnalisadorLexico("42")
        self.assertEqual(lx.yylex(), (NUM, "42"))
        self.assertEqual(lx.yylex(), (EOL, None))

    def test_real(self):
        lx = AnalisadorLexico("18.0")
        self.assertEqual(lx.yylex(), (NUM, "18.0"))
        self.assertEqual(lx.yylex(), (EOL, None))

    def test_operators(self):
        lx = AnalisadorLexico("+ - * /")
        self.assertEqual(lx.yylex(), (PLUS, None))
        self.assertEqual(lx.yylex(), (MINUS, None))
        self.assertEqual(lx.yylex(), (TIMES, None))
        self.assertEqual(lx.yylex(), (DIV, None))
        self.assertEqual(lx.yylex(), (EOL, None))

    def test_full_expression(self):
        lx = AnalisadorLexico("90 * 100 / 18.0 - 48 + 77")
        expected = [
            (NUM, "90"), (TIMES, None), (NUM, "100"), (DIV, None),
            (NUM, "18.0"), (MINUS, None), (NUM, "48"), (PLUS, None),
            (NUM, "77"), (EOL, None),
        ]
        for exp in expected:
            self.assertEqual(lx.yylex(), exp)

    def test_invalid_char_is_reported_and_lexing_continues(self):
        lx = AnalisadorLexico(".0")
        token, attrib = lx.yylex()
        self.assertEqual(token, ERROR)
        self.assertEqual(lx.erro_de_caractere, ".")
        # apos o erro, o lexico continua e reconhece o restante
        self.assertEqual(lx.yylex(), (NUM, "0"))
        self.assertEqual(lx.yylex(), (EOL, None))

    def test_invalid_char_letter(self):
        lx = AnalisadorLexico("3 & 4")
        self.assertEqual(lx.yylex(), (NUM, "3"))
        token, _ = lx.yylex()
        self.assertEqual(token, ERROR)
        self.assertEqual(lx.erro_de_caractere, "&")
        self.assertEqual(lx.yylex(), (NUM, "4"))

    def test_empty_line(self):
        lx = AnalisadorLexico("")
        self.assertEqual(lx.yylex(), (EOL, None))

    def test_whitespace_only(self):
        lx = AnalisadorLexico("   \t  ")
        self.assertEqual(lx.yylex(), (EOL, None))

    def test_multiple_spaces_between_tokens(self):
        lx = AnalisadorLexico("  10   +   20  ")
        self.assertEqual(lx.yylex(), (NUM, "10"))
        self.assertEqual(lx.yylex(), (PLUS, None))
        self.assertEqual(lx.yylex(), (NUM, "20"))
        self.assertEqual(lx.yylex(), (EOL, None))


class TestMainOutput(unittest.TestCase):
    def run_main(self, input_text):
        stdin = io.StringIO(input_text)
        stdout = io.StringIO()
        with patch("sys.stdin", stdin), patch("sys.stdout", stdout):
            main()
        return stdout.getvalue()

    def test_valid_expression_output(self):
        out = self.run_main("90 * 100 / 18.0 - 48 + 77\n")
        expected = (
            "<token: 1, atrib: 90>\n"
            "<token: 4>\n"
            "<token: 1, atrib: 100>\n"
            "<token: 5>\n"
            "<token: 1, atrib: 18.0>\n"
            "<token: 3>\n"
            "<token: 1, atrib: 48>\n"
            "<token: 2>\n"
            "<token: 1, atrib: 77>\n"
        )
        self.assertEqual(out, expected)

    def test_invalid_expression_output(self):
        out = self.run_main("90 * 100 / .0\n")
        expected = (
            "<token: 1, atrib: 90>\n"
            "<token: 4>\n"
            "<token: 1, atrib: 100>\n"
            "<token: 5>\n"
            "lexical error, char .\n"
            "<token: 1, atrib: 0>\n"
        )
        self.assertEqual(out, expected)

    def test_multiple_lines(self):
        out = self.run_main("1 + 2\n3 * 4\n")
        expected = (
            "<token: 1, atrib: 1>\n"
            "<token: 2>\n"
            "<token: 1, atrib: 2>\n"
            "<token: 1, atrib: 3>\n"
            "<token: 4>\n"
            "<token: 1, atrib: 4>\n"
        )
        self.assertEqual(out, expected)


if __name__ == "__main__":
    unittest.main()
