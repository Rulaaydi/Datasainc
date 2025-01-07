# Uppgift 11
# Skapa en funktion word_count(text) som returnerar antalet ord i en given text.


def word_count(text):
    
    words = text.split()
    return len(words)


text = "Detta är ett exempel på text med flera ord."
resultat = word_count(text)
print(f"Antalet ord i texten är: {resultat}")

