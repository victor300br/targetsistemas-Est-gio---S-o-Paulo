def fibonacci(n):
    fib_sequence = [0, 1]
    while fib_sequence[-1] < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def verifica_fibonacci(numero):
    fib_sequence = fibonacci(numero)
    return f"O número {numero} pertence à sequência de Fibonacci." if numero in fib_sequence else f"O número {numero} não pertence à sequência de Fibonacci."

entrada = input("Informe um número: ")
try:
    numero_informado = float(entrada)
    if numero_informado < 0 or (numero_informado % 1 != 0):
        print(f"O número {numero_informado} não pertence à sequência de Fibonacci.")
    else:
        resultado = verifica_fibonacci(int(numero_informado))
        print(resultado)
except ValueError:
    print("Por favor, informe apenas números.")