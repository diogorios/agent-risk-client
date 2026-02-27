
def avaliar_risco(dados: dict) -> dict:
    score = 0
    motivos = []

    resumo = dados["contas_receber"]["resumo_historico"]

    cliente = dados.get("cliente", {})
    nome = cliente.get("nome", "")

    # Regra 1: média de atraso
    media_atraso = resumo.get("media_dias_atraso", 0) or 0
    
    if media_atraso >= 10:
        score += 30
        motivos.append(f"Média de atraso elevada ({media_atraso:.1f} dias)")
    elif media_atraso >= 5:
        score += 15
        motivos.append(f"Média de atraso frequente ({media_atraso:.1f} dias)")

    # Regra 2: títulos atrasados
    titulos_atrasados = resumo.get("titulos_atrasados", 0)

    if titulos_atrasados >= 2:
        score += 20
        motivos.append(f"{titulos_atrasados} títulos em atraso")
    elif titulos_atrasados == 1:
        score += 10
        motivos.append("Cliente possui 1 título em atraso")

    # Regra 3: valor em aberto proporcional
    valor_aberto = resumo.get("valor_em_aberto", 0)
    valor_total = resumo.get("valor_total_faturado", 1)

    if valor_total > 0 and (valor_aberto / valor_total) > 0.3:
        score += 25
        motivos.append("Valor em aberto acima de 30% do faturamento")

    # Classificação final
    if score >= 60:
        nivel = "ALTO"

    elif score >= 20:
        nivel = "MEDIO"

    else:
        nivel = "BAIXO"
    
    # Definir ações separadamente
    if score >= 60:
        acao = [
            "Bloquear novos créditos",
            "Acionar cobrança imediata"
        ]

    elif score >= 30:
        acao = [
            "Permitir vendas com alerta",
            "Acompanhar cobrança"
        ]

    elif score >= 20:
        acao = [
            "Permitir vendas com limite reduzido",
            "Acompanhar pagamento atual"
        ]

    else:
        acao = [
            "Cliente liberado",
            "Monitoramento padrão"
        ]

    return {
        "nivel_risco": nivel,
        "score": score,
        "motivos": motivos,
        "acao_sugerida": acao,
        "nome_cliente_v3": nome
    }
