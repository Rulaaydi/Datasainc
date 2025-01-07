# Uppgift 12
# Skapa en funktion create_student_register(students) som tar emot en lista med namn och ålder och returnerar en dictionary där namnet är nyckeln och åldern är värdet.

def funktions_namn(variabel_namn: datatyp) -> returtyp:
    """
    Skriv beskrivning här.
    """
    pass 

def create_student_register(students):
   
    student_register = {}
    

    for student in students:
        name, age = student
        student_register[name] = age
    
    return student_register


students = [("Anna", 21), ("John", 22), ("Maria", 20)]
resultat = create_student_register(students)
print(f"Studentregistret: {resultat}")
