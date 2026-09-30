# Exercício 1 (E1) - Parte 2

## Equipe
- Membro 1: Giovane Santana
- Membro 2: Gustavo Trinchão
- Membro 3: Joaquim Neto
- Membro 4: Miguel Mota
- Membro 5: Théo Farias

## Descrição
Analisador léxico para expressões aritméticas com números inteiros e reais (com '.') e operadores +, -, *, /, implementado com C e Flex.

## Arquivos
- `e1.l` - Especificação Flex do analisador léxico
- `main.c` - Programa principal que chama yylex()
- `token.h` - Definição dos códigos de tokens
- `makefile` - Comandos para compilar/testar
- `tests/` - Casos de teste (arquivos .in e .ora)

## Como compilar
```bash
make compile
```
Gera o executável `e1` usando flex e gcc.

## Como executar
```bash
make run
```
Abre o executável em prompt para entrada da expressão a ser analisada.
Ou diretamente:
```bash
echo "90 * 100 / 18.0 - 48 + 77" | ./e1
```

## Como testar
```bash
make test
```
Executa todos os testes na pasta `tests/` comparando saída com arquivos `.ora`.

## Formato de saída
- Tokens NUM: `<token: 1, atrib: lexema>`
- Outros tokens: `<token: código>`
- Erro léxico: `lexical error, char X`

## Valores de tokens (conforme token.h)
- EOL = 0
- NUM = 1
- PLUS = 2
- MINUS = 3
- TIMES = 4
- DIV = 5
- ERROR = 6