age = input("Qual sua idade? ")

age = int(age)

if age >= 18:
    print("Você é maior de idade e pode votar!")
elif age >= 16 and age < 18:
    print("Você é menor de idade, mas pode votar!")
else:
    print("Você é menor de idade e não pode votar!")