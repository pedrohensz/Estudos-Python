<<<<<<< HEAD
#Operadores de associação
"""In: Retorna True se o valor estiver presente na sequência"""
"""Not in: Retorna False se o valor estiver presente na sequência ou True em sua ausência"""

palavra = "mamão"

print ("a" in palavra)

print ("a" not in palavra)

cores = ('vermelho', 'azul', 'verde')

print  ("azul" in cores)

"""Operadores de assoiciação com dicionário"""
"""Caso você tente procurar um valor em um dicionário 
ele sempre irá prcurar o valor nas chaves como o exemplo abaixo:
"""
aluno = {
    "nome": "Pedro",
    "idade": 22,
    "curso": "Engenharia"
}

print ("Pedro" in aluno )
# Retorna False, porque "Pedro" é um valor, não uma chave.

#Caso eu queria procuar o valor de uma chave devo executar 
=======
#Operadores de associação
"""In: Retorna True se o valor estiver presente na sequência"""
"""Not in: Retorna False se o valor estiver presente na sequência ou True em sua ausência"""

palavra = "mamão"

print ("a" in palavra)

print ("a" not in palavra)

cores = ('vermelho', 'azul', 'verde')

print  ("azul" in cores)

"""Operadores de assoiciação com dicionário"""
"""Caso você tente procurar um valor em um dicionário 
ele sempre irá prcurar o valor nas chaves como o exemplo abaixo:
"""
aluno = {
    "nome": "Pedro",
    "idade": 22,
    "curso": "Engenharia"
}

print ("Pedro" in aluno )
# Retorna False, porque "Pedro" é um valor, não uma chave.

#Caso eu queria procuar o valor de uma chave devo executar 
>>>>>>> 98a0e5b260482fe0647b6f29cf2d0cd72e9bb07e
print ("Pedro" in aluno.values() )