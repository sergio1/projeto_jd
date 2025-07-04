# Inteiros (int)
# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
''''
numero1 = input("Inserir o primeiro número inteiro: ")
numero2 = input("Inserir o segundo número inteiro: ")

if numero1.isalpha() or numero2.isalpha():
    print("Erro: Um ou ambos os números inseridos não são válidos.")
    exit()
    
if numero1.isspace() or numero2.isspace():
    print("Erro: Um ou ambos os números inseridos estão vazios.")
    exit()

resultado = int(numero1) + int(numero2)
#print(numero2.isdigit())   # True se for número

print(f"A soma de {numero1} e {numero2} é: {resultado}")
'''
# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
''''
numero = input("Inserir o primeiro número inteiro: ")

if numero.isalpha():
    print("Erro: Um ou ambos os números inseridos não são válidos.")
    exit()
    
if numero.isspace():
    print("Erro: Um ou ambos os números inseridos estão vazios.")
    exit()

resultado = int(numero) % 5
print(f"O resto da divisão de {numero} por 5 é: {resultado}")
'''
# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
'''
numero1 = input("Inserir o primeiro número inteiro: ")
numero2 = input("Inserir o segundo número inteiro: ")

if numero1.isalpha() or numero2.isalpha():
    print("Erro: Um ou ambos os números inseridos não são válidos.")
    exit()
    
if numero1.isspace() or numero2.isspace():
    print("Erro: Um ou ambos os números inseridos estão vazios.")
    exit()

resultado = int(numero1) * int(numero2)
#print(numero2.isdigit())   # True se for número

print(f"A multiplicacao de {numero1} e {numero2} é: {resultado}")
'''

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
'''
try:
    numero1 = input("Inserir o primeiro número inteiro: ")
    numero2 = input("Inserir o segundo número inteiro: ")
    resultado = int(numero1) // int(numero2)
    print(f"O resultado da divisão inteira de {numero1} por {numero2} é: {resultado}")

except ZeroDivisionError as e:
    print("Erro: Divisão por zero não é permitida." + str(e))

else:
    print('Divisão relalizada com sucesso.')

finally:
    print("Fim do programa.")
'''
# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
'''
numero = input("Inserir um número inteiro: ")

if numero.isalpha():
    print("Erro: Um ou ambos os números inseridos não são válidos.")
    exit()
    
if numero.isspace():
    print("Erro: Um ou ambos os números inseridos estão vazios.")
    exit()

resultado = int(numero) ** 2
print(f"O quadrado de {numero} : {resultado}")
'''

# #### Números de Ponto Flutuante (`float`)
# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
'''
numero1 = input("Inserir o primeiro número flutuante: ")
numero2 = input("Inserir o segundo número flutuante: ")

if numero1.isalpha() or numero2.isalpha():
    print("Erro: Um ou ambos os números inseridos não são válidos.")
    exit()
    
if numero1.isspace() or numero2.isspace():
    print("Erro: Um ou ambos os números inseridos estão vazios.")
    exit()

if "," in numero1:
    numero1 = numero1.replace(",",".")

if "," in numero2: 
    numero2 = numero2.replace(",",".")
    
resultado = float(numero1) + float(numero2)
#print(numero2.isdigit())   # True se for número

print(f"A multiplicacao de {numero1} e {numero2} é: {resultado}")
'''

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
'''
numero1 = input("Inserir o primeiro número flutuante: ")
numero2 = input("Inserir o segundo número flutuante: ")

if numero1.isalpha() or numero2.isalpha():
    print("Erro: Um ou ambos os números inseridos não são válidos.")
    exit()
    
if numero1.isspace() or numero2.isspace():
    print("Erro: Um ou ambos os números inseridos estão vazios.")
    exit()

if "," in numero1:
    numero1 = numero1.replace(",",".")

if "," in numero2: 
    numero2 = numero2.replace(",",".")

resultado = (float(numero1) + float(numero2)) /2
#print(numero2.isdigit())   # True se for número

print(f"A média de {numero1} + {numero2} é: {resultado}")
'''

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
'''
numero1 = input("Inserir o primeiro número flutuante (base da potência): ")
numero2 = input("Inserir o segundo  número flutuante (expoente da potência): ")
if numero1.isalpha() or numero2.isalpha():
    print("Erro: Um ou ambos os números inseridos não são válidos.")
    exit()
    
if numero1.isspace() or numero2.isspace():
    print("Erro: Um ou ambos os números inseridos estão vazios.")
    exit()

if "," in numero1:
    numero1 = numero1.replace(",",".")

if "," in numero2: 
    numero2 = numero2.replace(",",".")

resultado = float(numero1) ** float(numero2)
#print(numero2.isdigit())   # True se for número

print(f"A o resultada do potência com base {numero1} é expoente  {numero2} é: {resultado}")
'''

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
'''
temperatura = input("Inserir a temperatiura em graus Celsius : ")

if temperatura.isalpha():
    print("Erro: Um ou ambos os números inseridos não são válidos.")
    exit()
    
if temperatura.isspace():
    print("Erro: Um ou ambos os números inseridos estão vazios.")
    exit()

if "," in temperatura:
    temperatura = temperatura.replace(",",".")

if "," in temperatura: 
    temperatura = temperatura.replace(",",".")

temperatura = (float(temperatura)*9/5)+32

print(f"A temperatura em graus Fahrenheit é : {temperatura:.2f}F")
'''

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
'''raio_do_circulo = float(input("Inserir o raio do circulo: "))
import math
area_do_circulo = math.pi * (raio_do_circulo ** 2)
print(f"A área do circulo com raaio {raio_do_circulo} é : {area_do_circulo:.2f}")'''


# #### Strings (`str`)
# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
''''
palavra = input("Inserir uma string : ")

if palavra.isnumeric():
    print("Erro: foi inserido um número")
    exit()
    
if palavra.isspace():
    print("Erro: foi inserido dados vazios.")
    exit()

print(f"A string em maiúsculas é: {palavra.upper()}")
'''

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
'''
nome_completo = input("Inserir nome completo : ")

if nome_completo.isnumeric():
    print("Erro: foi inserido um número")
    exit()
    
if nome_completo.isspace():
    print("Erro: foi inserido dados vazios.")
    exit()

print(f"A nome em minusculo é: {nome_completo.lower()}")
''' 

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços
# em branco no início e no final.
'''
frase = input("Inserir uma frase: ")
if frase.isnumeric():
    print("Erro: foi inserido um número")
    exit()
    
if frase.isspace():
    print("Erro: foi inserido dados vazios.")
    exit()

print(f"A nome em minusculo é: {frase.strip()}")
'''

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
'''data = input("Inserir uma data no formato dd/mm/aaaa: ")
dia, mes, ano = data.split('/')
print(f"Dia: {dia}, Mês: {mes}, Ano: {ano}")'''

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
'''
frase1 = input("Inserir primeira frase: ")
frase2 = input("Inserir segunda frase: ")

print(f"A frase concatenada é: {frase1} {frase2}")
'''

# #### Booleanos (`bool`)
# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
'''
valor1 = input("Inserir True ou False : ")
valor2 = input("Inserir True ou False : ")

print("Resultado do AND lógico:", valor1 and valor2)
print("Resultado do OR lógico:", valor1 or valor2)
print("Resultado do NOT lógico:", not valor1)
print("Resultado da igualdade:", valor1 == valor2)
print("Resultado da diferença: ", valor1 != valor2)
'''

# #### try-except e if
# 21: Conversor de Temperatura
'''
try:
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C é igual a {fahrenheit}°F.") 
except ValueError as e:
    print("Por favor, digite um número válido para a temperatura.")
    print("Erro:", str(e))
'''

# 22: Verificador de Palíndromo
'''
try: 
    texto = input("Digite uma palavra ou frase: ")
    if not texto.isalnum():
        print('Existe caracteres especiais ou espaços em branco.')
        exit()
    
    texto = texto.lower().replace(" ", "")  # Remove espaços e deixa minúsculo
    if texto == texto[::-1]:
        print(f"{texto} é um palíndromo.")
    else:
        print(f"{texto} não é um palìndromo.")


except ValueError as e:
    print("Por favor, digite palavra ou frase.")
    print("Erro:", str(e))
'''

# 23: Calculadora Simples
'''
try:
    numero1 = input("Inserir o primeiro número flutuante: ")
    numero2 = input("Inserir o segundo número flutuante: ")
    operacao = input("Escolha a operação (+,-,*,/): ")


    if operacao not in ['+','-','*','/']:
        print("Erro: Operação inválida, Informe uma operação válida (+,-,*,/).")
        exit()

    if numero1.isalpha() or numero2.isalpha():
        print("Erro: Um ou ambos os números inseridos não são válidos.")
        exit()
        
    if numero1.isspace() or numero2.isspace():
        print("Erro: Um ou ambos os números inseridos estão vazios.")
        exit()

    if "," in numero1:
        numero1 = numero1.replace(",",".")

    if "," in numero2: 
        numero2 = numero2.replace(",",".")
        
    if operacao == '+':     
        resultado = float(numero1) + float(numero2)
    elif operacao == '-':
        resultado = float(numero1) - float(numero2)
    elif operacao == '*': 
        resultado = float(numero1) * float(numero2)
    else: 
        resultado = float(numero1) / float(numero2)

    print(f"O resultado da operação {numero1} {operacao} {numero2} é: {resultado:.2f}")
except:
    print('Erro: Ocorreu um erro ao realizar a operação. Tente novamente.')
finally:
    print('Fim do programa.')
'''

# 24: Classificador de Números
'''
try:
    numero = input("informe um numero: ")
    if numero.isalpha():
        print("Erro: Um ou ambos os números inseridos não são válidos.")
        exit()
        
    if numero.isspace():
        print("Erro: Um ou ambos os números inseridos estão vazios.")
        exit()

    if "," in numero:
        numero = numero.replace(",",".")

    numero = float(numero)
    if numero > 0:
        sinal = "positivo"
    elif numero < 0:
        sinal = "negativo"
    else:
        sinal = "zero"

    if numero == int(numero):
        tipo = "inteiro"    
        if int(numero) % 2 == 0:
            paridade = "par"
        else:
            paridade = "ímpar"
    else:
        tipo = "decimal"
        paridade = "paridade não aplicável (número decimal)"

    print(f"O número {numero} é {sinal}, do tipo {tipo} e é {paridade}.")
except:
    print('Erro: Ocorreu um erro ao realizar a operação. Tente novamente.')
finally:
    print('Fim do programa.')
'''

# 25: Conversão de Tipo com Validação
entrada_lista = input("Digite uma lista de números separados por vírgula: ")
print(entrada_lista)
numeros_str = entrada_lista.split(",")
print(f"Lista Original : {numeros_str}")
numeros_int = []
try:
    for num in numeros_str:
        if num.strip().isdigit():
           numeros_int.append(int(num.strip()))

    print("Lista de inteiros:", numeros_int)
    if len(numeros_int) == 0:
        print("Erro: Nenhum número inteiro válido foi inserido.")
        
    if not numeros_int:
        print("Erro: A lista não contém números inteiros válidos.")
        
except ValueError:
    print("Erro: certifique-se de que todos os elementos são números inteiros válidos.")