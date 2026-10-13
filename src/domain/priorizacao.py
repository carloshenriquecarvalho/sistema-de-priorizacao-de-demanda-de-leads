# - Critério: Vendedor só recebe lead se estiver com a etapa NOVO LEAD vazia
# - Critério Peso 2: Quantidade de Leads Ativos
# - Critério Peso 4: Taxa de Conversão de Leads em Venda

def calcular_priorizacao():

    # Inicializa lista para retenção dos consultores no processo corrente do programa
    consultores = []
    while True:

        nome_consultor = input("Digite o nome do Consultor (Ou sair para terminar): ").strip()
        if nome_consultor == 'sair':
            break

        # Critério 1: Vendedor só recebe lead se estiver com a etapa NOVO LEAD vazia
        criterio_1 = verifica_criterio_etapa_novo_lead_vazia()

        if not criterio_1:
            print(f"O consultor {nome_consultor} não está elegível para receber leads. Vamos para o próximo.")
            continue

        # Critério 2: Quantidade de Leads Ativos
        quantidade_leads_ativos = verifica_criterio_quantidade_de_leads()

        # Critério 3: Taxa de Conversão de Leads em Venda
        taxa_conversao = verifica_criterio_taxa_de_conversao(nome_consultor)

        pontos_prioritários = quantidade_leads_ativos + taxa_conversao

        # Adiciona o novo consultor à list  
        consultores.append({
            "nome": nome_consultor,
            "etapa_novo_lead_vazia": criterio_1,
            "quantidade_leads_ativos_peso_2": quantidade_leads_ativos,
            "taxa_conversao_peso_4": taxa_conversao,
            "prioridade": pontos_prioritários
        })

    return consultores

def verifica_criterio_etapa_novo_lead_vazia():
    etapa_novo_lead_vazia = input("A etapa de novos leads está vazia? ").strip().lower()
    
    etapa_novo_lead_vazia = True if etapa_novo_lead_vazia.startswith('s') else False
    return etapa_novo_lead_vazia

def verifica_criterio_quantidade_de_leads():
    quantidade_leads_ativos = int(input("Digite quantos leads ele tem no total: "))

    quantidade_leads_ativos *= 2
    return quantidade_leads_ativos

def verifica_criterio_taxa_de_conversao(nome_consultor: str):
    taxa = float(input(f"Digite qual a taxa de conversão do {nome_consultor}: "))

    taxa = taxa / 100 * 4

    return taxa

def metodo_listagem(e):
    return e["prioridade"]

if __name__ == '__main__':
    lista = calcular_priorizacao()
    lista.sort(key=metodo_listagem)

    for i in lista:
        print(i['nome'], i['prioridade'])