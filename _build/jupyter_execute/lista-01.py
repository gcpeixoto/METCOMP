#!/usr/bin/env python
# coding: utf-8

# # Lista de exercícios 1
# 
# **Resolva todos os problemas por computação e registre as suas respostas no questionário disponibilizado no ambiente virtual de aprendizagem.**
# <hr>

# **Exercício 1.** Calcule o valor de `1+1.0009`, atribua o resultado a uma variável e imprima o valor dessa variável. Quantos noves são impressos?

# **Exercício 2.** A expectativa de vida no Brasil em 2020 era de 76,6 anos. Paulo, um cidadão paraibano, já viveu 2,4 bilhões de segundos. Tomando como referência o valor de 2020, responda: Paulo atingiu a expectativa de vida? Quantos anos ele já viveu? **Nota:** a resposta deve ser um valor inteiro.

# **Exercício 3.** O _Birchfield Harriers_ é um clube de atletismo inglês fundado em 1877. Você recebeu um convite para trabalhar no setor de engenharia do clube provendo cálculos para materiais de revestimento de raias de corrida. Seu gerente lhe deu o seguinte desafio: construir um programa em Python para converter unidades de comprimento para o sistema britânico. O seu programa deve funcionar da seguinte forma: dado um valor de entrada `x` em metros, calcular o valor correspondente em _pés_, _polegadas_, _jardas_ e _milhas_. Supondo uma raia com `x = 1000` m de extensão, obtenha os valores correspondentes para `x`, nas 4 unidades acima, com 2 casas decimais. 
# 
# Tabela de conversão:
# 
# - 1 polegada = 2.54 centímetros
# - 1 pé = 12 polegadas
# - 1 jarda = 3 pés
# - 1 milha britânica = 1760 jardas
# 
# **Nota:** os valores calculados devem ser expressos na ordem acima mencionada para as unidades. Use a função `round(x,d)`, onde `d` é o número de casas decimais.

# **Exercício 4.** A massa específica de uma substância é definida por $\rho = m/V$, onde $m$ é a massa de um volume $V$. Calcule a massa, em quilogramas, para 10 m<sup>3</sup> de cada uma das substâncias listadas abaixo. 
# 
# |material|massa específica (g/cm<sup>3</sup>)|
# |---|---|
# |água do mar|1.025|
# |ar|0.0012|
# |gasolina|0.67|
# |gelo|0.9|
# |mercúrio|13.6|
# |ouro|18.9|
# |platina|21.4|
# |prata|10.5|
# 
# Então, considere os seguintes grupos:
# 
# - Grupo 1: água do mar, ar, gasolina, gelo
# - Grupo 2: mercúrio, ouro, platina, prata
# 
# Se $M_1$ e $M_2$ são as maiores massas que você calculou entre as substâncias dos grupos 1 e 2, nesta ordem, qual é o valor de $M_1$ + $M_2$, em toneladas?

# **Exercício 5.** Suponha que a taxa de juros de um banco brasileiro seja de $p$ por cento ao ano. Um depósito inicial de $A$ reais terá um montante de $A(1 + p)^n$ após $n$ anos. Considere que você tenha depositado 1000 euros em uma conta no exterior e espera retirar o dinheiro daqui a 5 anos com rendimentos a uma taxa de 2.5% ao ano. Quanto você obteria, em reais, após o período? **Nota:** use 1 euro = 6,52 reais.

# **Exercício 6.** O código a seguir contém dois erros. Identifique-os e proponha as correções devidas. 
# Que valor deve ser impresso após o símbolo de `=`?
# 
# ```python
# x = 1; print('sin({0})={1:.2f}'.format(x, sin(x))
# ```

# **Exercício 7.** Ao tentar calcular a identidade trigonométrica $\textrm{sen}^2(x) + \cos^2(x) = 1$, um engenheiro copiou o seguinte código de um colega:
# 
# ```python
# from math import sin, cos
# x = pi/4
# 1_val = math.sin^2(x) + math.cos^2(x)
# print(1_VAL)
# ```
# 
# Entretanto, verificou que a resposta não condizia com o esperado. Analise o que pode estar errado no código, proponha correções e avalie o resultado. Que valor é impresso com o código correto?

# **Exercício 8.** Escreva um programa para calcular as raízes de uma equação do 2o. grau qualquer na forma $P(x) = ax^2 + bx + c$. Use seu programa para computar as raízes de $P(x)$ para $a = \sqrt{3}$, $b = e^2$, $c = \textrm{ln}(2)/2$.
# 

# **Exercício 9.** A fórmula utilizada para determinar o volume de um tronco de pirâmide é dada por $V=\frac{h}{3}(A + \sqrt{Aa} + a)$, onde:
# 
# - $h$: altura do tronco
# - $A$: área da base maior
# - $a$: área da base menor
# 
# Suponha que as bases sejam formadas por octógonos regulares. Sabendo que a área de um octógono é dada por $2L^2(\sqrt{2} + 1)$, onde $L$ é a medida da aresta, calcule o volume de um tronco de pirâmide medindo 1,5 metros de altura, 3 metros de aresta inferior e 2 metros de aresta superior. Aproxime a resposta para um valor inteiro.

# **Exercício 10.** A força de arrasto devido à resistência do ar sobre um objeto pode ser expressa como $F_d = \frac{1}{2}C_d\rho AV^2$ (em newtons), onde $\rho$ é a massa específica do ar, $V$ é a velocidade do objeto, $A$ é a área da seção transversal (normal à direção da velocidade), e $C_d$ é o coeficiente de arrasto, o qual depende da forma do objeto e da rugosidade da superfície.A força gravitacional sobre um objeto de massa $m$ é dada por $F_g = mg$, onde $g = 9.81 \, m/s^2$. 
# 
# Podemos usar as fórmulas para $F_d$ e $F_g$ para estudar a importância da resistência do ar versus gravidade ao chutar uma bola de futebol. A massa específica do ar é $\rho = 1.2 \, kg/m^3$. Temos $A = \pi a^2$ para qualquer bola com raio $a$. Para uma bola de futebol, $a = 11 \, cm$, a massa é $m = 0.43 \, kg$ e $C_d = 0.2$.
# 
# Escreva um programa para calcular as forças de arrasto e gravitacional em newtons ($N$). Use o programa para calcular as força gravitacional e as forças de arrasto sobre a bola durante um chute pesado, $V = 120 \, km/h$ e, durante um chute leve, $V = 10 \, km/h$. Seu programa deverá imprimir 3 valores aproximados a 2 casas decimais, $F_g$, $F_d$ (chute pesado), $F_d$ (chute leve). **Nota:** utilize $V$ em $m/s$.
