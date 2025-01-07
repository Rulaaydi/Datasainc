# Uppgift 7
# Skapa en funktion validate_password(password) som kontrollerar att lösenordet är minst 8 tecken långt och innehåller minst en siffra.



def validate_password(password):
    
    if len(password) < 8:
        return 
    
    if not any(char.isupper() for char in password):
        return