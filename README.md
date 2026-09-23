# Exercício 1 (E1) - Análise Léxica

Fazer um analisador léxico para expressões aritméticas com números inteiros e reais
(com '.') e os operadores aritméticos ```+  -  *  e  / ```.

**Parte 1** : 
O analisador léxico deve ser implementado em uma linguagem de alto nível popular (por exemplo, python, C ou C++).

**Parte 2** : 
O analisador léxico deve ser implementado com Flex e C.

## Entrega 

### Instruções para Configuração do Repositório da Equipe

Este exercício possui duas partes (Parte 1 e Parte 2). 
O trabalho deve ser feito em equipe. 
Siga os passos abaixo rigorosamente para configurar o ambiente do seu grupo:

### 1. Criar o Repositório Privado da Equipe
1. Um dos membros da equipe deve acessar o GitHub e criar um novo repositório.
2. Configure o repositório como **Private** (Privado).
3. **Não** adicione README, .gitignore ou licença (deixe o repositório completamente vazio).
4. Nomeie o repositório seguindo o padrão: `MATA61-E1-Grupo-X` (substitua X pelo nome do seu grupo).

### 2. Importar o Conteúdo da Especificação
Abra o terminal na sua máquina e execute os seguintes comandos para clonar o repositório da disciplina e empurrá-lo para o repositório privado do seu grupo:

```bash
# Clone o repositório base da disciplina usando a opção --bare
git clone --bare https://github.com/MATA61-20262/E1.git

# Acesse a pasta criada
cd E1.git

# Envie o conteúdo para o novo repositório privado do seu grupo
# (Substitua a URL abaixo pela URL do repositório que seu grupo criou)
git push --mirror https://github.com

# Apague a pasta temporária E1.git da sua máquina
cd ..
rm -rf E1.git
```

Agora, **clone o repositório privado do seu grupo* normalmente na sua máquina para começar a trabalhar.

### 3. Adicionar a Professora e a Equipe
1. No repositório privado do grupo, vá em **Settings** > **Collaborators** > **Add people**.
2. Adicione os outros membros da equipe.
3. Adicione o usuário da professora: `christinaflachufba`.

---

## Como Entregar as Partes 1 e 2

Para facilitar a correção, **não faça commits diretamente na branch `main`**. Use o fluxo de Pull Requests (PR):

### Entrega da Parte 1:
1. Criem uma branch chamada `parte-1` (`git checkout -b parte-1`).
2. Desenvolvam a solução da primeira parte nesta branch.
3. Abram um **Pull Request** da branch `parte-1` para a branch `main` dentro do próprio repositório de vocês.
4. **Não deem "Merge" no PR!** 
O link desse Pull Request aberto será a entrega de vocês na plataforma da disciplina.
A professora usará este PR para comentar no código e dar a nota.

### Entrega da Parte 2:
1. Após o prazo da Parte 1, criem uma nova branch a partir da `main` chamada `parte-2` (`git checkout -b parte-2`).
2. Desenvolvam a segunda parte.
3. Abram um novo **Pull Request** da branch `parte-2` para a branch `main`.
4. Deixem o PR aberto para a correção da professora.

---

## Descrição Geral

O programa recebe uma expressão aritmética digitada na entrada padrão, apenas uma expressão por linha, 
e mostra, na saída padrão, o código da categoria de cada token identificado (valor inteiro)
e, para constantes númericas, também retorna o lexema (cadeia de caracteres).
Não é preciso converter para o lexema para int ou float.

### Valores de tokens

Usar os códigos de token de 1 a 5 para uniformizar e facilitar a correção.

```
NUM         1
PLUS        2
MINUS       3
TIMES       4
DIV         5
```
- Usar ERROR, com valor 6, para reportar erro léxico.

###  Exemplos

#### Entrada válida

- Entrada:

```90 * 100 / 18.0 - 48 + 77```

- Saída esperada (seguir o padrão):

```
<token: 1, atrib: 90>
<token: 4>
<token: 1, atrib: 100>
<token: 5>
<token: 1, atrib: 18.0>
<token: 3>
<token: 1, atrib: 48>
<token: 2>
<token: 1, atrib: 77>
```

#### Entrada com constante real malformada

- Entrada inválida:

```90 * 100 / .0 ```

- Saída esperada:

```
<token: 1, atrib: 90>
<token: 4>
<token: 1, atrib: 100>
<token: 5>
lexical error, char .
<token: 1, atrib: 0>
```

*Observação:* O erro está na formação da constante, sem ao menos um dígito decimal antes do '.', mas não reportaremos o erro léxico com esse detalhe no exercício.

#### Entrada com símbolo desconhecido

- Entrada inválida:

```90 ! 100 / 18.0 ```

- Saída esperada:

```
<token: 1, atrib: 90>
lexical error, char !
<token: 1, atrib: 100>
<token: 5>
<token: 1, atrib: 18.0>
```

*Observação:* Esse erro (símbolo desconhecido) é fácil de ser detectado e poderia ser reportado de modo mais amigável, 
mas preferimos deixar a mensagem de erro mais genérica.

### Testes

Considerar, no mínimo os cenários indicados em \tests\cenarios.md.
Os arquivos de teste devem ser texto simples. Os arquivos de entrada, com uma linha contendo uma expressão aritmética,
devem ter extensão '.in'; os arquivos com a saída esperada (oráculo) devem ter extensão '.ora' e seguir o formato de
saída ilustrado nos exemplos anteriores.

## (Parte 1) Análise léxica (implementar em linguagem de programação de alto nível)

**Analisador léxico para expressões aritméticas.**

- A função de análise léxica deve se chamar ```yylex()``` e retornar um valor inteiro que corresponde ao código do token reconhecido.
O lexema deve sempre estar acessível em uma variável chamada de ```yytext```.
Por exemplo, ao reconhecer um constante numérica "100", a função ```yylex()``` deve retornar o valor 1 (código NUM), 
e a variável ```yytext``` deve conter o lexema "100".
Se reconhecer o operador de adição '+', deve retornar o valor 2 (código PLUS), e 
a variável ```yytext``` deve conter o lexema "+" (ainda que esse lexema não seja usado na prática).

- Usar o token ERROR, com valor 6, para indicar erro léxico.
- Definir uma função main() que chama a função yylex() e imprime as informações indicadas para cada token retornado na saída padrão.

### Testes

Colocar mais testes na pasta \tests para os cenários indicados em \tests\cenarios.md

### Entrega

A entrega da Parte 1 do exercício E1 deve ser feita apenas via GitHub,
com o código fonte de sua implementação na **pasta E1-parte1**.

Arquivos:
- ./E1-parte1/README.md, com nomes dos membros da equipe (primeiras linhas, como comentário e orientações para compilar, executar e testar seu código.
- ./E1-parte1/makefile, com opções 'compile' e 'test'
- ./E1-parte1/<arquivos com código fonte>
- Pasta ./E1-parte1/'tests', contendo seus testes I/O para os cenários indicados em \tests\cenarios.md

---

## (Parte 2) Análise léxica com Flex

Considerar a Descrição Geral fornecida para este exercício. 
Implementar um analisador léxico para a linguagem de expressões usando Flex e C.

Usar o arquivo token.h: 

```
/* token.h */

typedef enum {
        EOL=0,       // 0 - Final de linha
        NUM,         // 1
        PLUS,        // 2
        MINUS,       // 3
        TIMES,       // 4
        DIV,         // 5
        ERROR,       // 6 - Erro léxico - pode ficar fora do tipo enumerado e ser definido como constante.
} token_t; 
```

---

### Entrega

A entrega da Parte 2 do exercício E1 deve ser feita apenas via GitHub,
com o código fonte de sua implementação na **pasta E1-parte2**.

Arquivos:
- ./E1-parte2/README.md, com nomes dos membros da equipe (primeiras linhas, como comentário e orientações para compilar, executar e testar seu código.
- ./E1-parte2/makefile, com opções 'compile' e 'test'
- ./E1-parte2/<arquivos com código fonte>, incluindo um arquivo Flex, um arquivo main.c, que chama yylex() --  e o arquivo token.h. Esses arquivos são suficientes.
- Pasta ./E1-parte2/'tests', contendo seus testes I/O para os cenários indicados em \tests\cenarios.md



