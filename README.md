# RegEx Parser
## Trabalho final de Compiladores do curso de Ciência da Computação da UFSM.
### Gustavo Fantinel, Mariano Dorneles e René Ferrari

O programa foi desenvolvido em python3, utilizando ANTLR para lexing e parsing da ER.
Os comandos foram testados em um terminal linux.

Deve-se instalar o ANTLR3 para python3:
```
pip3 install antlr4-python3-runtime
```

Para compilar use o seguinte comando:
```
java -Xmx500M -cp antlr-4.8-complete.jar org.antlr.v4.Tool -Dlanguage=Python3 gr.g4
``` 

Por fim, é necessário rodar o programa gr.py, onde a main está localizada:

```
python3 gr.py
```

Ao executar o programa, insira uma ER no seguinte formato, sem espaços:
```
Insira a ER: a*b*
```

Se a ER for válida, retornará a árvore de derivação, juntamente com a mensagem de que ela é válida.

```
ER Válida!
Arvore de derivação: (re (simple_re (concat (basic_re (star (char_ a) *)) (simple_re (basic_re (star (char_ b) *))))))
['a', '*', 'b', '*', '?']
```

Caso contrário, retornará uma mensagem de erro.

Se válida, o programa permite que sejam inseridas palavras para teste, até o término de sua execução (CTRL+C)

```
Insira a palavra a ser testada: aabb
```

O programa mostrará toda a tentativa de encontrar um caminho no autômato, logo depois, exibirá uma mensagem que dirá se a palavra está dentro da ER ou não:

```
Q2 - ε -> [Q2, Q0, Q3, Q6, Q4, Q7]
Q0 - a -> Q1
Q1 - ε -> [Q1, Q0, Q3, Q6, Q4, Q7]
Q0 - a -> Q1
Q1 - ε -> [Q1, Q0, Q3, Q6, Q4, Q7]
Q4 - b -> Q5
Q5 - ε -> [Q5, Q4, Q7]
Q4 - b -> Q5
Q5 - ε -> [Q5, Q4, Q7]
A palavra está dentro da ER apresentada!
```