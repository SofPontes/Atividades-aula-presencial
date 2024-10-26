def fibonacci(n):
    sequencia = []
    a, b = 0, 1
    for _ in range(n):
        sequencia.append(a)
        a, b = b, a + b
    return sequencia
    
#define numero
n = 10
fibonacci_ate_n = fibonacci(n)
print(f"sequencia de fibonacci ate {n} termina: {fibonacci_ate_n}")
