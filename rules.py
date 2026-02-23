
def avaliar_risco(dados: dict) -> dict:
    score = 0
    motivos = []

    resumo = dados["contas_receber"]["resumo_historico"]

    # Regra 1: média de atraso
    media_atraso = resumo.get("media_dias_atraso", 0) or 0
    if media_atraso > 10:
        score += 30
        motivos.append(f"Média de atraso elevada ({media_atraso:.1f} dias)")

    # Regra 2: títulos atrasados
    if resumo.get("titulos_atrasados", 0) > 2:
        score += 20
        motivos.append("Quantidade relevante de títulos em atraso")

    # Regra 3: valor em aberto proporcional
    valor_aberto = resumo.get("valor_em_aberto", 0)
    valor_total = resumo.get("valor_total_faturado", 1)

    if valor_total > 0 and (valor_aberto / valor_total) > 0.3:
        score += 25
        motivos.append("Valor em aberto acima de 30% do faturamento")

    # Classificação final
    if score >= 60:
        nivel = "ALTO"
        acao = [
            "Bloquear novos créditos",
            "Acionar cobrança imediata"
        ]
    elif score >= 30:
        nivel = "MEDIO"
        acao = [
            "Permitir vendas com alerta",
            "Acompanhar cobrança"
        ]
    else:
        nivel = "BAIXO"
        acao = [
            "Cliente liberado",
            "Monitoramento padrão"
        ]

    return {
        "nivel_risco": nivel,
        "score": score,
        "motivos": motivos,
        "acao_sugerida": acao
    }
