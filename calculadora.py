def soma(num1, num2):
	soma = num1 + num2
	return soma

def subtracao(num1, num2):
	subtracao = num1 - num2
	return subtracao

def multiplicacao(num1, num2):
	multiplicacao = num1 * num2
	return multiplicacao

def divisao(num1, num2):
	divisao = num1 / num2
	return divisao

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

operacao = int(input("Digite a operação que deseja realizar: (1) Soma, (2) Subtração, (3) Multiplicação ou (4) Divisão.\n"))

if(operacao == 1):
	resultado = soma(num1, num2)
elif(operacao == 2):
	resultado = subtracao(num1, num2)
elif(operacao == 3):
	resultado = multiplicacao(num1, num2)
elif(operacao == 4):
	resultado = divisao(num1, num2)

print(resultado)
