#Interpolação de strings
#f-strings
nome = "Pedro"
idade = 22
print(f"Meu nome é {nome} e tenho {idade} anos.")
#Saída: Meu nome é Pedro e tenho 22 anos.
#Pode se colocar expressões direto dentro:
print(f"Daqui 5 anos. Pedro terá {idade+ 5} anos.")

#str.format()
print("Meu nome é {} e tenho {} anos.".format(nome, idade))
# Ou com índices:
print("Meu nome é {0} e tenho {1} anos.".format(nome, idade))
# Ou com nomes:
print("Meu nome é {n} e tenho {i} anos.".format(n=nome, i=idade ))


#Operador % (estilo C)
print("Meu nome é %s e tenho %d anos."% (nome, idade))
# %s para string, %d para int, %f para float etc.