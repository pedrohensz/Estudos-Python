#Trabalhando com Tuplas em Python
# Tuplas são coleções ordenandas e imutáveis, usadas para armazenar múltiplos valores

#Criando tuplas
numeros = (1, 2, 3, 4) # Tupla de inteiros 
nomes = ("Ana", "João", "Maria") # Tupla de strings
mista = (1, "texto", True) # Tupla com diferentes tipos de dados

# Acessando elementos por indice (começa com 0)
print(nomes[0]) #Primeiro elemento: "Ana"
print(nomes[-1]) #Ultimo elemento: "Maria"

#Tuplas são imutáveis, não podemos alterar seus elementos após a criação.
#Isso significa que não podemos usar operações como .append() ou .remove().

# Fatiamento de tuplas (slicing)
print(nomes[1:3]) # Elementos do índice 1 até 2
print (nomes[:2]) # Do inicio até o indice 1 
print(nomes[::2]) # De 2 em 2, do início ao fim

# Verificando se um elemento está na tupla
if "João" in nomes:
    print("João está na lista") #Condicional baseada em presença

#Tupla com um único elemento 
tupla_unica = (5,) # Importante colocar a virgula para que o Python entenda como tupla

#Tuplas podem ser usadas como chaves de dicionários, já que são imutáveis.
dicionario = {(1, 2): "valor", (3, 4): "outro valor"}

#Funções utesi
print(len(nomes)) #retorna o número de elementos na tupla
print(min(numeros)) #retorna o menor valor da tupla
print(max(numeros)) #retorna o maior valor da tupla
print(sum(numeros)) # soma todos os valores da tupla

# Observação: Tuplas são imutáveis, ou seja, seus valores não podem ser alterados