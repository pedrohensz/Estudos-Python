#Len()
#Retorna o tamanho da string.
len("Pedro") #Retorna: 5

#Lower e Upper
#Convertem para minúsculas e maiúsculas.
"Pedro".lower() # 'pedro'
"Pedro".upper() # 'PEDRO'

#strip() / lstrip() / rstrip()
#Remove espaços em branco (ou caracteres específicos)
"    Olá     ".strip() # 'Olá'
"###Texto###".strip('#') # 'Texto'

#replace(old, new)
#Substitui partes da string
"Python é top".replace("top", "brabo") #Python é brabo

#find() e index()
#find() retorna o índice da primeira ocorrência, ou -1 se não acabar.
#index() é igual, mas lança erro se não achar
"banana".find("na") #2
"banana".find("na") #2

#split(sep) e join(lista)
#split(sep) divide a string.
#join() junta elementos de uma lista em uma string.
"nome, sobrenome".split(",") #['nome','sobrenome']
"-".join(['21', '04', '2025']) # '21-04-2025'

#startwith() e endswith()
#Verificam se começa ou termina com uma substring
"python".startswith("py") # True
"python".endswith("on") # True

#isdigit()/isalpha()/isalnum()/isspace()
#Verificam o tipo de caractere na string
"123".isdigit() #True
"abc".isalpha() #True
"abc123".isalnum() #True
"   ".isspace() #True

#capitalize()/ title()
#capitalize() deixa só a primeira letra da string maiúscula.
#title() deixa a primeira letra de cada palavra maiúscula
"python é massa".capitalize() #'Python é massa'
"python é massa".title() #'Python é Massa'

#count(sub)
#Conta quantas vezes uma substring aparece.
"banana".count("na") #2