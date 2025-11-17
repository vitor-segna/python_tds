horas = float(input("Quantas horas você assiste por semana a essa plataforma de streaming? "))
valor = float(input("Qual o valor mensal dessa assinatura? "))

horas = horas * 4 
custo = valor / horas


print(f"O custo por hora de entretenimento da plataforma de streaming é de: {custo}")