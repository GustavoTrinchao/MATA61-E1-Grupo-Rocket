#include <stdio.h>
#include "token.h"

extern char *yytext;
extern int yylex();

int main(int argc, char **argv) {

	token_t tok;

	while ((tok = yylex())) {
		if (tok == ERROR)
            printf("lexical error, char %s\n", yytext);
        else if (tok == NUM)
			printf("<token: %d, atrib: %s>\n", tok, yytext);
		else
			printf("<token: %d>\n", tok);
	}
}