# Estoque 6.2.0 - preparado para Render

Aplicacao completa com:

- Frontend HTML, CSS e JavaScript
- Backend FastAPI
- PostgreSQL
- Docker
- Alembic

No Render, o frontend e o backend executam no mesmo Web Service. O PostgreSQL e criado como banco gerenciado no mesmo Blueprint.

## Teste local com Docker Compose

Crie o arquivo `.env` com base no `.env.example` e execute:

```bash
docker compose up -d --build
```

Acessos locais:

- Site: http://localhost:4200
- API: http://localhost:8000/docs

## Deploy no Render

1. Nao envie o arquivo `.env` ao GitHub.
2. Envie todos os arquivos deste projeto ao repositorio.
3. No Render, escolha New > Blueprint.
4. Conecte o repositorio.
5. O Render detectara o `render.yaml` e criara:
   - `estoque-app`, Web Service Docker
   - `estoque-db`, PostgreSQL
6. Informe `ADMIN_EMAIL` e `ADMIN_PASSWORD` quando solicitado.
7. Depois do deploy, abra a URL `onrender.com` do servico.

## Variaveis obrigatorias no Render

- `DATABASE_URL`: vinculada automaticamente ao PostgreSQL pelo Blueprint
- `SECRET_KEY`: gerada automaticamente
- `ADMIN_EMAIL`: informada durante a criacao
- `ADMIN_PASSWORD`: informada durante a criacao
- `ADMIN_NAME`: Administrador

## Dominio proprio

No servico `estoque-app`, abra Settings > Custom Domains, adicione seu dominio ou subdominio e crie no DNS da HostGator o registro exibido pelo Render.
