#AND = para ser True tudo tem que ser True
#OR = para ser True apenas um tem que ser True

print(f"True and True and True = {True and True and True}")
print(f"True and False and True = {True and False and True}")
print(f"False and False and False = {False and False and False}")
print(f"True or True or True = {True or True or True}")
print(f"True or False or False = {True or False or False}")
print(f"False or False or False = {False or False or False}")

saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)