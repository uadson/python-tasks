##### Automatizando planilhas

Um recurso interessante na sua utilização é a automatização de planilhas excel através do python e a biblioteca openpyxl

##### Instalação

Para instalação da biblioteca, como boas práticas, é necessário a criação de um ambiente virtual para que não haja conflito entre outras bibliotecas.

Para isso utilize o comando:

    python -m venv venv

    ou

    py -m venv venv

onde:

    a instrução -m venv significa que o módulo venv da biblioteca nativa do python, virtualenv está sendo chamada, e o outro parâmetro venv é o nome que será dado ao ambiente virtual, podendo ser qualquer outro nome.


Após a criação do ambiente virtual é preciso ativá-lo para então proceder com a instalação.

No windows:

    comando:
    .\venv\Scripts\activate

No linux:

    comando:
    source /venv/bin/activate


Após a ativação do ambiente, a instalação:

    pip install openpyxl
