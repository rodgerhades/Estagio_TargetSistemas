def fibonacci(n):
    
    fibonacci_sequence = [a, b]
    
    while b < n:
        a, b = b, a + b
        fibonacci_sequence.append(b)
    
    return fibonacci_sequence

def verifica_fibonacci(number):
    
    fib_sequence = fibonacci(number)
    
    if number in fib_sequence:
        return f"O número {number} pertence a sequência de Fibonacci."
    else:
        return f"O número {number} não pertence a sequência de Fibonacci."

numero = int(input("Informe um número: "))
resultado = verifica_fibonacci(numero)
print(resultado)