import random

numero_secreto = random.randint(1, 100)
palpite = 0

print(" Adivinhe o numero secreto ")


while palpite != numero_secreto:
    palpite = int(input("Digite seu palpite (1 a 100): "))

    if palpite < numero_secreto:
        print("O número secreto é MAIOR!\n")
    elif palpite > numero_secreto:
        print("O número secreto é MENOR!\n")

    else:
        print("Parabéns! Você acertou o número!")