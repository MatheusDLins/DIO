curso = "pYtHon"

#Maiúsculo
print(curso.upper())

#Minúsculo
print(curso.lower())

#Título
print(curso.title())

print("_"*5, "Eliminando espaços", "_"*5)
#ELIMINANDO ESPAÇOS EM BRANCO

curso = "        Python   "

#Todo espaço em branco
print(curso.strip())

#Antes da palavra
print(curso.lstrip())

#Depois da palavra
print(curso.rstrip())

print("_"*5, "Junções e centralização", "_"*5)
#JUNÇÕES E CENTRALIZAÇÃO

curso = "Python"

print(curso.center(10, "#"))

print(".".join(curso))