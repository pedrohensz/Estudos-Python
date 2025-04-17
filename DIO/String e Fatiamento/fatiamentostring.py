#Fatiamento de strings
#string[inicio:passo]
#Componentes
"""
Inicio: Índice onde começa o fatiamento (inclusivo) significa que eu posso colocar a partir do primeiro índice
Fim: Índice onde termina o fatiamento (exclusivo) signigica que caso eu queria alcancer o índice 10 eu tenho que colocar o 11
passo: De quantos em quantos caracteres ele "anda".
"""
texto = "Pedro Henrique"

#Fatiar os 5 primeiros caracteres:
print(texto[0:5])

#Do índice 6 até o final
print(texto[6:]) #output: Henrique

#Últimos 3 caracteres:
print(texto[-3:]) #Output: que
"""
Nesse caso os índices negativos contam de trás para frente 
Ex:
P  e  d  r  o     H  e  n  r  i  q  u  e
0  1  2  3  4  5  6  7  8  9 10 11 12 13
Mas quando utilizamos o inicial negativo (como no exemplo)
P  e  d  r  o     H  e  n  r  i  q  u  e
-14-13-12-11-10 -9 -8 -7 -6 -5 -4 -3 -2 -1

"""
#Texto invertido
print(texto{::-1}) #Output: euqurneH ordeP
"""
quando colocamos o step = -1 o fatimento vai andar de trás para frente (-1,-2,-3 etc...)
Como não colocamos início nem fim (texto[::-1]), ele assume o padrão
início = final da string, fim = inicio da string, passo = -1 

"""
#caracteres de 2 em 2 
print(texto[::2]) #Output: PeoHnrq

#Últimos 3 caracteres:
print(texto[:-3]) #Output: Pedro Henri
"""
Aqui você está sendo dito: pegue do início até o índice -3 (exclusivo).
"""