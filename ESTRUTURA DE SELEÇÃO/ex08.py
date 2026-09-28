idade = int(input("DIgite sua idade: "))

if idade >= 0 and idade <= 12:
    print("Você é criança")

elif idade >= 13 and idade <= 17:
    print("Você é adolescente")

else:
    print("Você é adulto")