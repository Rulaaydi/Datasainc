# Uppgift 10
# Skapa en funktion celsius_to_fahrenheit(celsius) som konverterar en temperatur från Celsius till Fahrenheit.
 
def celsius_to_fahrenheit(celsius):
    
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


celsius = 25
resultat = celsius_to_fahrenheit(celsius)
print(f"{celsius} grader Celsius är lika med {resultat:.2f} grader Fahrenheit.")
