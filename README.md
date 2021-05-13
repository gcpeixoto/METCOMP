# METCOMP

## Como usar os .ipynb com RISE Slideshow

- Este curso usa a extensão RISE com `chalkboard` e `pencil` no Jupyter Notebook. 
- É adequado criar um ambiente `conda` separado. 

### Workflow

- Criar novo ambiente `lecture` a partir de YAML.

`conda create -f environment.yml` 

- Ativar ambiente

`conda activate lecture`

- Invocar Jupyter

`jupyter-notebook`

- Abrir notebooks com RISE (botão)

- Desativar Jupyter e ambiente

`conda deactivate`
