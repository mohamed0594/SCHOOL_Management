from models.notes_models import note_model



def matieres_add():
    student_id = input("ID étudiant : ")
    subject_id = input("ID matière : ")
    note = input("Note : ")
    note_model.ajouter_notes(student_id, subject_id, note)
    print("Note ajoutée")


def afficher_notes():
    for n in note_model.afficher_notes():
        print(n)


def modifier_notes():
    id_note = input("ID note : ")
    id_etudient = input("ID étudiant : ")
    id_matiere = input("ID matière : ")
    notes = input("Note : ")
                  
    
    note_model.modifier_notes(id_note, id_etudient, id_matiere, notes)
    print("Note modifiée")


def supp_notes():
    note_model.supprimer_notes(input("ID note : "))
    print("Note supprimée")
    