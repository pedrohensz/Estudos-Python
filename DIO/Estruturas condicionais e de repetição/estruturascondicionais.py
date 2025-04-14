#If else normal
maioridade = 18
idade_especial = 12

idade = int(input("Informe sua idade: "))
if idade >= maioridade:
    print("Maior de idade pode tirar a CNH")
elif idade < maioridade and idade >= idade_especial:
    print("Menor de idade não pode tirar a CNH")
    print("Pode apenas realizar as aulas teóricas.")
else:
    print("Idade inválida.")



#If else aninhado
conta_normal = True
conta_universitária = False
saldo = 2000
saque = 500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso! ")
    elif saque <= (saldo+cheque_especial):
        print("Saldo realizado com uso do cheque especial")
    else:
        ("Não foi possível realizar o saque")
elif conta_universitária:
    if saldo >= saque:
        print("Saque realizado com sucesso")

    else:
        print ("Saque realizado com sucesso! ")

else:
    print("Sistema não reconheceu o seu tipo de conta, favor entrar em contato com seu gerente.")


#If ternário

saldo = 1000
saque = 999
status = "Sucesso" if saldo >= saque else "Falha"
print (f"{status} ao realizar o saque! ")