#!/usr/bin/env python
# coding: utf-8

# # Fundamentos de *Python* para Computação Científica

# ### Aritmética
# 
# Os símbolos são os seguintes:
# 
# |operação|símbolo|
# |---|---|
# |adição|+|
# |subtração|-|
# |multiplicação|*|
# |divisão|/|
# |potenciação|**|

# **Exemplo:** calcule o valor de 
# $$4/3 - 2 \times 3^4$$

# In[13]:


4/3 - 2*3**4


# ### Expressões numéricas
# 
# - Comutatividade, associatividade, distributividade, agrupamentos
# 
# - Parênteses, colchetes e chaves (apenas parênteses)

# **Exemplo:** calcule o valor de 
# 
# $$2 - 98\{ 7/3 \, [ 2 \times (3 + 5 \times 6) - ( 2^3 + 2^2 ) - (2^2 + 2^3) ] - (-1) \}$$

# In[14]:


2 - 98*(7/3*(2*(3+5*6)-(2**3+2**2)-(2**2+2**3))-(-1))


# - Legibilidade, espaços **não alteram** o resultado
# - Princípios do Zen do Python: *a legibilidade conta*

# In[16]:


2 - 98*( 7/3*( 2*( 3 + 5*6 ) - ( 2**3 + 2**2 ) - ( 2**2 + 2**3 ) ) - (-1) ) 


# Parênteses não pareados (abrir, mas não fechar) produzirão um erro. 

# In[14]:


2 - 98*( 7/3  


# In[17]:


2 - 98*(7/3)


# ### Números inteiros e fracionários 
# 
# - Inteiros e fracionários distinguíveis pelo ponto decimal

# **Exemplo:** Calcule o valor de 
# $$2 + 3$$

# In[19]:


2 + 3 


# **Exemplo:** Calcule o valor de 
# $$2,0 + 3$$

# In[17]:


2.0 + 3


# > O valor é o mesmo, mas em Python, os dois números acima possuem naturezas diferentes. Essa "natureza" é chamada _tipo_. Falaremos disso mais tarde. Por enquanto, veja o seguinte: 

# In[8]:


type(5)


# In[18]:


type(5.0)


# > As duas palavras acima indicam que o **tipo** do valor 5 é `int` e o do valor 5.0 é `float`.

# **Exemplo:** Calcule o valor de
# $$5.0 - 5$$

# In[35]:


5.0 - 5


# > A diferença entre um número em ponto flutuante e um número inteiro resulta em um número em ponto flutuante! 
# 
# - Python 3.x *versus* Python 2

# #### Usar ponto ou usar vírgula?
# 
# > Em nosso sistema numérico, a vírgula (`,`) é quem separa a parte inteira da parte fracionária de um número decimal. Em Python, este papel é desempenhado pelo ponto (`.`). 
# 
# - Usaremos o **ponto e não a vírgula** para representar, em metalinguagem, números fracionários

# **Exemplo:** calcule o valor de $$5.1 - 5$$

# In[37]:


5.1 - 5


# - Observe o cálculo anterior... O resultado deveria ser 0.1, não? O que aconteceu?! 
# 
# - *Precisão de máquina* (discussão em outra disciplina)
# 
# - Resultados aproximados, matemática computacional

# ### Divisão inteira
#  
# Quando quisermos quociente inteiro, utilizamos o símbolo `//` (divisão inteira)

# **Exemplo:** calcule o valor de $$5/2$$

# In[42]:


5/2


# **Exemplo:** calcule o valor da **divisão inteira** $$5/2$$

# In[45]:


5//2


# #### O algoritmo da divisão e restos 
# 
# $$D = d \times q + r$$
# 
# - Podemos calcular $r$ de divisão inexata por meio do símbolo `%`, chamado de **operador módulo**.

# **Exemplo:** determine o resto da divisão $$7/2$$

# In[46]:


7 % 2 


# De fato, $7 = 2\times3 + 1$

# Verificando números inteiros pares e ímpares com o operador `%`.

# In[28]:


5 % 2  


# In[48]:


6 % 2


# ### Porcentagem
# 
# - `%` serve para calcular o resto de uma divisão
# 
# - Não há um símbolo especial para o cálculo da porcentagem
# 
# - Dividir o número em questão por 100 da maneira usual

# **Exemplo:** Quanto é 45\% de R\$ 43,28?

# In[30]:


45/100*43.28


# Veja que poderíamos também realizar esta conta da seguinte forma:

# In[33]:


0.45*43.28 


# Ou da forma:

# In[32]:


45*43.28/100


# > Esta última não seria tão literal quanto à conta original, porém, os três exemplos mostram que a multiplicação e a divisão são equivalentes em **precedência**. 
# 
# > Tanto faz neste caso realizar primeiro a multiplicação e depois a divisão, ou vice-versa. A única ressalva é o segundo exemplo, no qual, na verdade, não foi o computador quem dividiu 45 por 100. 

# #### Precedência de operações
# 
# - Assim como na Matemática, Python possui precedências em operações. 
# 
# - Quando não há parênteses envolvidos, multiplicação e divisão são realizadas antes de adições e subtrações.

# **Exemplo:** calcule $4 \times 5 + 3$

# In[34]:


4*5 + 3


# **Exemplo:** calcule $4 / 5 + 3$

# In[36]:


4/5 + 3


# Quando houver parênteses, eles têm precedência. 
# 
# **Exemplo:** calcule $4 \times (5 + 3)$

# In[22]:


4*(5+3)


# Em regra, operações são executadas da esquerda para a direita e do par de parênteses mais interno para o mais externo.
# 
# **Exemplo:** calcule $2 - 10 - 3$

# In[37]:


# primeiramente, 2 - 10 = - 8 é calculado; 
# depois - 8 - 3 = -11
2 - 10 - 3 =


# **Exemplo:** calcule $2 - (10 - 3)$

# In[38]:


# primeiramente, (10 - 3) = 7 é calculado; 
# depois  2 - 7 = -5
2 - (10 - 3)


# ### Comentários
# 
# - Inserimos *comentários* para documentar código. 

# #### Comentários em linha
# 
# São utilizados para ignorar tudo o que vier após o símbolo `#` naquela linha.

# In[55]:


# isto aqui é ignorado


# In[44]:


2 + 3 # esta linha será calculada  


# A instrução abaixo resulta em erro, pois `2 +` não é uma operação completa.

# In[45]:


2 + # 3


# A instrução abaixo resulta em 2, pois `+ 3` está comentado.

# In[46]:


2 # + 3 


# **Exemplo:** qual é o valor de 
# $$(3 - 4)^2 + (7/2 - 2 - (3 + 1))?$$

# In[47]:


""" ORDEM DE OPERAÇÕES 
primeiramente, (3 + 1) = 4 é calculado :: parêntese mais interno
em seguida, 7/2 = 3.5 :: divisão mais interna
em seguida, 3.5 - 2  = 1.5 :: primeira subtração mais interna
em seguida, 1.5 - 4  = -2.5 :: segunda subtração e resolve parêntese externo
em seguida, (3 - 4) = -1 :: parêntese
em seguida, (-1)**2 = 1 :: potenciação, ou duas multiplicações
em seguida, 1 + (-2.5) = -1.5 :: última soma
""" 

# Expressão 
(3 - 4)**2 + (7/2 - 2 - (3 + 1)) 


# #### Docstrings 
# 
# > Em Python, não há comentários em bloco, mas podemos usar _docstrings_ quando queremos comentar uma ou múltiplas linhas. Basta inserir um par de três aspas simples (`'''`) ou duplas (`"""`). Aspas simples são também chamadas de "plicas" (`'...'`). 

# #### Exemplo 
# 
# ```python
# '''
# Isto aqui é 
# um comentário em bloco e
# será ignorado pelo 
# interpretador se vier 
# seguido de outra instruções.
# '''
# ```
# > **Cuidado!** plicas não são apóstrofes!

# #### cont.
# 
# ```python
# """
# Isto aqui é 
# um comentário em bloco e
# será ignorado pelo 
# interpretador se vier 
# seguido de outra instruções.
# """
# ```

# In[48]:


"""
Isto aqui é 
um comentário em bloco e
será ignorado pelo 
interpretador se vier 
seguido de outras instruções.
"""


# ### Omitindo impressão 
# 
# Podemos usar um `;` para omitir a impressão do último comando executado na célula. 

# In[63]:


2 + 3; # a saída não é impressa na tela 


# In[54]:


2 - 3 
1 - 2; # nada é impresso pois o último comando vem seguido por ;


# In[66]:


"""
Docstring múlipla
não impressa
""";


# In[68]:


'''Docstring simples omitida''';


# ## Variáveis, atribuição e reatribuição
# 
# - Em Matemática, letras substituem valores
# 
# - Em Python, uma variável é um nome associado a um "endereço" na memória do computador

# **Exemplo:** se $x = 2$ e $y = 3$, calcule $x + y$

# In[69]:


x = 2
y = 3
x + y


# - `x` e `y` são variáveis
# 
# - O símbolo `=` indica *atribuição*
# 
# - Reatribuição ocorre quando fazemos uma nova atribuição na mesma variável (*overwriting*) 

# In[81]:


x = 2 # x tem valor 2 
y = 3 # y tem valor 3
x = y # x tem valor 3
x 


# **Exemplo:** A área de um retângulo de base $b$ e altura $h$ é dada por $A = bh$. Calcule valores de $A$ para diferentes valores de $b$ e $h$.

# In[75]:


b = 2 # base
h = 4 # altura
A = b*h
A 


# In[74]:


b = 10 # reatribuição em b
A = b*h # reatribuição em A, mas não em h 
A


# In[76]:


h = 5 # reatribuição em h
b*h # cálculo sem atribuição em A


# In[77]:


A # A não foi alterado


# > Variáveis são *case sensitive*, isto é, sensíveis a maiúsculas/minúsculas. 

# In[79]:


a = 2
A = 3 
a - A


# In[80]:


A - a


# ### Atribuição por desempacotamento
# 
# Podemos realizar atribuições em uma única linha.

# In[80]:


b,h = 2,4


# In[81]:


b


# In[82]:


h


# ### Imprimindo com `print`
# 
# - `print` é uma **função**. 
# 
# - Aprenderemos sobre funções mais à frente
# 
# - Por enquanto, basta entender que ela funciona da seguinte forma

# In[83]:


print(A) # imprime o valor de A


# In[84]:


print(b*h) # imprime o valor do produto b*h


# Com `print`, podemos ter mais de uma saída na célula.

# In[90]:


b, h = 2.1, 3.4
print(b) 
print(h)


# Podemos inserir mais de uma variável em `print` separando-as por vírgula.

# In[91]:


print(b, h)


# In[92]:


x = 0
y = 1 
z = 2 
print(x, y, z)


# In[99]:


print(x, x + 1, x + 2)


# ## Caracteres, letras, palavras: strings
# 
# Em Python, escrevemos caracteres entre plicas ou aspas. 

# In[93]:


'Olá!'


# In[53]:


"Olá!"


# In[94]:


'Olá, meu nome é Python.'


# Podemos atribuir caracteres a variáveis.

# In[111]:


a = 'a'
A = 'A'
print(a)
print(A)


# In[98]:


area1 = 'Matemática'
area2 = 'Estatística' 
print(area1, 'e', area2)


# Nomes de variáveis não podem iniciar por números ou conter caracteres especiais ($, #, ?, !, etc)

# In[96]:


1a = 'a' # inválido


# In[121]:


a1 = 'a1' # válido
a2 = 'a2' # válido


# Podemos usar `print` concatenando variáveis e valores.

# In[99]:


b = 20  
h = 10
print('Aprendo', area1, 'e', area2) 
print('A área do retângulo é', b*h)


# Em Python, tudo é um "objeto". Nos comandos abaixo, temos objetos de três "tipos" diferentes.

# In[101]:


a = 1
x = 2.0 
b = 'b'


# Poderíamos também fazer:

# In[130]:


a, x, b = 1, 2.0, 'b' # modo menos legível!


# Ao investigar essas variáveis (objetos) com `type`, veja o que temos:

# In[128]:


type(a) # verifica o "tipo" do objeto


# In[129]:


type(x)


# In[64]:


type(b)


# `str` (abreviação de *string*) é um objeto definido por uma cadeia de 0 ou mais caracteres.

# In[133]:


nenhum = ''
nenhum


# In[137]:


espaco = ' '
espaco


# **Exemplo:** Calcule o valor da área de um círculo de raio $R = 3$ e imprima o seu valor usando print e strings. Assuma o valor de $\pi = 3.145$.

# In[140]:


R = 3.0
pi = 3.145
A = pi*R**2
print('A área do círculo é: ', A)


# ## Tipos de dados: `int`, `float` e `str`

# - Em Python, cada objeto possui uma "família" ("tipo de dado") 
# 
# - Verificamos o tipo do objeto `x` com `type(x)`
# 
# - `int` equivale a dizer que $x \in \mathbb{Z}$
# 
# - `float` é "quase o mesmo" que dizer $y \in \mathbb{R}$
# 
# - No caso de `str`, é mais difícil denotar, mas podemos criar exemplos

# **Exemplo:** Considere o conjunto $A = \{s \in \mathbb{S} \, : s \text{ possui apenas duas vogais}\}$, onde $\mathbb{S}$ é o conjunto de palavras formadas por 2 letras.

# Todo elemento $s$ desse conjunto pode assumir um dos seguintes valores:
# 
# `aa`, `ae`, `ai`, `ao`, `au`, 
# 
# `ea`, `ee`, `ei`, `eo`, `eu`, 
# 
# `ia`, `ie`, `ii`, `io`, `iu`,
# 
# `oa`, `oe`, `oi`, `oo`, `ou`,
# 
# `ua`, `ue`, `ui`, `uo`, `uu`.

# Apesar de apenas algumas terem significado na nossa língua, existem 25 *anagramas*.
# 
# Então, poderíamos escrever:

# In[141]:


s1, s2, s3, s4, s5  = 'aa', 'ae', 'ai', 'ao', 'au'
s6, s7, s8, s9, s10  = 'ea', 'ee', 'ei', 'eo', 'eu'
s11, s12, s13, s14, s15  = 'ia', 'ie', 'ii', 'io', 'iu'
s16, s17, s18, s19, s20  = 'oa', 'oe', 'oi', 'oo', 'ou'
s21, s22, s23, s24, s25  = 'oa', 'oe', 'oi', 'oo', 'ou' 


# Os 25 anagramas acima foram armazenados em 25 variáveis diferentes.

# In[69]:


print(s3)
print(s11)
print(s24)


# ### _Casting_

# Uma das coisas legais que podemos fazer em Python é alterar o tipo de um dado para outro. Essa operação é chamada de _type casting_, ou simplesmente _casting_. 
# 
# Para fazer _casting_ de `int`, `float` e `str`, usamos funções de mesmo nome.

# In[142]:


float(25) # 25 é um inteiro, mas float(25) é fracionário 


# In[145]:


int(34.21) # 34.21 é fracionário, mas int(34.21) é um "arredondamento" para um inteiro 


# In[72]:


int(5.65) # o arredondamento é sempre para o inteiro mais próximo "para baixo"


# In[146]:


int(-6.6)


# O _casting_ de um objeto 'str' composto de letras com 'int' é inválido.

# In[147]:


int('a')


# O _casting_ de um 'int' ou 'float' com 'str' formada como número é válido.

# In[148]:


str(2)  


# In[149]:


str(3.14)


# O _casting_ de um 'str' puro com 'float' é inválido.

# In[150]:


float('a')


# ### Concatenação

# A concatenação de objetos `str` pode ser feita de modo direto como uma "soma" (usando `+`) ou acompanhada por *casting*.

# In[154]:


s21 + s23


# In[155]:


s1 + s3 + s5


# In[156]:


'Casting do número ' + str(2) + '.'


# In[157]:


str(1) + ' é inteiro' + ',' + ' ' + 'mas ' + str(3.1415) + ' é fracionário!'


# Podemos criar concatenações de `str` por repetição usando multiplicação (`*`) e usar parênteses para formar as mais diversas "montagens". 

# In[173]:


(str(s3) + ',')*2 + s3 + '...'


# In[174]:


x = 1.0
'Usando 0.1, incrementamos ' + str(x) + ' para obter ' + str(x + 0.1) + '.' 


# In[175]:


print(5*s20 + 10*s2 + 5*s17 + 5*('.') + 'YEAH! :)')


# ## Módulos e importação

# - Módulos são como gavetas em um escritório ou equipamentos em uma oficina
# 
# - Vários módulos podem ser organizados juntos para formar um *pacote*
# 
# - Em Python, quando precisamos de algo específico, realizamos a importação de um módulo inteiro, de um submódulo deste módulo ou de apenas um objeto do módulo. 
# 
# - Há muitas maneiras de fazer isso. 

# Para importar um módulo inteiro, podemos usar a sintaxe:
# 
# ```python 
# import nomeDoModulo
# ```

# Para importar um submódulo, podemos usar a sintaxe:
# 
# ```python 
# import nomeDoModulo.nomeDoSubmodulo
# ```
# ou a sintaxe
# 
# ```python 
# from nomeDoModulo import nomeDoSubmodulo
# ```

# Caso queiramos usar uma função específica, podemos usar 
# 
# ```python 
# from nomeDoModulo import nomeDaFuncao
# ```
# ou 
# 
# ```python 
# from nomeDoModulo.nomeDoSubmodulo import nomeDaFuncao
# ```
# se a função pertencer a um submódulo.

# Usando _alias_ (pseudônimo)
# 
# ```python
# import nomeDoModulo as nomeQueEuQuero
# ```

# Como último exemplo de importação, considere a sintaxe:
# 
# ```python 
# from nomeDoModulo import nomeDoSubmodulo as nds
# ```
# 
# Neste exemplo, estamos criando um pseudônimo para um submódulo.

# ### O módulo `math`

# - O módulo `math` é uma biblioteca de funções matemáticas.
# 
# - Em Matemática, uma função é como uma máquina que recebe uma matéria-prima e entrega um produto. 

# Importaremos o módulo `math` como:

# In[2]:


import math as mt


# O número neperiano (ou número de Euler) $e$ é obtido como:

# In[6]:


mt.e


# O valor de $\pi$ pode ser obtido como: 

# In[8]:


mt.pi


# >$e$ e $\pi$ são números irracionais. No computador, eles possuem um número finito de casas decimais!

# **Exemplo:** calcule a área de um círculo de raio $r = 3$.

# In[184]:


r = 3 # raio 
area = mt.pi*r**2 # area 
print('A área é',area) # imprime com concatenação


# A raiz quadrada de um número $x$, $\sqrt{x}$, é calculada pela função `sqrt` (abreviação de "square root")

# In[11]:


x = 3 # note que x é um 'int'
mt.sqrt(x) # o resultado é um 'float'  


# In[15]:


mt.sqrt(16) # 16 é 'int', mas o resultado é 'float'


# **Exemplo:** calcule o valor de $\sqrt{ \sqrt{\pi} + e + \left( \frac{3}{2} \right)^y }$, para $y = 2.1$.

# In[23]:


mt.sqrt( mt.sqrt( mt.pi ) + mt.e + 3/2**2.1 ) # espaços dão legibilidade  


# O logaritmo de um número $b$ na base $a$ é dado por $\log_a \, b$, com $a > 0$, $b > 0$ e $a \neq 1$. 
# 
# - Quando $a = e$ (base neperiana), temos o _logaritmo natural_ de $b$, denotado por $\text{ln} \, b$.
# 
# - Quando $a = 10$ (base 10), temos o _logaritmo em base 10_ de $b$, denotado por $\text{log}_{10} \, b$, ou simplesmente $\text{log} \, b$.

# **Nota!**
# 
# - Para calcular $\text{ln} \, b$, use `log(b)`.
# 
# - Para calcular $\text{log} \, b$, use `log10(b)`.
# 
# - Para calcular $\text{log}_2 \, b$, use `log2(b)`.
# 
# - Para calcular $\text{log}_a \, b$, use `log(b,a)`.
# 
# Pelas duas últimas colocações, vemos que `log(b,2)` é o mesmo que `log2(b)`.

# Vejamos alguns exemplos:

# In[188]:


mt.log(2) # isto é ln(2) 


# In[24]:


mt.log10(2) # isto é log(2) na base 10    


# In[192]:


mt.log(2,10) # isto é o mesmo que a anterior


# In[193]:


mt.log2(2) # isto é log(2) na base 2


# **Exemplo:** se $f(x) = \dfrac{ \text{ln}(x+4) + \log_3 x }{ \log_{10} x }$, calcule o valor de $f(e) + f(\pi)$.

# In[26]:


x = mt.e # x = e  

fe = ( mt.log(x + 4) + mt.log(x,3) ) / ( mt.log10(x) ) # f(e)

x = mt.pi # reatribuição do valor de x

fpi = ( mt.log(x + 4) + mt.log(x,3) ) / ( mt.log10(x) ) # f(pi)

print('O valor é', fe + fpi)   


# No exemplo anterior, espaços foram acrescentados para tornar os comandos mais legíveis.

# ## Introspecção 
# 
# Podemos entender mais sobre módulos, funções e suas capacidades examinando seus componentes e pedindo ajuda sobre eles. 
# 
# Para listar todos os objetos de um módulo, use `dir(nomeDoModulo)`. 
# 
# Para pedir ajuda sobre um objeto, use a função `help` ou um ponto de interrogação após o nome `?`.

# In[197]:


dir(mt) # lista todas as funções do módulo math


# In[199]:


help(mt.pow) # ajuda sobre a função 'pow' do módulo 'math' 

get_ipython().run_line_magic('pinfo', 'mt.pow')


# Como vemos, a função `pow` do módulo `math` serve para realizar uma potenciação do tipo $x^y$. 

# In[27]:


mt.pow(2,3) # 2 elevado a 3


# **Exemplo:** considere o triângulo retângulo com catetos de comprimento $a = \frac{3}{4}\pi \, m$ e $b = \frac{2}{e} \, m$. Qual é o comprimento da hipotenusa $c$?

# In[28]:


'''
Resolução pelo Teorema de Pitágoras
c = sqrt( a**2 + b**2 )
'''
a = 3./4. * mt.pi # 3. e 4. é o mesmo que 3.0 e 4.0
b = 2./mt.e
c = mt.sqrt( a**2 + b**2 )
print('O valor da hipotenusa é:', c, 'm')


# O mesmo cálculo acima poderia ser resolvido com apenas uma linha usando a função `hypot` do módulo `math`.

# In[29]:


c = mt.hypot(a,b) # hypot calcula a hipotenusa
print('O valor da hipotenusa é:', c, 'm')


# **Exemplo:** Converta o ângulo de $270^{\circ}$ para radianos.

# 1 radiano ($rad$) é igual a um arco de medida $r$ de uma circunferência cujo raio mede $r$. Isto é, $r = 1 \,rad$. Uma vez que $180^{\circ}$ corresponde a meia-circunferência, $\pi r$, então, $\pi \, rad = 180^{\circ}$. Por regra de três, podemos concluir que $x^{\circ}$ equivale a $\frac{x}{180^{\circ}} \pi \, rad$.

# In[38]:


ang_graus = 270 # valor em graus
ang_rad = ang_graus/180*mt.pi # valor em radianos
print(ang_rad) 


# Note que em 
# 
# ```python
# ang_graus/180*mt.pi
# ```
# 
# a divisão é executada antes da multiplicação porque vem primeiro à esquerda. O parênteses não é necessário neste caso. 

# Poderíamos chegar ao mesmo resultado diretamente com a função `radians` do módulo `math`.

# In[32]:


get_ipython().run_line_magic('pinfo', 'mt.radians')


# In[40]:


mt.radians(ang_graus)    


# ### Arredondamento de números fracionários para inteiros

# Com `math`, podemos arredondar números fracionários para inteiros usando a regra "para cima" (teto) ou "para baixo" (chão). 
# 
# - Use `ceil` (abreviatura de _ceiling_, ou "teto") para arredondar para cima;
# - Use `floor` ("chão") para arredondar para baixo;

# In[41]:


mt.ceil(3.42)


# In[42]:


mt.floor(3.42)


# In[43]:


mt.ceil(3.5)


# In[45]:


mt.floor(3.5)


# ## Números complexos

# - Números complexos são importantes em fenômenos físicos envolvendo sons, frequencias e vibrações 
# 
# - O conjunto dos números complexos é definido como
# 
# $\mathbb{C} = \{ z = a + bi \, : \, a, b \in \mathbb{R} \text{ e } i = \sqrt{-1} \}$. O valor $i$ é o _número imaginário_.

# - Em Python, números complexos são objetos do tipo `complex` e escritos na forma
# 
# ```python
# z = a + bj
# ```
# ou 
# 
# ```python
# z = a + bJ
# ```
# - O símbolo `j` (ou `J`) quando vem acompanhado de um `int` ou `float` define a parte imaginária

# In[54]:


3 - 2j


# In[55]:


type(3 - 2j) # o número é um complex


# In[58]:


4J # J (maiúsculo)


# In[59]:


type(4j) 


# > Se `j` ou `J` são colocados isoladamente, significarão uma variável. Caso a variável não esteja definida, um erro de indefinição resultará.

# In[61]:


j


# ### Parte real, parte imaginária e conjugados

# Números complexos também podem ser diretamente definidos como `complex(a,b)` onde `a` é a parte real e `b` é a parte imaginária.  

# In[69]:


complex(6.3,9.8)


# As partes real e imaginária de um `complex` são extraídas usando as funções `real` e `imag`, nesta ordem. 

# In[70]:


z = 6.3 + 9.8j
z.real


# In[71]:


z.imag


# O conjugado de `z` pode ser encontrado com a função `conjugate()`.

# In[117]:


z.conjugate()


# ### Módulo de um número complexo
# 
# Se $Re(z)$ e $Im(z)$ forem, respectivamente, a parte real e a parte imaginária de um número complexo, o _módulo_ de $z$ é definido como
# 
# $$|z| =\sqrt{[Re(z)]^2 + [Im(z)]^2}$$

# **Exemplo:** se $z = 2 + 2i$, calcule o valor de $|z|$.

# Podemos computar esta quantidade de maneiras distintas. Uma delas é:

# In[72]:


(z.real ** 2 + z.imag ** 2) ** 0.5


# Entretanto, podemos usar a função `abs` do Python. Esta função é uma função predefinida pertencente ao _core_ da linguagem.

# In[74]:


abs(z)


# A função `abs` também serve para retornar o "valor absoluto" (ou módulo) de números reais. Lembremos que o módulo de um número real $x$ é definido como
# 
# $$
# |x| =
# \begin{cases}
# x,& \text{se } x \geq 0 \\
# -x,& \text{se } x < 0 \\
# \end{cases}
# $$

# In[75]:


help(abs)  


# In[79]:


abs(-3.1)


# In[81]:


abs(-mt.e)  

