# Recebe a idade do usuario como string
age = input("Digite sua idade: ")

# Faz "cast" da idade para inteiro e calcula
age = int(age) + 10

# exibe tudo "interpolando" 
print(f"Daqui a 10 anos você terá {age} anos.")