#!/usr/bin/env python
# coding: utf-8

# # Laboratório 2
# 
# **Resolva todos os problemas por computação.**
# <hr>

# **Problema 1**: Considere $f(x) = b + \sqrt{e^{\alpha} - (x - a)^2}$ e $g(x) = x^2\cos(x) - 4$. Calcule $y = f(g(x=0))$ para $a = 2$ e $b = -2$. Quais são os valores aceitáveis de $\alpha$ para que $y \in \mathbb{R}$?

# In[ ]:


import sympy as sym

a,b,x,alpha = sym.symbols('a b x alpha')

f = b + sym.sqrt(sym.exp(1)**(alpha) - (x - a)**2)
g = x**2*sym.cos(x) - 4

y = f.subs(x,g).subs(a,2).subs(b,-2).subs(x,0)

# discriminante
yr = sym.exp(1)**alpha - 36
sym.solveset(yr >= 0,alpha ,domain=sym.Reals)


# **Problema 2:** Considere os seguintes polinômios:
# 
# $$P(x) = a_0 + a_1x + a_5x^5 + a_{13}x^{13}$$
# 
# $$Q(x) = b_0 + b_4x^4 + b_8x^8 + b_{22}x^{22}$$
# 
# Compute a expressão algébrica de $R(x) = P(x)Q(x)$ em $x = \pi$.

# In[ ]:


import sympy as sym

a0,a1,a5,a13,b0,b4,b8,b22,x = sym.symbols('a_0 a_1 a_5 a_13 b_0 b_4 b_8 b_22 x')

P = a0 + a1*x + a5*x**5 + a13*x**13
Q = b0 + b4*x**4 + b8*x**8 + b22*x**22

R = P*Q.subs(x,sym.pi)


# **Problema 3:** Considere o polinômio $R(x)$ obtido no Problema 1. Se $a_0 = -2$, $a_1 = -4$, $a_5 = 6$, $a_{13} = 8/3$, $b_0 = -1$, $b_4 = -3/4$, $b_8 = 5$ e $b_{22} = 7$, determine o valor da soma dos coeficientes do termo $x^5$. Considere $\pi = 3.14$.

# In[ ]:


from math import pi
a0_n,a1_n,a5_n,a13_n = -2,-4,6,8/3
b0_n,b4_n,b8_n,b22_n = -1,-3/4,5,7

Rn = R.subs({a0:a0_n,a1:a1_n,a5:a5_n,a13:a13_n,         b0:b0_n,b4:b4_n,b8:b8_n,b22:b22_n})

Rn.expand()


# In[ ]:


(-4.5*sym.pi - 6 + 30*sym.pi*8 + 42*sym.pi*22).subs(sym.pi,3.14)


# **Problema 4:** Utilizando a mesma substituição de coeficientes apresentada no Problema 2, determine todas as raízes reais do polinômio $R(x)$ com aproximação de 3 casas decimais.

# In[ ]:


sym.solveset(Rn,x,sym.Reals)


# **Problema 5:** Uma fórmula usada para modelar o crescimento populacional é a função exponencial $P(t) = Ce^{rt}$, onde $C$ é a população inicial, $r$ a *taxa de crescimento* e $t$ o tempo decorrido. De acordo com o [[IBGE]](https://cidades.ibge.gov.br/brasil/pb), a população estimada no estado da Paraíba no último censo em 2010 era de 3.766.528 pessoas. Em 2019, este numéro saltou para 4.018.127 pessoas. Diante disso, crie um modelo simbólico para responder os itens a seguir: 
# 
# - considerando o interstício de 2010 a 2019, qual foi a taxa de crescimento $r$ do estado?
# 
# - supondo que a população cresça na mesma taxa encontrada no item anterior, qual será a população do estado em 2037? E em 2055?
