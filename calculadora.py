calculadora = input("Você necessita de qual tipo de calculadora?\n1: Normal (+,-,*,/)\n2: Porcentagem (%)\nEscreva aqui o número da calculadora: ")

if calculadora == "1":
    conta = int(input("(+,-,*,/) Digite uma conta e você terá seu resultado! "))
    resultado = eval(conta)
    print("O resultado de sua conta é", resultado)

elif calculadora == "2":
    primeiro_numero = int(input("Digite um número, ele vai ser a porcentagem de outro escolhido por você mais a frente "))
    segundo_numero = int(input("O número anterior é a porcentagem de que número? "))
    segundo_numero_dividido = segundo_numero / 100
    resultado = primeiro_numero * segundo_numero_dividido
    print("O resultado de sua conta é", resultado)

else:
    print("O número fornecido não foi entendido, você só pode colocar 1 ou 2 como resposta da primeira pergunta, o número 1 significa que você quer fazer uma conta de adição, subtração, divisão ou miltiplicação, o número 2 significa que você quer fazer uma conta de porcentagem, reinicie o código e tente de novo")
