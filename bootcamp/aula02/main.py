numero = input("Inserir um número: ")
numero = int(numero) 

if isinstance(numero, int):
    print(f"O número {numero} é um inteiro")
#elif isinstance(numero, float):

else: 
    print(f"A variável não é um número válido")
