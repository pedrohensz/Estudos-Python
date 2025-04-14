#for
texto = "python"
vogais = "AEIOU"


for letra in texto:
    if letra.upper() in vogais:
        print(letra, end="")

print()
"""Observei durante os estudos que a estutura for percorre apenas strings
em caso de números inteiros o correto é utilizar o range()
"""

#for else
texto = "python"
vogais = "AEIOU"


for letra in texto:
    if letra.upper() in vogais:
        print(letra, end="")
else:
    print()

    """Adiciona o print que estava "solto" ao final do laço"""
    
#range
list (range(4)) #nesse caso deve ser "forçado" como lista para que os valores sejam exibidos como tal
for numero in range (11):
    print (numero, end=" ")

#tabuada do 5 
for numero in (range 0,50,5):
    print (numero, end=" ")

    """Acima podemos ver que 
    o range recebe 3 argumentos sendo eles
    start: o número que irá se iniciar a sequência
    stop: o último número da sequência
    step: basicamente de "quantos em quantos" números será contado.
    """


#while 
opcao = -1 
while opcao != 0:
        try:
            opcao = int(input("\n [1]Sacar\n [2]Extrato\n [0]Sair\n: "))
            if opcao == 1:
                print("Sacando...")
            elif opcao == 2:
                print ("Exibindo extrato...")
        except ValueError:
            print ("Valor inválido")
else:
    print("Muito obrigado por utilizar nosso sistema até logo ")

    """
        A estrutura abaixo usa o "while", que significa "enquanto". 
        Ela diz que, enquanto o valor de 'opcao' for diferente de 0, 
        o código continuará sendo executado.
    """

#break
while True:
    numero = int(input("Insira um número de 0 a 100: "))

    if numero == 10:
         break
    print(numero)
    
    """
        A estrutura abaixo usa o "break", que significa "parar". 
        Ela diz que, quando o valor de 'numero' for igual a 0, 
        o código deverá ser encerrado.
    """