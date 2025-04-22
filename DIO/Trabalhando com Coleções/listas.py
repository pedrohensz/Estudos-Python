#Trabalhando com Listas
"""listas são coleçõe ordenadas e mutáveis, usadas para armazena
multiplos valores"""

#criando listas
frutas = ["maçã","banana", "laranja"] # Lista de strings
numeros = [1,2,3,4,5] #Lista de inteiros
mista = [1, "texto", True]

#Acessando elementos por índice (começa no 0)
print(frutas[0]) # Primeiro elemento: "maçã"
print(frutas[-1]) #último elemento: "laranja"

# Removendo elementos da lista
frutas.remove("banana") # Remove o primeiro valor "banana"
frutas.pop #Remove e retorna o último elemento
frutas.pop(1) #Remove e retorna o elemento na posição 1 

#iterando sobre os elementos da lista
for fruta in frutas:
    print(fruta) # Imrpime cada item da lista

#Verificando se um elemento está na lista
if "maçã" in frutas:
    print ("Tem maçã!") #Condicional baseada em presença


#criando listas com range()
lista_numero = list(range(10)) #Gera números de 0 a 9

#fatiamento de listas (slicing)
print(frutas[1:3]) # Elementos do índice 1 até 2
print(frutas[:2]) # Do início até o índice 1
print(frutas[::2]) # De 2 em 2, do início ao fim

# Funções úteis
print(len(frutas)) #Retorna o número de elementos
frutas.sort() #Oderna a lista (altera a original)
print(sorted(frutas)) #Retorna nova lista ordenada (sem alterar a originalk)
frutas.reverse() # Inverte a ordem da lista

# Observação: listas em Python são mutáveis, ou seja, podem ser modificadas após a criação.