# Uppgift 2
# Skapa en funktion sum_list(numbers) som returnerar summan av alla siffror i listan.

def sum_list(numbers):
    """Returnerar summan av alla siffror i listan."""
    total = sum(numbers)
    return total


my_list = [1, 2, 3, 4, 5]
result = sum_list(my_list)
print(f"Summan av listan är: {result}")
