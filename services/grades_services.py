from models.grades_models import GradesModels

class GradeService:
    def __init__(self):
        self.model = GradesModels()

    def ajouter_note(self):
        student_id = input("ID étudiant: ")
        subject_id = input("ID matière: ")
        note = float(input("Note: "))

        self.model.ajouter(student_id, subject_id, note)
        print("✅ Note ajoutée")

    def voir_notes_etudiant(self):
        student_id = input("ID étudiant: ")
        notes = self.model.rechercher_par_etudiant(student_id)
        print(notes)

    def moyenne_etudiant(self):
        student_id = input("ID étudiant: ")
        moyenne = self.model.calculer_moyenne(student_id)
        print("📊 Moyenne:", moyenne)