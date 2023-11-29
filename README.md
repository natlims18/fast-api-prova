<div align=center>

# fast-api-prova

</div>


## Como Rodar?

### Iniciando o Backend

No diretório raiz do projeto crie um novo ambiente virtual do Python e entre nele para que seja possível ter total controle sobre as bibliotecas do Python que serão instaladas para a utilização deste projeto.

```bash
python -m venv .venv
```

```bash
source .venv/bin/activate
```

Também é um boa atualizar o PIP (gerenciador de pacotes do Python para a versão mais recente) utilizando o seguinte comando

```bash
pip install --upgrade pip
```

<hr>

Agora que você já se encontra no ambiente virtual do Python, caracterizado pela palavra `(.venv)` no início da linha do terminal instale todas as bibliotecas necessárias com o comando abaixo:

```bash
pip install -r requirements.txt
```

Com tudo devidamente instalado e configurado basta executar o servidor do FastAPI através do `uvicorn`

```bash
uvicorn ite.main:app --reload
```

<br />

### Iniciando o Frontend

Abra um novo terminal (mantendo backend rodando no terminal anterior) e rode os comandos abaixo

```bash
npm install
```

```bash
npm start
```