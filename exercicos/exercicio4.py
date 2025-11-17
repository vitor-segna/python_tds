nome = input("Qual seu nome? ")
reais = float(input("Qual o valor que você possui em reais? "))
dolar = 5.32
euro =  6.16

conta1 = reais / dolar
conta2 = reais / euro

print(f"Olá {nome},  você teria {conta1} reais de dolar, e {conta2} em euro")
