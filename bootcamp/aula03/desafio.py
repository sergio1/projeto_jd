# Integre na solução anterior um fluxo de While 
# que repita o fluxo até que o usuário insira as 
# informações corretas
nome_valido = False
salario_valido = False
bonus_valido = False

while nome_valido is not True: 
    try:
        nome = input('Digite o nome do funcionário: ')
        if len(nome.strip()) == 0:
            raise ValueError('O nome não pode estar vazio')
        # verifica se há números no nome
        elif any(char.isdigit() for char in nome): 
            raise ValueError('O nome não pode conter números')
        else: 
            nome_valido = True
            print('Nome válilo:', nome)
    except ValueError as e: 
        print(f'Erro: {e}')

# que digite o valor do salário e converte para float

while salario_valido is not True:
    try:
        salario = float(input('Digite o salário do funcionário: '))
        if salario < 0:
            raise ValueError('O salário não pode ser negativo')
        elif salario == 0: 
            raise ValueError('O salário não pode ser zero')
        else: 
            salario_valido = True
            print('Salário válido:', salario)
    except ValueError as e:
        print(f'Erro: {e}')

while bonus_valido is not True:
    try:
        BONUS_FIXO = 1000.00
        bonus = input('Digite o seu bonus: ')
        if bonus.isalpha():
            raise ValueError("Erro: valor inserido não é válidos.")

        if bonus.isspace():
            raise ValueError("Erro: não inserir valor vazios.")

        bonus = float(bonus)
        if bonus <= 0:
            raise ValueError("Erro: O bonus deve ser um número positivo e maior que zero.")
        
        bonus_valido = True
    except ValueError as e:
        print(f"Erro: {e}")


# 4) Calcule o valor do bônus final
bonus_final = BONUS_FIXO + (salario * bonus)

# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print(f"{nome}, seu salário é R${salario:.2f} e seu bônus final é R${bonus_final:.2f}.")



