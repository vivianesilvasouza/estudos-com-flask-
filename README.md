# Como Executar o Projeto

Siga os passos abaixo para configurar e rodar o projeto:

1. **Instalar as Dependências**

Execute o seguinte comando para instalar as dependências listadas no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

2. **Configurar variaveis de ambiente**


Execute o comando abaixo para criar o arquivo .env

```bash
cp .env-example .env
# No macOS ou Linux
```

ou

```bash
copy .env-example .env
# No Windows
```

Criado o arquivo altere as keys indicadas dentro do arquivo .env criado

3. **Criar e Ativar o Ambiente Virtual**

Antes de rodar o projeto, é recomendável criar e ativar um ambiente virtual para isolar as dependências.
Siga as instruções de acordo com o seu sistema operacional:

**Windows**

```bash
Set-ExecutionPolicy AllSigned
python -m pip install virtualenv
python -m venv venv
.\venv\Scripts\activate
```

**Caso ocorra um erro relacionado à execução de scripts no Windows, siga o passo abaixo:**

```bash
Set-ExecutionPolicy Unrestricted
```

**Linux**

```bash
source venv/bin/activate
```

### Comando para Rodar o Projeto

2. Agora você está pronto para rodar o projeto. Use o comando apropriado de acordo com o seu sistema operacional:

**Windows**

```bash
python run_ssl.py
```

**Linux**

```bash
python3 run_ssl.py
```
