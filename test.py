from models.users_models import userModel
from models.notes_models import note_model
from models.users_models import userModel

user = userModel()

#user.ajouter_users(
 #   "Admin", "admin", "admin@gmail.com", "12345"
#)

#user.ajouter_users(
 #   "Prof","teachers", "prof@gmail.com", "1234"
#)

#user.ajouter_users(
   # "Etudiant", "students","student@gmail.com","123"
#)

#print(user.afficher_users())


from models.notes_models import note_model

note_model.ajouter_notes(1, 2, 15.5)

print("Note ajoutée avec succès.")

notes = [
    (1, 1, 15.5),
    (1, 2, 17),
    (1, 3, 12),

    (2, 1, 14),
    (2, 2, 16),
    (2, 3, 18),

    (3, 1, 10),
    (3, 2, 11),
    (3, 3, 13),

    (4, 1, 19),
    (4, 2, 18),
    (4, 3, 20),
]

for student_id, subject_id, note in notes:
    note_model.ajouter_notes(student_id, subject_id, note)

print("Toutes les notes ont été ajoutées avec succès.")