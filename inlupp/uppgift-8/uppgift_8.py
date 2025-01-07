# Uppgift 8
# Skapa en funktion count_letters(string) som returnerar en dictionary med varje bokstav som nyckel och antalet förekomster som värde.


def count_letters(string):
    
    letter_count = {}
    
   
    for char in string:
        if char.isalpha(): 
            char = char.lower()
            letter_count[char] = letter_count.get(char, 0) + 1
            
    return letter_count


text = "Hello World"
resultat = count_letters(text)
print(f"Antal förekomster av varje bokstav i '{text}': {resultat}")
