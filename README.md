# Calculadora

Projeto desenvolvido durante as aulas de Python na FIAP.

Comecei fazendo no terminal com `input()` e `if/elif` para cada operação. Depois converti para uma página web simples.

## O que aprendi

- Criar funções separadas para cada operação (`somar`, `subtrair`, etc.)
- Tratar o erro de divisão por zero com `if b == 0`
- Usar dicionário para mapear operações a funções
- Estruturar um menu interativo com `while True`

## Versão Python (terminal)

```python
def dividir(a, b):
    if b == 0:
        print("Erro: divisão por zero!")
        return None
    return a / b

while True:
    print("1 - Soma | 2 - Subtração | 3 - Multiplicação | 4 - Divisão | 0 - Sair")
    opcao = input("Escolha: ")

    if opcao == "0":
        break

    a = float(input("Primeiro número: "))
    b = float(input("Segundo número: "))

    if opcao == "1": print(a + b)
    elif opcao == "2": print(a - b)
    elif opcao == "3": print(a * b)
    elif opcao == "4": print(dividir(a, b))
```

## Como rodar

```bash
python calculadora.py
```

Ou abra o `index.html` no navegador para a versão web.

---
Feito por Igor Davi · FIAP Engenharia de Software
