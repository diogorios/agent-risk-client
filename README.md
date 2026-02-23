
# Agente de Risco Financeiro

API para avaliação de risco de clientes com base em histórico de contas a receber.

## Endpoint principal

POST `/avaliar-risco-cliente`

### Payload
JSON contendo dados do cliente, títulos em aberto e resumo histórico.

### Resposta
- nível de risco
- score
- motivos
- ação sugerida

## Tecnologias
- Python
- FastAPI
- Deploy via Vercel
