# API de Gerenciamento com NGINX

## 1. Descrição do projeto

Este projeto consiste em uma API REST desenvolvida com Python e FastAPI, utilizando SQLite como banco de dados.

Nesta atividade, foi implementado o NGINX como **Reverse Proxy (proxy reverso)**, responsável por receber as requisições HTTP e encaminhá-las para a aplicação FastAPI, executada pelo servidor Uvicorn.

A infraestrutura utiliza Docker e Docker Compose para facilitar a configuração e execução dos serviços.

## 2. Tecnologias utilizadas

- Python 3.12
- FastAPI
- Uvicorn
- SQLite
- NGINX
- Docker
- Docker Compose

## 3. Estrutura dos arquivos adicionados

```text
ApitUniBHSD202602/
├── nginx/
│   └── nginx.conf
├── data/
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── database.py
├── main.py
├── models.py
├── services.py
└── README.md
```

## 4. Configuração do NGINX

Foi criado o arquivo `nginx/nginx.conf` com a configuração do servidor:

```nginx
events {
    worker_connections 1024;
}

http {
    server {
        listen 80;

        location / {
            proxy_pass http://api:8000;

            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
    }
}
```

O NGINX recebe as requisições na porta 80 e as encaminha para o serviço `api`, na porta 8000, dentro da rede Docker.

## 5. Como executar o projeto

### Pré-requisitos

- Docker Desktop instalado e em execução.
- Git instalado.

### Passo 1 – Clonar o repositório

```bash
git clone https://github.com/mateusdca/ApitUniBHSD202602.git
```

### Passo 2 – Acessar a pasta

```bash
cd ApitUniBHSD202602
```

### Passo 3 – Selecionar a branch da atividade

```bash
git checkout atividade-nginx
```

### Passo 4 – Construir e iniciar os containers

```bash
docker compose up --build -d
```

Esse comando constrói a imagem da API e inicia os containers da aplicação e do NGINX em segundo plano.

### Passo 5 – Verificar os containers

```bash
docker compose ps
```

Os serviços da API e do NGINX devem aparecer em execução.

## 6. Como acessar a aplicação

Após iniciar os containers, a aplicação estará disponível pelos seguintes endereços:

| Recurso | Endereço |
|---|---|
| API | http://localhost |
| Documentação Swagger | http://localhost/docs |
| Especificação OpenAPI | http://localhost/openapi.json |

As requisições são recebidas pelo NGINX e encaminhadas para a API FastAPI.

## 7. Testes realizados

Foram realizados testes utilizando o PowerShell:

**Teste da documentação Swagger:**

```powershell
Invoke-WebRequest http://localhost/docs -UseBasicParsing
```

Resultado: `200 OK`.

**Teste da especificação OpenAPI:**

```powershell
Invoke-WebRequest http://localhost/openapi.json -UseBasicParsing
```

Resultado: `200 OK`.

Os resultados confirmaram que o NGINX está recebendo e encaminhando corretamente as requisições para a aplicação.

## 8. Gerenciamento dos containers

**Visualizar os containers:**

```bash
docker compose ps
```

**Visualizar os logs:**

```bash
docker compose logs
```

**Parar os serviços:**

```bash
docker compose down
```

**Reiniciar e reconstruir a aplicação:**

```bash
docker compose up --build -d
```

## 9. Conclusão

A implementação permitiu integrar o NGINX à API desenvolvida com FastAPI, utilizando Docker e Docker Compose.

Com o uso do NGINX como proxy reverso, as requisições passam a ser recebidas pela porta 80 e encaminhadas internamente para a aplicação na porta 8000.

Os testes realizados retornaram o status HTTP 200 OK, comprovando o funcionamento da configuração.

Dessa forma, a atividade demonstrou na prática a utilização do NGINX para intermediar as requisições entre os clientes e uma aplicação web.
