# O cáculi do KPI do bôbus de 2024 é de '1000 + salario * bônus'

CONSTANTE_BONUS = 1000

#  1) Solicita ao usuário que digite seu nome
nome = input('Digite o seu nome: ')

# 2) Solicita ao usuário que digite  valor do seu salário
salario = float(input('Digite o seu salário: '))

# 3) Solicita ao usuário o valor do bônus recebido.
# converte a entrada para um número de ponto flutuante.
bonus = float(input('Digite o seu bônus: '))

# 4) Calculo o valor do bônus final
valor_do_bonus = (CONSTANTE_BONUS + (salario * bonus))

# 5) Imprime a mensagem personalizada incluindo o nome do usuário e o valor bônus
print(f"O usuario {nome} possui o bônus de {valor_do_bonus:.2f}")

# Bônus: Quantos bugs e riscos você consegue identificar ness programa?

      
 

