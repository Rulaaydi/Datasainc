# Uppgift 9
# Skapa en funktion is_palindrome(string) som kontrollerar om en given sträng är ett palindrom (dvs. samma framifrån och bakifrån).

def funktions_namn(variabel_namn: datatyp) -> returtyp:
    """
    Skriv beskrivning här.
    """
    pass 
def is_palindrome(string):
    
    clean_string = ''.join(char.lower() for char in string if char.isalnum())
    
   
    return clean_string == clean_string[::-1]


text1 = "Anna"
text2 = "Hello"
text3 = "A man, a plan, a canal: Panama"

print(f"Är '{text1}' ett palindrom
