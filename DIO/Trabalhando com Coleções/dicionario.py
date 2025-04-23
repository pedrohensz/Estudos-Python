# Dicionários: Criação e Acesso aos Dados

# O dicionário em Python é uma estrutura de dados que armazena pares de chave-valor
# Ele é útil quando você precisa de uma associação entre chaves únicas e seus respectivos valores.
# A criação de um dicionário pode ser feita de várias formas, e o acesso aos dados é feito através da chave.

# Criação de dicionários
#Usando chaves {} ou a função dict()
dicionario = {"nome": "Pedro", "idade": 22, "cidade": "São Paulo"}
dicionario_vazio = {}

#Acessando valores através da chave:
print(dicionario["nome"]) #Output: Pedro
print(dicionario.get('idade')) # Output: 22

#Adicionando ou atualizando um valor:
dicionario["idade"] = 23 # Atualiza a chave "idade" com um novo valor
dicionario["profissao"] = "Desenvolvedor" #Adiciona a chave "profissao" com valor "Desenvolvedor"

#Verificando se uma chave existe:
if "nome" in dicionario:
    print("A chave 'nome' existe no dicionario")

# Removendo um item do dicionario
del dicionario ["cidade"] # Remove a chave "cidade"
valor_removido = dicionario.pop("idade") # Remove e retorna valor da chave "idade"

#Iterando sobre chaves e valor:
for chave, valor in dicionario.items():
    print(f"Chave: {chave}, Valor:{valor}")


# Métodos úteis:
# .keys() - Retorno todas as chaves.
# .values() - Retorna todos os valores.
# .items() - Retorna uma lista de tuplas (chave, valor)
# .update() - Atualiza um dicionario com outros.
# .clear() - Remove todos os items do dicionario.