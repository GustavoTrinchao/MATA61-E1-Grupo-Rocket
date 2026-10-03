**cenario1:**

**Entrada:**\
90 * 100 / 18.0 - 48 + 77

**Saida:**\
<token: 1, atrib: 90>\
<token: 4>\
<token: 1, atrib: 100>\
<token: 5>\
<token: 1, atrib: 18.0>\
<token: 3>\
<token: 1, atrib: 48>\
<token: 2>\
<token: 1, atrib: 77>

**cenario2:**

**Entrada:**\
0.5+12.99*3

**Saida:**\
<token: 1, atrib: 0.5>\
<token: 2>\
<token: 1, atrib: 12.99>\
<token: 4>\
<token: 1, atrib: 3>

**cenario3:**

**Entrada:**\
45 $ 2

**Saida:**\
<token: 1, atrib: 45>\
lexical error, char $\
<token: 1, atrib: 2>

**cenario4:**

**Entrada:**\
90 * 100 / .0 - 777

**Saida:**\
<token: 1, atrib: 90>\
<token: 4>\
<token: 1, atrib: 100>\
<token: 5>\
lexical error, char .\
<token: 1, atrib: 0>\
<token: 3>\
<token: 1, atrib: 777>

**exemplo1:**

**Entrada:**\
2+3

**Saida:**\
<token: 1, atrib: 2>\
<token: 2>\
<token: 1, atrib: 3>
