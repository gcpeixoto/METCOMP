#!/usr/bin/env python
# coding: utf-8

# # Laboratório 3
# 
# **Resolva todos os problemas por computação.**
# <hr>

# **Problema 1**: A Evona Inc. é uma empresa que fabrica microcomponentes para _cockpits_ de aeronaves. Em seu novo catálogo, implementado após uma mudança da gestão operacional, cada microcomponente passou a ser guardado no estoque em pequenas caixas endereçadas por um número natural
# e unicamente identificado por um código formado por 4 caracteres que obedece à seguinte regra: 
# 
# $$v: \underline{c_1} \, \underline{c_2} \, \underline{c_3} \, \underline{c_4}$$
# 
# - O valor `v` é o índice do código na sequencia ordenada crescente;
# - O caracter $c_1$ deve assumir o valor `'A'`, `'B'` ou `'C'`;
# - O caracter $c_2$ deve ser um número ímpar;
# - Os caracteres $c_3$ e $c_4$ devem assumir valores entre 0 e 9, podendo ser repetidos.
# 
# Assim, o primeiro código possível é `'A100'` e o último é `'C999'`.
# 
# Você foi incumbido de organizar o catálogo e criar um mecanismo de busca onde um usuário qualquer pode localizar rapidamente o endereço da caixa a partir do código de 4 caracteres. Diante disso:
# 
# - Crie uma função chamada `lst_cod_4` para gerar todos os códigos possíveis;
# 
# - Crie uma segunda função chamada `loc_cod` para determinar o endereço do microcomponente a partir de seu código;
# 
# - Determine os endereços no estoque para os códigos `'A385'`, `'B743'` e `'C109'`.

# **Problema 2:** Borrachas sintéticas são obtidas por processos químicos de polimerização pela adição de compostos diênicos. A borracha vulcanizada, por exemplo, foi descoberta em 1839, por Charles Goodyear, cujo sobrenome deu origem à fabricante de pneus _Goodyear_. Outros tipos de borracha sintética, tais como a siliconada, fluorada e nitrílica, são utilizados para fabricar correias, revestimentos, mangueiras, vedantes. 
# 
# Alguns elementos comuns que constituem as fórmulas químicas das borrachas sintéticas são: carbono, hidrogênio, nitrogênio e oxigênio. Suponha que você está trabalhando em um projeto na indústria química onde lhe foi pedido para fazer um levantamento das seguintes informações a respeito dos elementos químicos consoante a tabela periódica: símbolo ($s$), número atômico ($Z$), massa atômica ($m$) e configuração eletrônica ($e$).
# 
# As tarefas atribuídas a você são as seguintes:
# 
# - organizar em uma lista `T` todas as ênuplas do tipo `(s,Z,m,e)` para cada um dos 4 elementos;
# - escrever uma expressão computacional que forme, por indexações e concatenações, a fórmula do metano, i.e. `'CH4'`, cujo tipo de dado deve ser `str`.
# 
# Notas:
# 
# - A lista `T` deve ser algo como `[(s1,Z1,m1,e1),...,(s4,Z4,m4,e4)]`.
# 
# - A expressão deve usar apenas indexações e um casting de `str` (p.ex. `T[2][2] + str(T[3][1]) ...`, bem como números acessados na própria tabela. Isto é, expressões do tipo `T[2][2] + 1` ou `T[1][2] - 6` não são permitidas porque 1 e 6 são inteiros isolados.

# **Problema 3:** _Alcanos_ são hidrocarbonetos parafínicos constituídos exclusivamente por carbono e hidrogênio cuja fórmula geral é dada por: 
# 
# $$C_nH_{2n+2}$$
# 
# Para $n = 1,2,\ldots,10$, os alcanos recebem nomes especiais da seguinte forma: `prefixo` + `-ano`. Os prefixos são:
# 
# |n|prefixo|
# |---|---|
# |1|met-|
# |2|et-|
# |3|prop-|
# |4|but-|
# |5|pent-|
# |6|hex-|
# |7|hept-|
# |8|oct-|
# |9|non-|
# |10|dec-|
# 
# - Use a fórmula e os prefixos dados para imprimir na tela uma tabela do tipo:
# 
# |n|fórmula|alcano|
# |-|----|------|
# |1|C1H4|metano|
# |...|...|...|

# **Problema 4**: Uma esteira rolante de bagagens especiais de um aeroporto brasileiro possui 3 slots de transporte sendo capaz de comportar no máximo 3 objetos (1 em cada slot) suportando uma carga máxima total de 5 kg. Suponha que os objetos sejam denominados $a$, $b$ e $c$. Exceto a configuração de nenhum objeto transportado,
# 
# 1. Determine todas as configurações possíveis transportáveis como ternas do tipo ($p_a$,$p_b$,$p_c$), onde $p_a$, $p_b$ e $p_c$ são os pesos individuais dos objetos. 
# 
# 2. Quantas combinações são possíveis de modo que $p_a + p_b + p_c = 5$?
# 
# Notas:
# 
# - Para resolver 1, observe que será necessário encontrar todas as soluções inteiras não-negativas como ternas ($p_a$,$p_b$,$p_c$) tais que $p_a + p_b + p_c \leq 5$.
# 
# - Para resolver 2, considere o seguinte resultado: 
# 
# > Se $x_1 + x_2 + \ldots + x_n = b$, então $N = \frac{(n + b -1)!}{b!(n-1)!}$ é o número de soluções não-negativas da equação linear.
