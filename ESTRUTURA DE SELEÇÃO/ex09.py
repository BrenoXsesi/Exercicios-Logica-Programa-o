valor_compra = float(input("Digite o valor da compra: "))

if valor_compra > 100:
    valor_compra = valor_compra - (valor_compra * 0.1)
    print(f"O valor da compra com o desconto é: {valor_compra}")
else:
    print(f"Sem descontos, valor da compra: {valor_compra}")