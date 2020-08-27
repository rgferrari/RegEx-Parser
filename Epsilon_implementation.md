Explicação da implementação do vazio na gramática atual

Na gramática presente no arquivo gr.g4, foi adicionado como char_ (linha 13) o token 'E', o qual representará o vazio nas expressões.

No arquivo automata.py, nas linhas 104 e 105, foi adicionada a seguinte lógica para a implementação do vazio quando encontrado o token 'E':

```
elif (token == 'E'):
            stack.append(fromNull())
```

Exemplo de uso:
(a|E)b - Essa ER deve aceitar as palavras 'b' ou 'ab'.