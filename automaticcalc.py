def calcular_pagamento(dias, entregas_por_dia, taxa=1.35,diaria=15.0):
    pagamento_total=0
    for distancia in entregas_por_dia:
        total_km = sum(distancia)
        pagamento_diario = (total_km * taxa)+diaria
        pagamento_total+=pagamento_diario
    return pagamento_total
dias_trabalhados = int(input("Dias trabalhados: "))

entregas_por_dia = []

for dia in range (1, dias_trabalhados + 1):
    print(f"\n {dia}:")
    entregas =  input("Distância em cada entrega, separada por espaço: ")
    entregas = list(map(float,entregas.split()))
    entregas_por_dia.append(entregas)

valor_a_pagar = calcular_pagamento(dias_trabalhados, entregas_por_dia)

print(f"O valor total a ser pago é: R$ {valor_a_pagar:.2f}")