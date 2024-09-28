import json

with open('questao_faturamento\dados.json') as file:
    faturamento_diario = json.load(file)

faturamento_valido = [dia['valor'] for dia in faturamento_diario if dia['valor'] > 0]

menor_valor = min(faturamento_valido)
maior_valor = max(faturamento_valido)
media_mensal = sum(faturamento_valido) / len(faturamento_valido)

dias_acima_da_media = len([dia['valor'] for dia in faturamento_diario if dia['valor'] > media_mensal])

print(f"Menor valor de faturamento: {menor_valor}")
print(f"Maior valor de faturamento: {maior_valor}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
