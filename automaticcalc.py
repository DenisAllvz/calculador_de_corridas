def collect_deliveries_per_day(days_worked):
    deliveries_per_day = []
    for dia in range (1, days_worked + 1):
        print(f"\n {dia}:")
        deliveries =  input("Distância em cada entrega, separada por espaço: ")
        deliveries = list(map(float,deliveries.split()))
        deliveries_per_day.append(deliveries)
    return deliveries_per_day


def calculate_total_payment(deliveries_day, rate=1.35,daily=15.0):
    total_payment=0
    for distance in deliveries_day:
        total_km = sum(distance)
        daily_payment = (total_km * rate)+daily
        total_payment+=daily_payment
    return total_payment

days_worked = int(input("Dias trabalhados: "))

days = collect_deliveries_per_day(days_worked)

amount_to_pay = calculate_total_payment(days)

print(f"O valor total a ser pago é: R$ {amount_to_pay:.2f}")
