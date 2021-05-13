#!/usr/bin/env python
# coding: utf-8

# # Ferramentas computacionais do curso
# 
# Neste curso, usaremos Python 3.x (onde x é um número de versão) como linguagem de programação. Por se tratar de uma linguagem interpretada, interagir com ela é mais fácil do que uma linguagem compilada. Um conjunto mínimo de recursos para Python funcionar é composto do _core_ da linguagem, um terminal de comandos e um editor de texto. Enquanto programadores experientes usam menos recursos visuais, para efeito didático, usaremos interfaces mais amigáveis e interativas comprovadas como bons ambientes de aprendizagem.  
# 
# ### _iPython_ e _Jupyter Notebook_ 
# 
# O [[iPython]](http://ipython.org) foi um projeto iniciado em 2001 para o desenvolvimento de um interpretador Python para melhorar a interatividade com a linguagem. Ele foi integrado como um _kernel_ (núcleo) no projeto [[Jupyter]](http://jupyter.org), desenvolvido em 2014, permitindo textos, códigos e elementos gráficos sejam integrados em cadernos interativos. _Jupyter notebooks_ são interfaces onde podemos executar códigos em diferentes linguagens desde que alteremos os _kernels_. A palavra _Jupyter_ é uma aglutinação das iniciais de _Julia_, _Python_ e _R_, que são as linguagens de programação mais usuais para ciência de dados.
# 
# ### *Anaconda* 
# 
# Em 2012, o projeto [[Anaconda]](https://www.anaconda.com) foi iniciado como objetivo de fornecer uma ferramenta completa para o trabalho com Python. Em 2020, já como uma empresa de ponta, ela tornou-se uma das pioneiras no fornecimento de plataformas individuais e empresariais para ciência de dados. Segundo a empresa, a [[Individual Edition]](https://www.anaconda.com/products/individual), que é a versão aberta para uso é a mais popular no mundo com mais de 20 milhões de usuários. Recomendamos que você siga as orientações de instalação desta versão. Uma vez instalada, basta lançar as ferramentas a partir do dashboard _Anaconda Navigator_.
# 
# ### *Jupyter Lab*
# 
# Uma ferramenta que melhorou a interatividade do Jupyter é o _Jupyter Lab_, que realiza um alto nível de integração. Este [[artigo]](https://blog.jupyter.org/jupyterlab-is-ready-for-users-5a6f039b8906) discute as características do Jupyter Lab, entre as quais vale citar o recurso de arrastar/soltar para reordenar células de cadernos e copiá-las entre cadernos.
# 
# ### *Binder* 
# 
# O projeto [[Binder]](https://mybinder.org) funciona como um servidor online baseada na tecnologia _Jupyter Hub_ para servir cadernos interativos online. Através do Binder, é possível executar códigos "na nuvem" sem a necessidade de instalações, porém as sessões são perdidas após o uso. 
# 
# ### *Google Colab* 
# 
# O [[Google Colab]](http://colab.research.google.com), uma redução de _Colaboratory_, é uma ferramenta que possui características mistas entre o _Jupyter notebook_ e o _Binder_, porém permite que o usuário use a infra-estrutura de computação de alto desempenho (GPUs e TPUS) da Google. A vantagem é que usuários de contas Google podem sincronizar arquivos diretamente com o Google Drive. 
# 
# ### *Live Code*
# 
# Ferramenta experimental que permite executar códigos instantaneamente a partir do livro interativo do curso disponibilizado online.
# 
# ### Módulos principais
# 
# Neste curso, o ecossistema de ferramentas torna-se pleno com a adição de alguns módulos que são considerados essenciais para a prática da ciência e análise de dados contemporânea: 
# 
# - *numpy* (*NUMeric PYthon*): o *numpy* serve para o trabalho de computação numérica, operando fundamentalmente com vetores, matrizes e ágebra linear.
# 
# - *pandas* (*Python for Data Analysis*): é a biblioteca para análise de dados de Python, que opera *dataframes* com eficiência.
# 
# - *sympy* (*SYMbolic PYthon*): é um módulo para trabalhar com matemática simbólica e cumpre o papel de um verdadeiro sistema algébrico computacional.
# 
# - *matplotlib*: voltado para plotagem e visualização de dados, foi um dos primeiros módulos Python para este fim.
# 
# - *scipy* (*SCIentific PYthon*): o *scipy* pode ser visto, na verdade, como um módulo mais amplo que integra os módulos anteriores. Em particular, ele é utilizado para cálculos de integração numérica, interpolação, otimização  e estatística.
# 
# - *seaborn*: é um módulo para visualização de dados baseado no *matplotlib*, porém com capacidades visuais melhores. 
# 
# A visualização de dados é um tema de suma importância para resultados da análise exploratória de dados em estatística. Um site recomendado para pesquisar as melhores ferramentas para análise de dados é o [[PyViz]](https://pyviz.org). 
