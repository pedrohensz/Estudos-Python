<<<<<<< HEAD
saldo = "1000"
limite = "1000"



#Operador Is
print (saldo is limite)
"""Testa se as variáveis apontam para o mesmo objeto"""


print(saldo is not limite)
"""Testa se as variáveis não apontam para o mesmo objeto"""

"""
A diferença entre == e "is" é que:
== : compara valores

is : compara identidade do objeto
"""
""""""

x = [1, 2]
y = [1, 2]

print(x == y)  # True → os valores são iguais
print(x is y)  # False → são objetos diferentes na memória

print(id(saldo))  
print(id(limite))

"""
Em Python, para valores imutáveis e pequenos,
 como inteiros e strings curtas, o interpretador costuma reaproveitar os objetos na memória para otimizar desempenho. 
Isso é chamado de interning.
Se duas variáveis compartilham o mesmo objeto (por causa do interning), o id() delas será igual.
=======
saldo = "1000"
limite = "1000"



#Operador Is
print (saldo is limite)
"""Testa se as variáveis apontam para o mesmo objeto"""


print(saldo is not limite)
"""Testa se as variáveis não apontam para o mesmo objeto"""

"""
A diferença entre == e "is" é que:
== : compara valores

is : compara identidade do objeto
"""
""""""

x = [1, 2]
y = [1, 2]

print(x == y)  # True → os valores são iguais
print(x is y)  # False → são objetos diferentes na memória

print(id(saldo))  
print(id(limite))

"""
Em Python, para valores imutáveis e pequenos,
 como inteiros e strings curtas, o interpretador costuma reaproveitar os objetos na memória para otimizar desempenho. 
Isso é chamado de interning.
Se duas variáveis compartilham o mesmo objeto (por causa do interning), o id() delas será igual.
>>>>>>> 98a0e5b260482fe0647b6f29cf2d0cd72e9bb07e
"""