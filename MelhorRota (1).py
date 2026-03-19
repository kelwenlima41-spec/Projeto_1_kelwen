import heapq

def dijkstra(grafo, partida, destino):
    fila_prioridade = [(0, partida, [])]
    visitados = set()

    while fila_prioridade:
        (custo_total, cidade_atual, caminho) = heapq.heappop(fila_prioridade)

        if cidade_atual in visitados:
            continue

        caminho = caminho + [cidade_atual]
        visitados.add(cidade_atual)

        if cidade_atual == destino:
            return caminho, custo_total

        for vizinho, peso in grafo.get(cidade_atual, {}).items():
            if vizinho not in visitados:
                heapq.heappush(fila_prioridade, (custo_total + peso, vizinho, caminho))

    return None, float('inf')

mapa_cidades = {
    "A": {"B": 7, "C": 9},
    "B": {"A": 7, "D": 10},
    "C": {"A": 9, "D": 2, "E": 1},
    "D": {"B": 10, "C": 2, "E": 3},
    "E": {"C": 1, "D": 3}
}

print("Planejador de Rotas (Dijkstra Manual)")
print("Cidades disponíveis:", ", ".join(mapa_cidades.keys()))

cidade_partida = input("\nCidade de partida: ").strip().upper()
cidade_destino = input("Cidade de destino: ").strip().upper()

if cidade_partida not in mapa_cidades or cidade_destino not in mapa_cidades:
    print("\nErro: Uma ou ambas as cidades não existem no mapa.")
else:
    rota, distancia = dijkstra(mapa_cidades, cidade_partida, cidade_destino)
    
    if rota:
        print("\nResultado")
        print(f"Melhor rota: {' -> '.join(rota)}")
        print(f"Distância total: {distancia}")
    else:
        print("\nNão foi possível encontrar um caminho entre as cidades.")