### Desafio - Refatorar o projeto da aula anterior evitando Bugs!

# 1) Solicita ao usuário que digite seu nome
nome_usuario = input('Digite o seu nome : ')

if nome_usuario.isdigit():
    print("O nome não pode conter apenas números.")
    exit()

elif len(nome_usuario.strip()) == 0:
    print("O nome não pode ser vazio.")
    exit()
elif any(char.isdigit() for char in nome_usuario):
    print("O nome não pode conter números.")
    exit()
else:
    print("Nome válido:", nome_usuario)

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
salario = input('Digite o seu salário: ')

if salario.isalpha():
    print("Erro: valor inserido não é válidos.")
    exit()
    
if salario.isspace():
    print("Erro: não inserir valor vazios.")
    exit()
try:
    salario = float(salario)
    if salario <= 0:
        print("Erro: O salário deve ser um número positivo e maior que zero.")
        exit()
    
except ValueError:
    print("Erro: valor inválido para salário.")


# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
BONUS_FIXO = 1000.00

bonus = input('Digite o seu bonus: ')

if bonus.isalpha():
    print("Erro: valor inserido não é válidos.")
    exit()
    
if bonus.isspace():
    print("Erro: não inserir valor vazios.")
    exit()
try:
    bonus = float(bonus)
    if bonus <= 0:
        print("Erro: O bonus deve ser um número positivo e maior que zero.")
        exit()
    
except ValueError:
    print("Erro: valor inválido para bonus.")


# 4) Calcule o valor do bônus final
bonus_final = BONUS_FIXO + (salario * bonus)

# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print(f"{nome_usuario}, seu salário é R${salario:.2f} e seu bônus final é R${bonus_final:.2f}.")


# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?