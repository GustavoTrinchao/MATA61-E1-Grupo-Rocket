CC = gcc
FLEX = flex
CFLAGS = -Wall -Wextra

.PHONY: compile test run clean

compile: e1

e1: lex.yy.c main.c token.h
	$(CC) $(CFLAGS) -o e1 lex.yy.c main.c

lex.yy.c: e1.l token.h
	$(FLEX) e1.l

test: compile
	@echo "=== Executando testes ==="
	@passed=0; failed=0; \
	for infile in tests/*.in; do \
		[ -f "$$infile" ] || continue; \
		base=$$(basename "$$infile" .in); \
		orafile="tests/$$base.ora"; \
		echo -n "Teste $$base: "; \
		if [ -f "$$orafile" ]; then \
			output=$$(cat "$$infile" | ./e1 | tr -d '\r'); \
			expected=$$(tr -d '\r' < "$$orafile"); \
			if [ "$$output" = "$$expected" ]; then \
				echo "Sucesso"; \
				passed=$$((passed + 1)); \
			else \
				echo "Falha"; \
				echo "  Esperado:"; \
				echo "$$expected" | sed 's/^/    /'; \
				echo "  Obtido:"; \
				echo "$$output" | sed 's/^/    /'; \
				failed=$$((failed + 1)); \
			fi; \
		else \
			echo "Teste pulado (sem .ora)"; \
		fi; \
	done; \
	echo "=== Sumário: $$passed testes passaram, $$failed falharam ==="; \
	[ $$failed -eq 0 ] || exit 1

run: compile
	@echo "Digite a expressão a interpretar:"
	@./e1


clean:
	@rm -f e1 lex.yy.c
