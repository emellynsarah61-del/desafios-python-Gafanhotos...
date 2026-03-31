velocidade = 90
limite = 80
preco_por_km = 7

# 1. Quanto passou do limite?
km_excedidos = velocidade - limite

if km_excedidos > 0:
    # 2. Como calcular o total?
    valor_multa = km_excedidos * preco_por_km

    print(f"Passou {km_excedidos} km/h do limite.")
    print(f"O valor da multa é: R$ {valor_multa:.2f}")
else:
    print("Dentro do limite. Sem multa!")





