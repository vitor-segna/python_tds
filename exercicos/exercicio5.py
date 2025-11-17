nome = input("Qual o seu nome? ")
sacola = int(input(f"{nome} você deseja comprar quantas camisas? "))
camisa = 12.5
total = sacola * camisa 

if sacola <= 5:
 total = total *0.97
else:
 if sacola <=10:
  total = total * 0.95
 else:
  total = total * 0.93

  print(f'Valor total da compra é de: {total:.2f}') 
 