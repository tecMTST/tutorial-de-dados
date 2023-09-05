# Tutoriais de análise de dados

Uma série de tutoriais sobre análise de dados, para você aprender com a mão na massa e com dados reais! 👊🏽

Todos os tutoriais são
[notebooks Jupyter](https://site.alura.com.br/artigos/conhecendo-o-jupyter-notebook) de Python.


## Estrutura deste repositório

    .
    ├── 06_expectativa-de-vida    <- Análise (tutorial) sobre um tema específico.
    :
    ├── 80_material-complementar  <- Tutoriais sobre assuntos auxiliares.
    ├── 99_incompletos            <- Tutoriais em desenvolvimento.
    ├── 00_indice.ipynb           <- Lista de tutoriais por assunto e técnica.
    ├── LICENSE                   <- Licença para uso deste repositório.
    ├── README.md                 <- Informações sobre o projeto.
    └── requirements.txt          <- Pacotes de Python necessários.

Os tutoriais estão organizados por assunto analisado, em pastas que começam com um número. Com exceção
dos materiais complementares e dos tutoriais em desenvolvimento, esses números indicam a ordem aproximada dos tutoriais,
em termos de sua complexidade.

Para escolher um tutorial com base no assunto tratado, na técnica de análise de dados abordada
ou no método de Python utilizado, siga a lista no arquivo [00_indice.ipynb](00_indice.ipynb). Esse notebook também dá
uma sugestão de ordem didática para os notebooks.


## Por que escolhemos Notebooks de Python?

* Seu uso é comum entre analistas e cientistas de dados.
* Usar múltiplos aplicativos e/ou linguagens numa mesma análise a torna mais bagunçada e menos reprodutível. É melhor manter tudo num mesmo ambiente.
* Python é uma linguagem bastante flexível que pode ser usada para realizar qualquer coisa: 
  raspagem de dados, automação, processamento e limpeza de dados, análises estatísticas, gráficos e visualizações, modelos de aprendizado de máquina, entre outros.
* Python e Jupyter Notebooks são ferramentas gratuitas feitas em código aberto; qualquer pessoa pode utilizá-los sem custo ou restrições.


## Como usar este material

📝 Tente reproduzir os códigos e a lógica de análise você mesmo. Isso vai lhe ajudar a entender e memorizar o assunto. 

🔧 Modifique o código e explore novas possibilidades de parâmetros, análises, etc.

💡 Se descobrir algo novo sobre os dados ou sobre a análise, comente e contribua!

📣 Se gostar do material, divulge para mais pessoas! 


## Requisitos

🐍 Assumimos que você já saiba o básico de Python. Caso não saiba, veja nosso 
[notebook de Python básico](80_material-complementar/00_tutorial-python.ipynb) 
ou faça o curso do [Núcleo de Tecnologia](http://nucleodetecnologia.com.br)! 🚩

💻 Você tem 3 opções para abrir e executar os notebooks: localmente, no
[Jupyter Lite](https://jupyter.org/try-jupyter/lab/) ou no
[Google Colab](https://colab.research.google.com/).


### Uso local (no seu computador)

#### Windows

_Em construção_

#### Linux

Você precisa ter os programas
[git](https://site.alura.com.br/artigos/o-que-e-git-github),
python 3, [pip](https://pt.wikipedia.org/wiki/Pip_(gerenciador_de_pacotes)) e
[venv](https://docs.python.org/pt-br/3/library/venv.html). Se não tiver, instale-os.
Em seguida, siga as instruções abaixo:


1. Abra o terminal.
2. Use o comando `cd` para entrar no diretório onde gostaria de copiar o tutorial.
3. Clone o tutorial com o comando:

```
    git clone https://github.com/tecMTST/tutorial-de-dados.git
```

4. Acesse o diretório do tutorial:

```
    cd tutorial-de-dados
```

5. Crie um ambiente virtual e ative-o:

```
    python3 -m venv env
    source env/bin/activate
```

6. Instale os pacotes de Python necessários:

```
    pip install -r requirements.txt
```

7. Execute o jupyter lab:

```
    jupyter lab &
```

### Jupyter Lite

_Em construção_

### Google Colab

_Em construção_


<center>
<img src="https://nucleodetecnologia.com.br/assets/img/novo-logo-tecnologia.svg?bl=tutorial-readme" width="200">
</center>
