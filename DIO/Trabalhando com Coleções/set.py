# 🐍 Conjuntos em Python

# Conjuntos são coleções não ordenadas e mutáveis, usadas para armazenar elementos únicos (sem duplicatas).

# Criando Conjuntos
numeros = {1, 2, 3, 4}            # Conjunto com inteiros
frutas = {"maçã", "banana", "laranja"}  # Conjunto com strings

# Acessando elementos do conjunto
# Conjuntos não têm índice, então não podemos acessar por posição, mas podemos iterar sobre os elementos:
for fruta in frutas:
    print(fruta)  # Imprime cada item do conjunto

# Adicionando elementos ao conjunto
frutas.add("uva")  # Adiciona "uva" ao conjunto

# Removendo elementos do conjunto
# Usando remove() - Remove o elemento, mas gera erro se o elemento não existir
frutas.remove("banana")  # Remove "banana" do conjunto

# Usando discard() - Remove o elemento sem gerar erro, mesmo que o elemento não exista
frutas.discard("abacaxi")  # Não gera erro, mesmo se "abacaxi" não estiver no conjunto

# Verificando se um elemento está no conjunto
if "maçã" in frutas:
    print("Maçã está no conjunto!")  # Condicional para verificar a presença

# Operações com Conjuntos
# União: Combina os elementos de dois conjuntos
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
uniao = conjunto1 | conjunto2  # Resultado: {1, 2, 3, 4, 5}
print("União:", uniao)

# Interseção: Retorna os elementos comuns entre dois conjuntos
interseccao = conjunto1 & conjunto2  # Resultado: {3}
print("Interseção:", interseccao)

# Diferença: Retorna os elementos do primeiro conjunto que não estão no segundo
diferenca = conjunto1 - conjunto2  # Resultado: {1, 2}
print("Diferença:", diferenca)

# Diferença Simétrica: Retorna os elementos que estão em um dos conjuntos, mas não em ambos
dif_simetrica = conjunto1 ^ conjunto2  # Resultado: {1, 2, 4, 5}
print("Diferença Simétrica:", dif_simetrica)

# Funções úteis com Conjuntos
# len() - Retorna o número de elementos no conjunto
print("Número de elementos em frutas:", len(frutas))

# clear() - Remove todos os elementos do conjunto
frutas.clear()  # Agora o conjunto está vazio
print("Conjunto após clear:", frutas)

# copy() - Cria uma cópia do conjunto
frutas_copy = frutas.copy()  # Cópia do conjunto
print("Cópia do conjunto:", frutas_copy)

# Observações
# - Conjuntos não permitem elementos duplicados. Se você tentar adicionar um valor já existente, ele será ignorado.
# - A ordem dos elementos em um conjunto não é garantida, ou seja, os elementos não têm índice fixo.