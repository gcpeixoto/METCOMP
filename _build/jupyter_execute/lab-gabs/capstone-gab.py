#!/usr/bin/env python
# coding: utf-8

# # Projeto Final - Métodos Computacionais - 2020/02 (Real 2021/01)
# 
# **Nota:** use 3 dígitos de precisão para arredondar as respostas (`round(x,3)`).
# 
# ## Motivação
# 
# A Fig. 1 mostra perfis laterais do automóvel _Tesla Model 3_ em sua forma original e aproximada.
# 
# ```{figure} ./figs/capstone/tesla-3-profiles.png
# ---
# width: 300px
# name: cycle-ds
# ---
# Perfis do modelo Tesla 3: original e aproximado.
# ```
# 
# Considere que o perfil aproximado da carcaça do _Tesla Model 3_ corresponde ao plano de corte médio ($x-z$) perpendicular ao vetor diretor que determina o eixo normal ao papel $y$ (largura do veículo). A Fig. 2 mostra esboços do perfil aproximado, em destaque, bem como uma visão tridimensional que o replica ao longo da terceira dimensão (largura).
# 
# ```{figure} ./figs/capstone/tesla-3-3d.png
# ---
# width: 400px
# name: cycle-ds
# ---
# Perfil cotado do modelo Tesla 3: perfis 2D e 3D.
# ```

# ### Dados de entrada
# 
# Considere os seguintes dados do problema, onde $m(\overline{AB})$, por exemplo, representa a medida do segmento $\overline{AB}$.
# 
# - $m(\overline{OF}) = 4.694 \, m$ (comprimento do veículo)
# - $m(\overline{HG}) = 2.875 \, m$ (_wheelbase_)
# - $m(\overline{OC'}) = 0.26 \, m(OF)$
# - $m(\overline{J'J''}) = h = 1.443 \, m$
# - $m(\overline{HH'}) = r = 0.254 \, m$
# - $m(\overline{EF}) = 0.196m(\overline{OF}) \, m$
# - $m(\overline{AC'}) = 0.028m(\overline{OF}) \, m$
# - $\Delta x = 0.36m(\overline{HG})
# - $2y = 1.849 \, m$ (largura) 
# 
# Adicionalmente, considere que:
# 
# - O ponto $O$ é a origem do plano $(x,z)$ e ponto médio do segmento de comprimento $2y$ (largura).
# - O ponto $B$ possui a mesma coordenada $z$ do ponto que, juntamente com $H$, produz um segmento paralelo ao segmento $\overline{OB}$.
# - O ponto $C'$ é a projeção de $C$.
# - O ponto $A$ é tangente ao arco da roda dianteira.
# 
# ### Perfil da carcaça
# 
# Consideramos duas funções polinomiais, $z = f_1(x)$ e $z = f_2(x)$, para aproximar o perfil total $z = f(x)$ da carcaça do veículo, dividido entre a parte do capô (cor verde) e o teto (cor vermelha). O perfil é definido por:
# 
# $$f(x) = 
# \begin{cases}
# f_1(x), & \text{se} \ \ 0 \leq x \leq 1.200 \\
# f_2(x), & \text{se} \ \ 1.200 < x \leq 4.694
# \end{cases},$$
# onde 
# 
# $$f_1(x) = - 0.005332578925
# + 0.5463459255x 
# + 0.08146419954x^2 
# - 1.252167345x^3 
# + 1.25979124x^4 
# - 0.3450922701x^5 
# + h_1$$
# 
# e
# 
# $$f_2(x) = 2.73575898888339 
# - 7.11069548788072x
# + 6.41934813696066x^2
# - 0.987835568812394x^3
# - 1.60223473322946x^4
# + 1.09085209373009x^5
# - 0.305386264116437x^6
# + 0.0411721062624371x^7
# - 0.00219320927672036x^8
# + h_2$$

# ## Problema 1 (Volume de carcaça)
# 
# Determine o volume $V$ da carcaça do Tesla 3 assumindo o perfil aproximado supracitado e que a área da figura do plano médio replica-se de maneira constante por translação deste plano ao longo do eixo $y$ (para a direção positiva $+y$ e negativa $-y$), assim perfazendo uma largura medindo $w$ (Veja Figura 3D). Note que a área no plano médio em questão está limitada acima pela função $f(x)$ e abaixo, pela função $g(x) = 0$ (eixo $x$).
# 
# Use o seguinte roteiro para a solução: 
# 
# 1. Calcular o valor do ângulo $\theta$.
# 
# 2. Calcular a área do setor circular representativo do espaço ocupado pelas rodas (note que a geometria do setor circular no perfil médio estende-se ao longo da terceira dimensão tanto para a roda dianteira quanto traseira).
# 
# 3. Calcule o valor de $h_1$.
# 
# 4. Calcule a área líquida OBCC', ou seja, excluindo-se a área do setor circular dianteiro.
# 
# 5. Calcule a área líquida C'CEF, ou seja, excluindo-se a área do setor circular traseiro.
# 
# 6. Calcule o volume usando a hipótese de translação.
# 
# **Nota:** observe que, para os itens 4 e 5, é necessário calcular integrais. Vide apêndice _Calculando integrais numericamente_.

# ### Solução

# 1. O ângulo $\theta$ pode ser calculado como `theta = arcsen(AC'/r)`

# In[1]:


import numpy as np
import pandas as pd
from scipy.integrate import quad

OF = 4.694
AC_ = 0.028*OF
r = 0.254
theta = np.arcsin(AC_/r)
print(f'θ = {round(np.rad2deg(theta),3)} graus')


# 2. Para o cálculo da área do setor circular, observar que HA é paralelo a H'C'. O arco inferior tem abertura $2\theta$, de modo que o arco complementar tem abertura de $2\pi - 2\theta$. 
# 
# Usar a fórmula $A_S = \alpha r^2/2$ para a área.

# In[2]:


A_S = 2*(np.pi - theta)*r**2/2
print(f'Área do setor = {round(A_S,3)} m2')


# 3. Pela perpendicularidade de OB a HB', onde B' é o "pico" do arco, temos $h_1 = m(AC') + r$.

# In[3]:


h1 = AC_ + r
print(f'h1 = {round(h1,3)} m')


# 4. O cálculo de cada área líquida deve ser dado por  $I_j = \int_{a_j}^{b_j} f_j(x) \, dx - A_S, \ \ j = 1,2$

# In[4]:


# m(EF)
h2 = 0.196*OF

# perfil do capô
f1 = lambda x: - 0.005332578925 + 0.5463459255*x + 0.08146419954*x**2          -1.252167345*x**3 + 1.25979124*x**4 - 0.3450922701*x**5 + h1

# perfil teto/hatch
f2 = lambda x: 2.73575898888339 - 7.11069548788072*x + 6.41934813696066*x**2      -.987835568812394*x**3 - 1.60223473322946*x**4 + 1.09085209373009*x**5      -.305386264116437*x**6 + 0.0411721062624371*x**7 - 0.00219320927672036*x**8 + h2

I1,e1 = quad(f1,0,1.2)
I2,e2 = quad(f2,1.2,OF)

I1 = I1 - A_S
I2 = I2 - A_S

print(f'Integral 1 = {round(I1,3)} m2')
print(f'Integral 2 = {round(I2,3)} m2')


# 6. O cálculo do volume deve ser dado diretamente por $V=2y(I_1 + I_2)$ 

# In[5]:


y = 1.849/2
V = 2*y*(I1 + I2)
print(f'V = {round(V,3)} m3')


# ## Problema 2 (Movimento de gotícula)
# 
# Considere que o Tesla 3 está em movimento em uma _Autobanh_ alemã e que, em um certo momento da viagem, uma massa de água respingue sobre o capô. Na Fig. 2, representamos a trajetória executada por uma gotícula de água dessa massa que resvala o capô do automóvel e descola-se do para-brisa exatamente no ponto $D$, cujas coordenadas são dadas por $(x_D,y_D) = (1.2 + 0.082m(\overline{OF}),h_2 + 0.055m(\overline{OF}))$, a uma velocidade inicial $V = 1.5 \, m/s$.
# 
# Suponha que a gotícula realize um movimento perfeitamente parabólico atingindo a altura máxima no ponto $J$, que dista verticalmente de $\delta h$ do teto do automóvel, e horizontalmente de $\Delta x$ do ponto de descolamento. Determine:
# 
# - o valor de $\delta h$, em metros;
# - o valor de $\Delta x$, em metros;
# - a coordenada $x$, em metros, do veículo em que a gotícula atinge a altura máxima;
# - o tempo, em segundos, que a gotícula leva para realizar o movimento parabólico completo em segundos.
# 
# **Nota:** use as equações usuais para o movimento de um projétil tomando $(x_D,y_D)$ como ponto de lançamento e assuma a constante de gravidade igual a $9.81 \, m/s^$2.

# ### Solução

# Para este problema, aplicamos as equações padrão do movimento de projéteis, com deslocamento
# 
# - altura máxima: $H_{max} = y_D + \frac{V^2\sin^2(\theta)}{2g}$
# - alcance: $X = x_D + \frac{V^2\sin(2\theta)}{g}$
# - tempo: $T = \frac{2V\sin(\theta)}{g}$
# 
# Daí, segue que $\delta h = H_{max} - h$, e $\Delta X = X/2$.

# In[28]:


xD,yD = 1.2 + 0.082*OF, h2 + 0.055*OF
V = 4.5 # velocidade
h = 1.443 # altura do carro
g = 9.81 # gravidade

H_max = yD + V**2*np.sin(theta)**2/(2*g)
X = xD + V**2*np.sin(2*theta)/g
T = 2*V*np.sin(theta)/g

print(f'dh = {round(H_max - h,3)} m')
print(f'Δx = {round(X/2,3)} m')
print(f'x = {round(xD + X/2,3)} m')
print(f't = {round(T,3)} s')


# ## Problema 3 (Análise de veículos elétricos) 
# 
# A planilha [smart-vehicle-epa-2020.xlsx](data/smart-vehicle-epa-2020.xlsx) agrega informações sobre modelos de automóveis movidos a eletricidade e/ou gasolina vendidos nos Estados Unidos e a pontuação deles no âmbito da economia verde (emissão de gases de efeito estufa, poluição do ar etc.)
# 
# Usando a biblioteca _Pandas_:
# 
# 1. Leia a planilha em um _DataFrame.
# 
# 2. Identifique todos os modelos que são movidos a gasolina/eletricidade.
# 
# 3. Exporte um arquivo chamado `gas-elet.csv` contendo apenas 4 colunas com as seguintes informações acerca dos modelos encontrados no item 2: 
# 
# - _Model_
# - _Fuel_
# - _Air Pollution Score_
# - _Greenhouse Gas Score_

# In[48]:


# ler
df = pd.read_excel('METCOMP/data/smart-vehicle-epa-2020.xlsx')

# reduzir dataframe
df2 = df[['Model','Fuel','Air Pollution Score','Greenhouse Gas Score']]

# localiza indices de gas/eletricos
ids = np.where(df2['Fuel'].str.find('Gasoline/Electricity').array == 0)

df2.iloc[ids].to_csv('gas-ele.csv',index=False)

