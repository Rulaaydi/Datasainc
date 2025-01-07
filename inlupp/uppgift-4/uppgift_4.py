# Uppgift 4
# Skapa en funktion fibonacci(n) som returnerar en lista med de första n Fibonacci-talen.

# Uppgift 4: Fibonacci-funktion

def fibonacci(n):
    
    if n <= 0:
        return "Ange ett positivt heltal."
    
    
    fib_lista = [0, 1] if n > 1 else [0]
    
    
    for i in range(2, n):
        fib_lista.append(fib_lista[i-1] + fib_lista[i-2])
    
    return fib_lista


n = 10  
resultat = fibonacci(n)
print(f"De första {n} Fibonacci-talen är: {resultat}")
