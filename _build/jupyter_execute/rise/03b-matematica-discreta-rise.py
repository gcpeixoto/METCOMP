#!/usr/bin/env python
# coding: utf-8

# # Fundamentos de Matemática Discreta com Python - Parte 2

# ## Controle de fluxo: condicionais `if`, `elif` e `else`
# 
# 
# ```python
# if condição:
#     # faça algo
# ```
# 
# Este bloco diz basicamente o seguinte: "faça algo se a condição for verdadeira". Vejamos alguns exemplos.

# In[2]:


if 2 > 0: # a condição é 'True'
    print("2 é maior do que 0!") 


# In[3]:


2 > 0 # esta é a condição que está sendo avaliada


# In[3]:


if 2 < 1: # nada é impresso porque a condição é 'False'
    print("2 é maior do que 0!") 


# In[16]:


2 < 1 # esta é a condição que está sendo avaliada


# A condição pode ser formada de diversas formas desde que possa ser avaliada como `True` ou `False`.

# In[7]:


x, y = 2, 4
if x < y:
    print(f'{x} < {y}')


# - A estrutura condicional pode ser ampliada com um ou mais `elif` ("ou se") e com `else` (senão). 
# - Se nenhum `elif` for `True`, `else` será executado. 

# **Exemplo:** teste da tricotomia. Verificar se um número é $>$, $<$ ou $= 0$.

# In[36]:


'''
x = 4.1 # número para teste

if x < 0: # se
    print(f'{x} < 0')
elif x > 0: # ou se
    print(f'{x} > 0')
else: # senão
    print(f'{x} = 0')
''';

objetos_da_sala_de_aula = ['mesa','quadro','apagador','lâmpada']
obj = ['giz','cabo eletrico','projetor','cadeira']

if obj[0] in objetos_da_sala_de_aula:
    print(f'{obj[0]} não está em falta.')    
elif obj[0] not in objetos_da_sala_de_aula:
    print(f'É necessário comprar {obj[0]}.')
elif obj[1] in objetos_da_sala_de_aula:
    print(f'{obj[1]} não está em falta.')    
elif obj[1] not in objetos_da_sala_de_aula:
    print(f'É necessário comprar {obj[1]}.')    
elif obj[2] in objetos_da_sala_de_aula:
    print(f'{obj[2]} não está em falta.')   
elif obj[2] not in objetos_da_sala_de_aula:
    print(f'É necessário comprar {obj[2]}.')    


# **Exemplo:** Considere o conjunto de classificações sanguíneas ABO (+/-) 
# 
# $$S = \{\text{A+}, \text{A-}, \text{B+}, \text{B-}, \text{AB+}, \text{AB-}, \text{O+}, \text{O-}\}$$
# 
# Se em um experimento aleatório, $n$ pessoas ($n \geq 500$) diferentes entrassem por um hospital em um único dia, qual seria a probabilidade de $p$ entre as $n$ pessoas serem classificadas como um(a) doador(a) universal (sangue $\text{O-}$) naquele dia? Em seguida, estime a probabilidade das demais.

# In[47]:


# 'randint' gera inteiros aleatoriamente
from random import randint 

# número de pessoas  
n = 150000 

# associa inteiros 0-7 ao tipo sanguíneo
tipos = [i for i in range(0,8)]   
sangue = dict(zip(tipos,['A+','A-','B+','B-','AB+','AB-','O+','O-'])) 


# In[48]:


# primeira pessoa
i = randint(0,8) 

# grupo sanguíneo
s = [] 

# repete n vezes
for _ in range(0,n): # _ significa uma variável inutilizada, mas necessária para criar a repetição
    if i == 0:
        s.append(0)
    elif i == 1:
        s.append(1)
    elif i == 2:
        s.append(2)
    elif i == 3:
        s.append(3)
    elif i == 4:
        s.append(4)
    elif i == 5:
        s.append(5)
    elif i == 6: 
        s.append(6)
    else:
        s.append(7)
        
    i = randint(0,8) # nova pessoa


# In[49]:


# calcula a probabilidade do tipo p em %. 
# Seria necessário definir uma lambda? 
prob = lambda p: p/n*100
        
# armazena probabilidades no dict P 
P = {}
for tipo in tipos:
    P[tipo] = prob(s.count(tipo))
    if sangue[tipo] == 'O-':
        print('A probabilidade de ser doador universal é de {0:.2f}%.'.format(P[tipo]))        
    else:
        print('A probabilidade de ser {0:s} é de {1:.2f}%.'.format(sangue[tipo],P[tipo]))        


# ## Conjuntos
# 
# As estruturas `set` (conjunto) são úteis para realizar operações com conjuntos.

# In[15]:


set(['a','b','c']) # criando por função


# In[145]:


{'a','b','c'} # criando de modo literal


# In[83]:


{1,2,2,3,3,4,4,4} # 'set' possui unicidade de elementos


# ### União de conjuntos
# 
# Considere os seguintes conjuntos.

# In[146]:


A = {1,2,3}
B = {3,4,5}
C = {6}


# In[147]:


A.union(B) # união


# In[148]:


A | B # união com operador alternativo ('ou')


# ### Atualização de conjuntos (união)
# 
# A união *in-place* de dois conjuntos pode ser feita com `update`.

# In[150]:


C


# In[88]:


C.update(B) # C é atualizado com elementos de B
C


# In[152]:


C.union(A) # conjunto união com A


# In[91]:


C # os elementos de A não foram atualizados em C


# A atualização da união possui a seguinte forma alternativa com `|=`.

# In[153]:


C |= A # elementos de A atualizados em C
C


# ### Interseção de conjuntos

# In[154]:


A.intersection(B) # interseção


# In[155]:


A & B # interseção com operador alternativo ('e')


# ### Atualização de conjuntos (interseção)
# 
# A interseção *in-place* de dois conjuntos pode ser feita com `intersection_update`.

# In[156]:


D = {1, 2, 3, 4}
E = {2, 3, 4, 5}


# In[157]:


D.intersection(E) # interseção com E


# In[159]:


D # D inalterado


# In[102]:


D.intersection_update(E) 
D # D alterado


# A atualização da interseção possui a seguinte forma alternativa com `&=`.

# In[160]:


D &= E
D 


# ### Diferença entre conjuntos

# In[161]:


A


# In[162]:


D


# In[163]:


A.difference(D) # apenas elementos de A


# In[164]:


D.difference(A) # apenas elementos de D


# In[165]:


A - D # operador alternativo 


# In[166]:


D - A 


# ### Atualização de conjuntos (diferença)
# 
# A interseção *in-place* de dois conjuntos pode ser feita com `difference_update`.

# In[167]:


D = {1, 2, 3, 4}
E = {1, 2, 3, 5} 


# In[169]:


D 


# In[170]:


D.difference(E)
D


# In[114]:


D.difference_update(E)
D


# A atualização da diferença possui a seguinte forma alternativa com `-=`.

# In[171]:


D -= E
D


# ### Adição ou remoção de elementos

# In[172]:


A


# In[117]:


A.add(4) # adiciona 4 a A
A


# In[174]:


B


# In[119]:


B.remove(3) # remove 3 de B
B


# ### Reinicialização de um conjunto (vazio)
# 
# Podemos remover todos os elementos de um conjunto com `clear`, deixando-o em um estado vazio.

# In[175]:


A


# In[177]:


A.clear()
A # A é vazio 


# In[123]:


len(A) # 0 elementos


# ### Diferença simétrica
# 
# A diferença simétrica entre dois conjuntos $A$ e $B$ é dada pela união dos complementares relativos: 
# 
# $$A \triangle B = A\backslash B \cup B\backslash A$$
# 
# Logo, em $A \triangle B$ estarão todos os elementos que pertencem a $A$ ou a $B$ mas não aqueles que são comuns a ambos.
# 
# **Nota:** os complementares relativos $A\backslash B$ e $B\backslash A$ aqui podem ser interpretados como $A-B$ e $B-A$. Os símbolos $\backslash$ e $-$ em conjuntos podem ter sentidos diferentes em alguns contextos.

# In[178]:


G = {1,2,3,4}
H = {3,4,5,6}


# In[180]:


G.symmetric_difference(H) # {3,4} ficam de fora, pois são interseção


# In[127]:


G ^ H # operador alternativo


# ### Atualização de conjuntos (diferença simétrica)
# 
# A diferença simétrica *in-place* de dois conjuntos pode ser feita com `symmetric_difference_update`.

# In[181]:


G


# In[182]:


G.symmetric_difference_update(H) 
G # alterado 


# In[183]:


G ^= H # operador alternativo
G 


# ### Continência
# 
# Podemos verificar se um conjunto $A$ é subconjunto de (está contido em) outro conjunto $B$ ($A \subseteq B$) ou se $B$ é um superconjunto para (contém) $A$ ($B \supseteq A$) com `issubset` e  `issuperset`. 

# In[184]:


B


# In[186]:


C


# In[188]:


B.issubset(C) # B está contido em C


# In[190]:


C.issuperset(B) # C contém B


# ## Subconjuntos e subconjuntos próprios
# 
# Podemos usar operadores de comparação entre conjuntos para verificar continência.
# 
# - $A \subseteq B$: $A$ é subconjunto de $B$
# - $A \subset B$: $A$ é subconjunto próprio de $B$ ($A$ possui elementos que não estão em $B$)

# In[191]:


{1,2,3} <= {1,2,3} # subconjunto


# In[193]:


{1,2} < {1,2,3} # subconjunto próprio


# In[194]:


{1,2,3} > {1,2}


# In[196]:


{1,2} >= {1,2,3} 


# ### Disjunção
# 
# Dois conjuntos são disjuntos se sua interseção é vazia. Podemos verificar a disjunção com `isdisjoint`

# In[197]:


E


# In[199]:


G


# In[200]:


E.isdisjoint(G) # 1,2,5 são comuns


# In[201]:


D


# In[203]:


E.isdisjoint(D)


# In[204]:


A


# In[206]:


E.isdisjoint(A)


# ### Igualdade entre conjuntos
# 
# Dois conjuntos são iguais se contém os mesmos elementos.

# In[207]:


H = {3,'a', 2}
I = {'a',2, 3} 
J = {1,'a'}


# In[208]:


H == I


# In[209]:


H == J


# In[211]:


{1,2,2,3} == {3,3,3,2,1} # lembre-se da unicidade


# ## Compreensão de conjunto
# 
# Podemos usar `for` para criar conjuntos de maneira esperta do mesmo modo que as compreensões de lista e de dicionários. Neste caso, o funcionamento é como `list`, porém, em vez de colchetes, usamos chaves.

# In[69]:


{e for e in range(0,10)}


# In[212]:


{(i,v) for (i,v) in enumerate(range(0,4))}


# ## Sobrecarga de operadores
# 
# Em Python, podemos realizar alguns procedimentos úteis para laços de repetição.

# In[57]:


x = 2
x += 1 # x = 2 + 1 (incrementação)
x  


# In[ ]:





# In[52]:


y = 3
y -= 1 # y = 3 - 1 (decrementação)
y


# In[56]:


z = 2
z *= 2 # z = 2*2


# In[58]:


t = 3
t /= 3 # t = 3/3
t


# **Exemplo:** verifique se a soma das probabilidades no `dict` `P` do experimento aleatório é realmente 100%.

# In[59]:


s = 0
for p in P.values(): # itera sobre os valores de P
    s += p # soma cumulativa
print(f'A soma de P é {s}%')


# De modo mais Pythônico:

# In[60]:


sum(P.values()) == 100


# Ou ainda:

# In[63]:


if sum(P.values()) == 100:
    print(f'A soma de P é {s}%')
else:
    print(f'Há erro no cálculo!') 


# ## Controle de fluxo: laço `while`
# 
# - O condicional `while` permite que um bloco de código seja repetidamente executado até que uma dada condição seja avaliada como `False`
# - Ou o laço seja explicitamente terminado com a keyword `break`.
# - Em laços `while`, é muito comum usar uma linha de atualização da condição usando sobrecarga de operadores.
# 
# A instrução é como segue: 
# 
# 
# ```python
# while condicao:
#     # faça isso 
#     # atualize condicao
# ```

# In[1]:


x = 10
boom = 0
while x > boom: # não leva em conta igualdade
    print(x)
    x -= 1 # atualizando por decrementação
print('Boom!') 


# In[227]:


x = 5
boom = 10
while x <= boom: # leva em conta igualdade
    print(x) 
    x += 0.5 # atualizando por incrementação   


# In[17]:


from math import sin,pi
x = 1.0
i = 1
while x**3 > 0:
    if i % 100 == 0: # imprime apenas a cada 100 repetições
        print(f'Repeti {i} vezes e x = {x**3}. Contando...')     
    x -= 1e-3  # atualiza o decremento
    i += 1 # contagem de repetição
print(f'x = {x**3}')


# In[230]:


from math import sin,pi
x = 1.0
i = 1
while x**3 > 0:
    if i % 100 == 0: # imprime apenas a cada 1000 repetições
        print(f'Repeti {i} vezes e x = {x**3}. Contando...')    
    if i == 500:
        print(f'Repeti demais. Vou parar.')  
        break # execução interrompida aqui       
    x -= 1e-3  # atualiza o decremento
    i += 1 # contagem de repetição
print(f'x = {x**3}')


# **Exemplo:** construa seu próprio gerador de números aleatórios para o problema da entrada de pessoas no hospital.

# In[2]:


# exemplo simples
def meu_gerador():
    nums = []
    while True: # executa indefinidamente até se digitar ''
        entr = input() # entrada do usuário            
        nums.append(entr) # armazena         
        if entr == '': # pare se nada mais for inserido
            return list(map(int,nums[:-1])) # converte para int e remove '' da lista


# In[3]:


# execução: 
# 2; shift+ENTER; para 2
# 3; shift+ENTER; para 3
# 4; shift+ENTER; para 4
# shift+ENTER; para nada
nums = meu_gerador() 
nums


# **Exemplo:** verifique se a soma das probabilidades no `dict` `P` do experimento aleatório é realmente 100%.

# In[84]:


sum(P.values())


# ## `map`
# 
# A função `map` serve para construir uma função que será aplicada a todos os elementos de uma sequencia. Seu uso é da seguinte forma: 
# 
# ```python
# map(funcao,sequencia)
# ``` 
# 
# No exemplo anterior, as entradas do usuário são armazenadas como `str`, isto é, '2', '3' e '4'. Para que elas sejam convertidas para `int`, nós executamos um *casting* em todos os elementos da sequencia usando `map`. 
# 
# A interpretação é a seguinte: para todo `x` pertencente a `sequencia`, aplique `funcao(x)`. Porém, para se obter o resultado desejado, devemos ainda aplicar `list` sobre o `map`.

# In[12]:


nums = ['2','3','4']
nums


# In[13]:


m = map(int,nums) # aplica a função 'int' aos elementos de 'num'
m


# Observe que a resposta de `map` não é *human-readable*. Para lermos o que queremos, fazemos:

# In[14]:


l = list(m) # aplica 'list' sobre 'map'
l


# Podemos substituir `funcao` por uma função anônima. Assim, suponha que você quisesse enviezar os valores de entrada somando 1 a cada número. Poderíamos fazer isso como:

# In[15]:


list(map(lambda x: x**2,l)) # eleva elementos ao quadrado


# ## `filter`
# 
# - Podemos aplicar um "filtro" usando a função `filter`. 
# - No caso anterior, consideramos um `dict` cujo valor das chaves é no máximo 7. 
# - Podemos filtrar a lista para coletar apenas valores menores do que 7. 
# - Para tanto, definimos uma função `lambda` com este propósito.

# In[16]:


lista_erronea = [2,9,4,6,7,1,9,10,2,4,5,2,7,7,11,7,6]
lista_erronea


# In[90]:


f = filter(lambda x: x <= 7, lista_erronea) # aplica filtro
f


# In[91]:


lista_corrigida = list(f) # valores > 7 excluídos
lista_corrigida


# ## Exemplos com maior complexidade

# **Exemplo:** Podemos escrever outro gerador de forma mais complexa. Estude este caso (pouco Pythônico).

# In[48]:


import random

la = random.sample(range(0,1000),1000) # escolhe 1000 números numa lista aleatória de 0 a 1000
teste = lambda x: -1 if x >= 8 else x # retorna x no intervalo [0,7], senão o próprio número
f = list(map(teste,la))
final = list(filter(lambda x: x != -1,f)) # remove > 8
final


# **Exemplo:** Associando arbitrariamente o identificador de uma pessoa a um tipo sanguíneo com compreensão de `dict`.

# In[52]:


id_pessoas = {chave:x for chave,x in enumerate(f) if x > -1} # compreensão de dicionário com if
id_pessoas

