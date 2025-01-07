# Uppgift 5
# Skapa en funktion filter_odd(numbers) som returnerar en lista med alla jämna tal från den givna listan.


def filter_odd(numbers):
   
    even_numbers = [num for num in numbers if num % 2 == 0]
    return even_numbers


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultat = filter_odd(numbers)
print(f"Jämna tal från listan är: {resultat}")
