/* recognize tokens for the calculator */

%option noyywrap
%{
#include "token.h"
%}

DIGIT   [0-9]
INTEGER {DIGIT}+
FLOAT   {DIGIT}+"."{DIGIT}+

%%

[ \t]+              ;
\n                  {return EOL;}

{FLOAT}             {return NUM;}
{INTEGER}           {return NUM;}
"."                 {return ERROR;}
"+"                 {return PLUS;}
"-"                 {return MINUS;}
"*"                 {return TIMES;}
"/"                 {return DIV;}
.                   {return ERROR;}

%%