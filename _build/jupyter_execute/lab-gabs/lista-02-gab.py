#!/usr/bin/env python
# coding: utf-8

# # Lista de exercícios 2
# 
# **Resolva todos os problemas por computação e registre as suas respostas no questionário disponibilizado no ambiente virtual de aprendizagem.**
# <hr>

# **Exercício 1.** Defina uma variável chamada `primos` e atribua a ela uma lista usando um laço `for` para preenchê-la com os números primos de 2 a 13, inclusive. Enfim, atribua o número 17 a uma variável chamada `p` e adicione `p` ao final da lista. Imprima a nova lista inteira.

# **Exercício 2.** Escreva um programa que gera todos os números ímpares de `1` a `n`. Defina `n` no início do programa e use um laço `while` para computar os números. (Certifique-se que se `n` é um número par, o maior número ímpar gerado seja `n-1`.

# **Exercício 3.** Defina a seguinte lista aninhada:
# 
# ```python
#  q = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h']]
# ```
# 
# Use indexação para extrair: 
# 
# a. a letra `'a'`;
# 
# b. a lista `['d','e','f']`;
# 
# c. o último elemento `'h'`;
# 
# d. o elemento `'d'`;
# 
# e. o elemento `'g'`.
# 
# Considere o seguinte código: 
# 
# ```python
# for i in q:
#     for j in range(len(?)):
#         print ??[j]
# ```
# 
# Para que sejam impressos todos os elementos da lista `q`, `?` e `??` devem ser substituídos por letras, convenientemente, de modo que o código realize o que pretende. Faças as modificações devidas para essa finalidade.

# **Exercício 4.** Um triângulo arbitrário pode ser descrito pelas coordenadas de seus três vértices: $(x_1,y_1)$, $(x_2,y_2)$ e $(x_3,y_3)$, orientados no sentido anti-horário. A área do triângulo é dada pela fórmula:
# 
# $$A = \frac{1}{2}
# \begin{vmatrix}
# x_1 & y_1 & 1 \\
# x_2 & y_2 & 1 \\
# x_3 & y_3 & 1 \\
# \end{vmatrix}$$
# 
# Escreva uma função `area(vertices)` que calcule a área $A$ de um triângulo cujos vértices são especificados pelo argumento `vertices`, o qual deve ser dado por uma lista aninhada contendo as coordenadas de cada vértice. Por exemplo, a área do triângulo com vértices $(0,0)$, $(1,0)$ e $(0,1)$ deve ser calculada como segue:
# 
# ```python
# A = area([[0,0], [1,0], [0,1]])
# ```
# 
# ou como 
# 
# ```python
# v1 = (0,0);  v2 = (1,0);  v3 = (0,1)
# vertices = [v1, v2, v3]
# A = area(vertices)
# ```

# **Exercício 5.** Considere a seguinte função: 
# 
# ```python
# def f(x):
#     if 0 <= x <= 2:
#         return x**2
#     elif 2 < x <= 4:
#         return 4
#     elif x < 0:
#         return 0
# ```
# 
# Explique por que `f(15)` não mostra nenhum valor? O que poderia ser feito para que `f(15)` seja igual a `-15`?

# **Exercício 6.** Considere a função (matemática) $f(x) = e^{rx} \, \textrm{sen}(mx) + e^{sx} \, \textrm{sen}(nx)$. Escreva uma função (computacional) para calcular o valor de $x$ para quaisquer valores reais $m$, $n$, $r$ e $s$. Por exemplo, sua função deve começar com a instrução:
# 
# ```python
# def f(x,m,n,r,s):
#     ...
# ```

# **Exercício 7.** Defina $h(x) = \frac{1}{\sqrt{2\pi}}e^{-\frac{1}{2}x^2}$. Escreva duas listas, `x` e `h`, contendo os valores de $x$ e $h(x)$ para 51 valores uniformemente espaçados no domínio $[-4,4]$.

# **Exercício 8.** Escreva um código para plotar o gráfico de $h(x)$. Em seguida, plote o gráfico de h(x). (Na resposta ao questionário, insira apenas o código.)

# **Exercício 9.** Considere a função $f(t) = t^3 + te^t + 1$ e o vetor $v = (3,2,-1)$. Aplique $f$ a cada elemento de $v$ e determine o resultado como uma tupla de 3 elementos.

# **Exercício 10.** Escreva um código para plotar o gráfico da função $y(t) = v_0t - \frac{1}{2}gt^2$, que descreve a trajetória de uma bola. Use $v_0 = 10$, $g = 9.81$ e $t \in [0,2v_0/g]$. Configure a legenda do eixo $x$ para `tempo (s)` e a do eixo $y$ para `altura (m)`. 
