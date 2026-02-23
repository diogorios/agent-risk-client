
from fastapi import FastAPI
from .rules import avaliar_risco

app = FastAPI(
    title="Agente de Risco Financeiro",
    description="Avaliação de risco de clientes com base em contas a receber",
    version="1.0.0"
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/avaliar-risco-cliente")
def avaliar(payload: dict):
    resultado = avaliar_risco(payload)
    return resultado


# Explicação
# /health
# → endpoint simples para teste (Vercel, browser, monitoramento)

# /avaliar-risco-cliente
# → endpoint que o Delphi vai chamar

# payload: dict
# → recebe exatamente o JSON que você montou no ERP
