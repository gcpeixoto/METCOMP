#!/usr/bin/env python
# coding: utf-8

# # Leitura e Escrita de Arquivos de Planilha
# 
# Grande parte da informação que é manipulada no terceiro setor e na indústria encontra-se estruturada na forma de planilhas intercambiáveis entre programas bem conhecidos, tais como _Microsoft Excel_, _LibreOffice Calc_ e _Apple Numbers_. Planilhas compõem-se de tabelas que contém texto e números dispostos em células. 
# 
# Hoje em dia, o formato de arquivo `.csv` (_comma separated values_), ou _valores separados com vírgula_, tem ganhado notoriedade em diversas áreas, principalmente ciência e análise de dados. Para um engenheiro, a linguagem Python pode oferecer uma enorme gama de utilidades para tratamento de dados tabelados, permitindo que o trabalho conjunto com softwares de planilha seja expandido.
# 
# Neste capítulo, aprenderemos a ler e a escrever arquivos em formato `.csv` para realizar análises e cálculos estatísticos básicos, dando enfoque à biblioteca _Pandas_.

# ## Motivação 
# 
# O arquivo [autos.csv](./data/autos.csv) contém uma planilha relacionando modelos automotivos com sua massa (em kg) e consumo (em km/litro). Usaremos essas informações para realizar algumas análises. 

# ## Leitura de arquivos
# 
# Usaremos a função `read_csv` para ler o arquivo.

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./data/autos.csv')
df


# ## _Series_ e _DataFrames_
# 
# A variável `df` é um _DataFrame_, uma tabela (bidimensional) com cada coluna formada como uma _Series_. Uma _Series_ (série) é um _array_ unidimensional que possui um índice para cada entrada e tipos de dados variáveis.

# ### Selecionando colunas e valores
# 
# Para acessar as colunas, usamos indexação:

# In[2]:


modelo = df['modelo']
modelo


# Para acessar os valores, usamos `values`:

# In[3]:


modelo.values


# Notemos que `modelo` é uma série, mas `modelo.values` é um _array_ 1D.

# In[4]:


type(modelo)


# In[5]:


type(modelo.values)


# Enquanto a série acima armazena objetos `str`, as demais armazenam valores numéricos.

# In[6]:


massa = df['massa (kg)'].values
massa


# In[7]:


consumo = df['C (km/litro)'].values
consumo


# ### Renomeando colunas
# 
# Vamos renomear as colunas através de um `dict` para facilitar a manipulação.

# In[8]:


# mapa de renomeação
n = {'massa (kg)':'M',
     'C (km/litro)': 'C' }

# renomeia colunas
df = df.rename(columns=n)
df


# ### Identificando máximos, mínimos e médias
# 
# Buscando os valores para _massa_:

# In[9]:


# máximo
df['M'].max()


# In[10]:


# mínimo
df['M'].min()


# In[11]:


# média
df['M'].mean()


# Buscando os valores para _consumo_:

# In[12]:


# máximo
df['C'].max()


# In[13]:


# mínimo
df['C'].min()


# In[14]:


# média
df['C'].mean()


# Encontrando os índices correspondentes:

# In[15]:


np.argmin(df['M'])


# In[16]:


np.argmax(df['M'])


# In[17]:


np.argmin(df['C'])


# In[18]:


np.argmax(df['C'])


# ## Acessando dados por índice
# 
# Primeiramente, notemos que os índices forma um array. 

# In[19]:


df.index


# In[20]:


# converte para array
df.index.to_numpy()


# Para acessar entradas pelo índice usamos `iloc`.

# In[21]:


# massa máxima no índice 2
df.iloc[2]['M']


# In[22]:


# consumo máximo no índice 7
df.iloc[7]['C']


# ## Selecionando subtabelas

# In[23]:


df.iloc[0:5]


# In[24]:


# salto de 2
df.iloc[::2]


# Restringindo colunas:

# In[25]:


df.iloc[0:2]['M']


# In[26]:


# apenas considera colunas 'M' e 'C'
df.iloc[3:9][['M','C']]


# ## Plotando dados
# 
# Podemos plotar dados diretamente a partir das séries.

# In[27]:


plt.plot(df['M'],df['C'],'o')
plt.xlabel('massa')
plt.ylabel('consumo');


# In[28]:


plt.hist(df['M'],color=[0.5,0.5,0.5])
plt.title('Histograma');


# ## Adicionando colunas
# 
# Suponhamos que queiramos computar o índice massa/consumo e seu inverso e adicioná-los como colunas em nossa planilha. Podemos fazer isso diretamente com:

# In[29]:


# cria coluna 'M/C'
df['M/C'] = df['M']/df['C']
df['C/M'] = 1./df['M/C']
df


# ## Escrita de arquivos
# 
# Para exportar nossa nova planilha para um novo arquivo, digamos `autos-novo.csv`, fazemos:

# In[30]:


df.to_csv('data/autos-novo.csv',index=False)


# Podemos checar novamente o conteúdo do novo arquivo com:

# In[31]:


dfnovo = pd.read_csv('data/autos-novo.csv')
dfnovo


# Caso seu arquivo seja muito grande, é possível visualizar parte dele usando `head` e `tail`.

# In[32]:


# 'cabeça' do arquivo
dfnovo.head()


# In[33]:


# 'cauda' do arquivo
dfnovo.tail()


# ## Estatística Descritiva
# 
# Algumas medidas importantes da estatística podem ser calculadas diretamente com _DataFrames_. Aqui, aprenderemos a calcular duas classes:
# 
# - medidas de posição: média, moda, mediana
# - medidas de dispersão: amplitude, desvio médio, desvio padrão, variância

# ### Medidas de posição

# In[34]:


# consumo
c = df['C']


# In[35]:


# média
c.mean()


# In[36]:


# moda: valores mais frequentes
c.mode()


# In[37]:


# mediana
c.median()


# ### Medidas de dispersão

# In[38]:


# amplitude
c.max() - c.min()


# In[39]:


# desvio médio
c.mad()


# In[40]:


# desvio padrão
c.std()


# In[41]:


# variância
c.var()

