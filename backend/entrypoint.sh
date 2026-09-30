#!/bin/sh
set -e

echo "Aplicando migracoes do banco..."
alembic upgrade head

echo "Criando usuario administrador inicial, se necessario..."
python -m app.seed

echo "Iniciando aplicacao na porta ${PORT:-10000}..."
exec uvicorn app.main:app --host 0.0.0.0 --port "${PORT:-10000}"
