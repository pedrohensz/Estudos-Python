def sacar (valor):
    saldo = 500

    if saldo >= valor:
        novo_saldo = saldo - valor
        print(f"Valor sacado. Novo saldo:{novo_saldo}")

    """
    O python nos obriga em diversos momentos a identar o código
    para que ele consiga rodar o mesmo, no caso acima, tudo 
    que estava abaixo do if rodou apenas pois estava identado.
       """    

sacar (100)