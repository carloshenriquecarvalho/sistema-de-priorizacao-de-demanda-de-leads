# - Critério: Vendedor só recebe lead se estiver com a etapa NOVO LEAD vazia
# - Critério Peso 2: Quantidade de Leads Ativos
# - Critério Peso 4: Taxa de Conversão de Leads em Venda

def calcular_pontuacao(
        nome_consultor: str,
        etapa_novo_lead_vazia: bool,
        quantidade_leads_ativos: int,
        taxa_conversao: float
    ) -> dict:
    # Calcula a prioridade de um consultor elegível
    if not etapa_novo_lead_vazia:
        return {
            "nome": nome_consultor,
            "elegivel": False,
            "prioridade": None,
        }

    pontos_leads = quantidade_leads_ativos * 2
    pontos_conversao = taxa_conversao * 4

    return {
        "nome": nome_consultor,
        "etapa_novo_lead_vazia": etapa_novo_lead_vazia,
        "quantidade_leads_ativos_peso_2": pontos_leads,
        "taxa_conversao_peso_4": pontos_conversao,
        "prioridade": pontos_leads + pontos_conversao,
        "elegivel": True,
    }

if __name__ == '__main__':
    calcular_pontuacao()