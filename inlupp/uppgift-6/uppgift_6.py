# Uppgift 6
# Skapa en funktion multiplication_table(n, limit) som returnerar multiplikationstabellen för n upp till limit i en lista.


def multiplication_table(n, limit):
    
    table = [n * i for i in range(1, limit + 1)]
    return table


n = 5
limit = 10
resultat = multiplication_table(n, limit)
print(f"Multiplikationstabellen för {n} upp till {limit} är: {resultat}")
