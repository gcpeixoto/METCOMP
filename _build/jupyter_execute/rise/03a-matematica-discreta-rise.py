#!/usr/bin/env python
# coding: utf-8

# # Fundamentos de Matemática Discreta com Python 

# ## Matemática Discreta
# 
# - Área da Matemática que lida com objetos discretos, a saber, conjuntos, sequencias, listas, coleções ou quaisquer entidades *contáveis*. 
# - Exemplo, $\mathbb{R}$ é incontável, ou não enumerável
# - Vários exemplos de contáveis:
#     - O conjunto das vogais da língua portuguesa;
#     - O conjunto dos times de futebol brasileiros da série A em 2020;
#     - O conjunto de nomes das estações do ano;
#     - O conjunto das personagens do quarteto do filme *Os Pinguins de Madagascar* e;
#     - O conjunto dos números pares positivos menores ou iguais a dez.

# - Conjuntos denotados por *extensão*: quando listamos seus elementos
# 
# - $\{ a, e, i, o, u \}$
# - $\{ \text{Atlético-PR}, \ldots, \text{Bahia}, \text{Botafogo}, \ldots, \text{Coritiba}, \ldots, \text{Fortaleza}, \ldots, \text{Internacional}, \ldots, \text{São Paulo}, \text{Sport}, \text{Vasco} \}$
# - $\{ \text{Primavera}, \text{Verão}, \text{Outono}, \text{Inverno}\}$
# - $\{ \text{Capitão}, \text{Kowalski}, \text{Recruta}, \text{Rico}\}$
# - $\{ 2, 4, 6, 8,10\}$

# - Denotados por *compreensão*: quando usamos uma propriedade que distingue seus elementos. 
# 
# - $\{ c \in \mathbb{A} \, ; \, c \text{ é vogal} \}$
# - $\{ t \in \mathbb{T} \, ; \, t \text{ é da Série A} \}$
# - $\{ x  \, ; \, x \text{ é uma estação do ano} \}$
# - $\{ p  \, ; \, p \text{ é personagem do quarteto principal do filme Os Pinguins de Madagascar} \}$
# - $\{ e  \, ; \, e \text{ é estação do ano} \}$
# - $\{ n \in \mathbb{Z} \, | \, n = 2k \wedge 2 \leq n \leq 10 \wedge k \in \mathbb{Z} \}$

# Por livre conveniência: 
# 
# - $\mathbb{A}$ é o conjunto de todas as letras de nosso alfabeto
# - $\mathbb{T}$ é o conjunto de todos os times de futebol do Brasil.

# ## Estruturas de dados para objetos discretos
# 
# As principais que aprenderemos: 
# 
# - `list`: estrutura cujo conteúdo é modificável e o tamanho variável. Listas são caracterizadas por *mutabilidade* e *variabilidade*. Objetos `list` são definidos por um par de colchetes e vírgulas que separam seus elementos: `[., ., ... ,.]`.
# 
# - `tuple`: estrutura cujo conteúdo não é modificável e o tamanho fixado. Tuplas são caracterizadas por *imutabilidade* e *invariabilidade*. Objetos `tuple` são definidos por um par de colchetes e vírgulas que separam seus elementos: `(., ., ... ,.)`.

# - `dict`: estruturas contendo uma coleção de pares do tipo *chave-valor*. Dicionários são caracterizados por *arrays associativos* (*tabelas hash*). Objetos `dict` são definidos por um par de chaves e agrupamentos do tipo  `'chave':valor` (*key:value*), separados por vírgula: `{'chave1':valor1, 'chave2':valor2, ... ,'chaven':valorn}`. As chaves (*keys*) podem ser do tipo `int`, `float`, `str`, ou `tuple` ao passo que os valores podem ser de tipos arbitrários.
# 
# - `set`: estruturas similares a `dict`, porém não possuem chaves e contêm objetos únicos. Conjuntos são caracterizadas por *unicidade* de elementos. Objetos `set` são definidos por um par de chaves e vírgulas que separam seus elementos: `{., ., ... ,.}`.

# ## Listas
# 
# Estruturas `list` formam uma coleção de objetos arbitrários e podem ser criadas de modo sequenciado com operadores de pertencimento ou por expressões geradoras, visto que são estruturas iteráveis.

# In[120]:


vogais = ['a','e','i','o','u'] # elementos são 'str'
vogais


# In[121]:


times = ['Bahia', 'Sport', 'Fortaleza', 'Flamengo']
times 


# In[122]:


pares10 = [2,4,6,8,10]
pares10


# In[123]:


mix = ['Bahia',24,6.54,[1,2]] # vários objetos na lista
mix 


# ### Listas por geração
# 
# **Exemplo**: crie uma lista dos primeiros 100 inteiros não-negativos.

# In[124]:


os_100 = range(100) # range é uma função geradora
print(list(os_100)) # casting com 'list'


# **Exemplo**: crie o conjunto $\{ x \in \mathbb{Z} \, ; \, -20 \leq x < 10 \}$

# In[125]:


#print(list(range(-20,10))) # print é usado para imprimir column-wise 

print(list(range(-20,10)))


# **Exemplo**: crie o conjunto $\{ x \in \mathbb{Z} \, ; \, -20 \leq x \leq 10 \}$

# In[126]:


print(list(range(-20,11))) # para incluir 10, 11 deve ser o limite. Por quê?


# ## Adicionando e removendo elementos
# 
# Há vários métodos aplicáveis para adicionar e remover elementos em listas.

# ### Adição por apensamento
# 
# Adiciona elementos por concatenação no final da lista.

# In[127]:


times.append('Botafogo')
times 


# In[128]:


times.append('Fluminense')
times


# ### Adição por extensão 
# 
# Para incluir elementos através de um objeto iterável, sequenciável, usamos `extend`.

# In[129]:


falta = ['Vasco', 'Atlético-MG']
times.extend(falta) # usa outra lista pra estender a lista
times 


# #### Iteração e indexação
# 
# - *Iterar* sobre uma lista é "passear" por seus elementos
# 
# - Em Python, a indexação de listas vai de `0` a `n - 1`, onde `n` é o tamanho da lista. 
# 
# Por exemplo:
# 
# $\text{posição} : \{p=0, p=1, \ldots, p={n-1}\}$
# 
# $\text{elementos na lista} : [x_1, x_2, \ldots, x_{n}]$
# 
# - Mesma idéia aplicável a qualquer coleção, sequencia ou objeto iterável.

# ### Remoção por índice
# 
# Suponha que tivéssemos criado a lista:

# In[130]:


pares = [0,2,5,6] # 5 não é par
pares


# Como 5 não é par, não deveria estar na lista. Para excluírmos um elemento em uma posição específica, usamos `pop` passando o *índice* onde o elemento está. 

# In[131]:


pares.pop(2) # o ímpar 5 está na posição 2 e NÃO 3! 
pares     


# ### Adição por índice
# 
# Nesta lista, podemos pensar em incluir 4 entre 2 e 6. Para isto, usamos `insert(posicao,valor)`, para `valor` na `posicao` desejada.

# In[132]:


pares.insert(2,4) # 4 é inserido na posição de 6, que é deslocado
pares
  


# ### Apagar conteúdo da lista
# 
# Podemos apagar o conteúdo inteiro da lista com `clear`.

# In[133]:


times.clear()
times # lista está vazia 


# Podemos contar o número de elementos da lista com `len`.

# In[134]:


len(times) # verifica que a lista está vazia


# In[135]:


type([]) # a lista é vazia, mas continua sendo lista 


# ### Outros métodos de lista

# Conte repetições de elementos na lista com `count`.

# In[136]:


numeros = [1,1,2,3,1,2,4,5,6,3,4,4,5,5]
print( numeros.count(1), numeros.count(3), numeros.count(7) )


# Localize a posição de um elemento com `index`.

# In[137]:


numeros.index(5) # retorna a posição da primeira aparição 


# Remova a primeira aparição do elemento com `remove`.

# In[138]:


numeros.remove(1) # perde apenas o primeiro
numeros


# Faça uma reflexão ("flip") *in-place* (sem criar nova lista) da lista com `reverse`.

# In[139]:


numeros.reverse() 
numeros


# Ordene a lista de maneira *in-place* (sem criar nova lista) com `sort`.

# In[140]:


numeros.sort()
numeros


# ## Concatenação de listas
# 
# Listas são concatenadas ("somadas") com `+`. Caso já possua listas definidas, use `extend`.

# In[141]:


['Flamengo', 'Botafogo'] + ['Fluminense']  


# In[142]:


['Flamengo', 'Botafogo'] + 'Fluminense' # erro: 'Fluminense' não é list


# In[143]:


times_nordeste = ['Fortaleza','Sport']
times_sul = ['Coritiba','Atlético-PR']
times_nordeste + times_sul 


# In[144]:


times_nordeste.extend(times_sul) # mesma coisa
times_nordeste 


# ## Fatiamento de listas 
# 
# O fatiamento ("slicing") permite que selecionemos partes da lista através do modelo `start:stop`, em que `start` é um índice incluído na iteração, e `stop` não. 

# In[145]:


letras = ['a','b','c','d','e','f','g']
letras[0:2]


# In[146]:


letras[1:4]


# In[147]:


letras[5:6]


# In[148]:


letras[0:7] # toda a lista


# ### Omissão de `start` e `stop`

# In[149]:


letras[:3] # até 3, exclusive


# In[150]:


letras[:5] # até 5, exclusive


# In[151]:


letras[4:] # de 4 em diante


# In[152]:


letras[6:] # de 6 em diante 


# ### Modo reverso

# In[153]:


letras[-1] # último índice 


# In[154]:


letras[-2:-1] # do penúltimo ao último, exclusive


# In[155]:


letras[-3:-1] 


# In[156]:


letras[-4:-2]


# In[157]:


letras[-7:-1] # toda a lista


# In[158]:


letras[-5:] 


# In[159]:


letras[:-3] 


# ## Elementos alternados com `step`
# 
# Podemos usar um dois pontos duplo (`::`) para dar um "passo" de alternância.

# In[160]:


letras[::2] # salta 2-1 intermediários 


# In[161]:


letras[::3] # salta 3-1 intermediários 


# In[162]:


letras[::7] # salto de igual tamanho 


# In[163]:


letras[::8] # salto além do tamanho


# ## Mutabilidade de listas
# 
# Podemos alterar o conteúdo de elementos diretamente por indexação.

# In[164]:


from sympy.abc import x,y

ops = [x+y,x-y,x*y,x/y]
ops2 = ops.copy() # cópia de ops
ops


# In[165]:


ops[0] = x-y
ops


# In[166]:


ops[2] = x/y
ops 


# In[167]:


ops[1], ops[3] = x + y, x*y # mutação por desempacotamento
ops


# In[168]:


ops[1:3] = [False, False, True] # mutação por fatiamento
ops


# In[169]:


ops = ops2 # recuperando ops 
ops


# In[170]:


ops2 is ops


# In[171]:


ops3 = [] # lista vazia
ops3


# In[172]:


ops2 = ops + ops3 # concatenação cria uma lista nova
ops2


# In[173]:


ops2 is ops # agora, ops2 não é ops 


# In[174]:


print(id(ops), id(ops2)) # imprime local na memória de ambas


# In[175]:


ops2 == ops # todos os elementos são iguais


# O teste de identidade é `False`, mas o teste de igualdade é `True`.

# **Exemplo:** Escreva uma função que calcule a área, perímetro, comprimento da diagonal, raio, perímetro e área do círculo inscrito, e armazene os resultados em uma lista. 

# In[176]:


# usaremos matemática simbólica
from sympy import symbols
from math import pi

# símbolos
B, H = symbols('B H',positive=True)

def propriedades_retangulo(B,H):
    '''
        A função assume que a base B 
        é maior do que a altura H. Senão, 
        as propriedades do círculo inscrito 
        não serão determinadas.        
    '''    
    d = (B**2 + H**2)**(1/2) # comprimento da diagonal
    r = H/2 # raio do círculo inscrito    
    return [B*H, 2*(B+H), d, r, 2*pi*r, pi*(r)**2]

# lista de objetos símbolos
propriedades_retangulo(B,H) 


# In[177]:


# substituindo valores
B, H = 4.0, 2.5

propriedades_retangulo(B,H)


# ### Formatação de strings
# 
# 
# O *template* a seguir usa a função `format` para substituição de valores indexados.
# 
# ```python
# templ = '{0} {1} ... {n}'.format(arg0,arg1,...,argn)
# ```
# 
# **Nota:** Para ajuda plena sobre formatação, consultar: 
# 
# ```python
# help('FORMATTING')
# ```

# In[178]:


# considere R: retângulo; C: círculo inscrito

res = propriedades_retangulo(B,H) # resultado

props = ['Área de R',
         'Perímetro de R',
         'Diagonal de R',
         'Raio de C',
         'Perímetro de C',
         'Área de C'
        ] # propriedades

# template 
templ = '{0:s} = {1:.2f}\n{2:s} = {3:.3f}\n{4:s} = {5:.4f}\n{6:s} = {7:.5f}\n{8:s} = {9:.6f}\n{10:s} = {11:.7f}'.format(props[0],res[0],                          props[1],res[1],                          props[2],res[2],                          props[3],res[3],                          props[4],res[4],                          props[5],res[5])

# impressão formatada
print(templ)


# ### Como interpretar o que fizemos? 
# 
# - `{0:s}` formata o primeiro argumento de `format`, o qual é `props[0]`, como `str` (`s`).
# - `{1:.2f}` formata o segundo argumento de `format`, o qual é `res[0]`, como `float` (`f`) com duas casas decimais (`.2`).
# - `{3:.3f}` formata o quarto argumento de `format`, o qual é `res[1]`, como `float` (`f`) com três casas decimais (`.3`).
# 
# A partir daí, percebe-se que um template `{X:.Yf}` diz para formatar o argumento `X` como `float` com `Y` casas decimais, ao passo que o template `{X:s}` diz para formatar o argumento `X` como `str`.

# Além disso, temos:
# 
# - `\n`, que significa "newline", isto é, uma quebra da linha.
# - `\`, que é um *caracter de escape* para continuidade da instrução na linha seguinte. No exemplo em tela, o *template* criado é do tipo *multi-line*. 
# 
# **Nota:** a contrabarra em `\n` também é um caracter de escape e não um caracter *literal*. Isto é, para imprimir uma contrabarra literalmente, é necessário fazer `\\`. Vejamos exemplos de literais a seguir.

# #### Exemplos de impressão de caracteres literais

# In[179]:


print('\\') # imprime contrabarra literal
print('\\\\') # imprime duas contrabarras literais
print('\'') # imprime plica 
print('\"') # imprime aspas


# #### f-strings
# 
# Temos uma maneira bastante interessante de criar templates usando f-strings, que foi introduzida a partir da versão Python 3.6. Com f-strings a substituição é imediata.

# In[180]:


print(f'{props[0]} = {res[0]}') # estilo f-string


# #### Estilos de formatação
# 
# Veja um comparativo de estilos:

# In[181]:


print('%s = %f ' % (props[0], res[0])) # Python 2
print('{} = {}'.format(props[0], res[0])) # Python 3
print('{0:s} = {1:.4f}'.format(props[0], res[0])) # Python 3 formatado


# **Exemplo:** Considere o conjunto: V = $\{ c \in \mathbb{A} \, ; \, c \text{ é vogal} \}.$ Crie a concatenação de todos os elementos com f-string.

# In[182]:


V = ['a','e','i','o','u']
V 


# In[183]:


f'{V[0]}{V[1]}{V[2]}{V[3]}{V[4]}' # pouco Pythônico


# Veremos à frente meios mais elegantes de fazer coisas similares.

# ## Controle de fluxo: laço `for`
# 
# Em Python, podemos realizar iterar por uma coleção ou iterador usando *laços*. Introduziremos aqui o laço `for`. Em Python, o bloco padrão para este laço é dado por: 
# 
# ```python
# for valor in sequencia:
#     # faça algo com valor
# ```
# 
# Acima, `valor` é um iterador.

# In[196]:


for v in vogais: # itera sobre lista inteira
    print(v)


# In[205]:


for v in vogais[0:3]: # itera parcialmente
    print(v + 'a')


# In[230]:


for v in vogais[-2:]: 
    print(f'{v*10}')


# ## Compreensão de lista
# 
# Usando `for`, a criação de listas torna-se bastante facilitada.

# **Exemplo:** crie a lista dos primeiros 10 quadrados perfeitos.

# In[251]:


Q = [q*q for q in range(1,11)]
Q


# A operação acima equivale a:

# In[252]:


Q2 = []
for q in range(1,11):
    Q2.append(q*q)
Q2        


# **Exemplo:** crie a PA: $a_n = 3 + 6(n-1), \, 1 \leq n \leq 10$

# In[256]:


PA = [3 + 6*(n-1) for n in range(1,11) ]
PA


# **Exemplo:** se $X = \{1,2,3\}$ e $Y=\{4,5,6\}$, crie a "soma" $X + Y$ elemento a elemento.

# In[266]:


X = [1,2,3]
Y = [4,5,6]

XsY = [ X[i] + Y[i] for i in range(len(X)) ]
XsY


# **Exemplo:** se $X = \{1,2,3\}$ e $Y=\{4,5,6\}$, cria o "produto" $X * Y$ elemento a elemento.

# In[268]:


XpY = [ X[i]*Y[i] for i in range(len(X)) ]
XpY


# ## Tuplas
# 
# Tuplas são são sequencias imutáveis de tamanho fixo. Em Matemática, uma tupla é uma sequência ordenada de elementos. Em geral, o termo $n-$upla ("ênupla") é usado para se referir a uma tupla com $n$ elementos.

# In[280]:


par = 1,2; par
par


# In[281]:


type(par)


# In[284]:


trio = (1,2,3); trio


# In[292]:


quad = (1,2,3,4); quad


# In[289]:


nome = 'Nome'; tuple(nome) # casting


# Tuplas são acessíveis por indexação.

# In[291]:


quad[2]


# In[293]:


quad[1:4]


# In[28]:


quad[3] = 5 # tuplas não são mutáveis


# Se na tupla houver uma lista, a lista é modificável.

# In[301]:


super_trio = tuple([1,[2,3],4]) # casting
super_trio


# In[302]:


super_trio[1].extend([4,5]) 
super_trio


# Tuplas também são concatenáveis com `+`.

# In[303]:


(2,3) + (4,3)


# In[304]:


('a',[1,2],(1,1)) # repetição


# ### Desempacotamento de tuplas

# In[311]:


a,b,c,d = (1,2,3,4)


# In[313]:


for i in [a,b,c,d]:
    print(i) # valor das variáveis


# In[339]:


a,b = (1,2)
a,b = b,a # troca de valores
a,b


# ### `enumerate`
# 
# Podemos controlar índice e valor ao iterar em uma sequencia.

# In[4]:


X = [1,2,3] # lista / sequencia

for i,x in enumerate(X): # (i,x) é uma tupla (índice,valor)
    print(f'{i} : {x}')


# **Exemplo:** Construa o produto cartesiano 
# 
# $$A \times B = \{(a,b) \in \mathbb{Z} \times \mathbb{Z} \, ; \, -4 \leq a \leq 4 \wedge 3 \leq b \leq 7\}$$

# In[16]:


AB = [(a,b) for a in range(-4,5) for b in range(3,8)]
print(AB)


# ## Dicionários
# 
# Dicionários, ou especificamente, objetos `dict`, possuem extrema versatilidade e são muito poderosos. Criamos um `dict` por diversas formas. A mais simples é usar chaves e pares explícitos.

# In[17]:


d = {} # dict vazio
d


# In[18]:


type(d)


# Os pares chave-valor incorporam quaisquer tipos de dados.

# In[30]:


d = {'par': [0,2,4,6,8], 'ímpar': [1,3,5,7,9], 'nome':'Meu dict', 'teste': True}
d


# ### Acesso a conteúdo

# Para acessar o conteúdo de uma chave, indexamos pelo seu nome.

# In[33]:


d['par'] 


# In[35]:


d['nome']


# **Exemplo:** construindo soma e multiplicação especial.

# In[38]:


# dict
op = {'X' :[1,2,3], 'delta' : 0.1}

# função
def sp(op):
    s = [x + op['delta'] for x in op['X']]
    p = [x * op['delta'] for x in op['X']]
    
    return (s,p) # retorna tupla

soma, prod = sp(op) # desempacota

for i,s in enumerate(soma):
    print(f'pos({i}) | Soma = {s} | Prod = {prod[i]}')


# ### Inserção de conteúdo

# In[67]:


# apensa variáveis
op[1] = 3 
op['novo'] = (3,4,1) 
op


# ### Alteração de conteúdo

# In[68]:


op['novo'] = [2,1,4] # sobrescreve
op


# ### Deleção de conteúdo com `del` e `pop`

# In[69]:


del op[1] # deleta chave 
op 


# In[70]:


novo = op.pop('novo') # retorna e simultaneamente deleta
novo


# In[71]:


op


# ### Listagem de chaves e valores
# 
# Usamos os métodos `keys()` e `values()` para listar chaves e valores.

# In[81]:


arit = {'soma': '+', 'subtr': '-', 'mult': '*', 'div': '/'} # dict
k = list(arit.keys())
#print(k)
val = list(arit.values())
#print(val)

for v in range(len(arit)):
    print(f'A operação \'{k[v]}\' de "arit" usa o símbolo \'{val[v]}\'.')


# ### Combinando dicionários
# 
# Usamos `update` para combinar dicionários. Este método possui um resultado similar a `extend`, usado em listas.

# In[83]:


pot = {'pot': '**'}
arit.update(pot)
arit


# ### Dicionários a partir de sequencias
# 
# Podemos criar dicionários a partir de sequencias existentes usando `zip`.

# In[89]:


arit = ['soma', 'subtr', 'mult', 'div', 'pot']
ops = ['+', '-', '*', '/', '**']

dict_novo = {}

for chave,valor in zip(arit,ops):
    dict_novo[chave] = valor
    
dict_novo


# Visto que um `dict` é composto de várias tuplas de 2, podemos criar um  de maneira ainda mais simples.

# In[90]:


dict_novo = dict(zip(arit,ops))
dict_novo


# ### *Hashability*
# 
# Dissemos acima que os valores de um `dict` podem ser qualquer objeto Python. Porém, as chaves estão limitadas por uma propriedade chamada *hashability*. Um objeto *hashable* em geral é imutável. Para saber se um objeto pode ser usado como chave de um `dict`, use a função `hash`. Caso retorne erro, a possibilidade de *hashing* é descartada. 

# In[145]:


# todos aqui são imutáveis, portanto hashable' 
hash('s'), hash(2), hash(2.1), hash((1,2))


# In[109]:


# não hashable 
hash([1,2]), hash((1,2),[3,4])


# Para usar `list` como chave, podemos convertê-las em `tuple`.

# In[146]:


d = {}; d[tuple([1,2])] = 'hasheando lista em tupla'; d


# ## Compreensão de dicionário
# 
# Podemos usar `for` para criar dicionários de maneira esperta do mesmo modo que as compreensões de lista com a distinção de incluir pares chaves/valor.

# In[94]:


{chave:valor for chave,valor in enumerate(arit)} # chave:valor


# In[148]:


{valor:chave for chave,valor in enumerate(arit)} # valor:chave

