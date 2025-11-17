nome =  input("Qual seu nome? ")
nota1 = float(input("Qual foi a sua nota na primeira prova? "))
nota2 = float(input("Qual foi a sua nota na segunda prova? "))
nota3 = float(input("Qual foi a sua nota na terceira prova?"))
nota4 = float(input("Qual foi a sua nota na quarta prova? "))

conta = nota1 + nota2 + nota3 + nota4
resultado = conta/4

print(f" {nome}, o resultado da média foi de: {resultado}")