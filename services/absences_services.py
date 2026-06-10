from models.absences_models import AbsencesModels

class AbsenceService:
    def __init__(self):
        self.model = AbsencesModels()

    def ajouter_absence(self):
        student_id = input("ID étudiant: ")
        date = input("Date: ")
        status = input("Status (justifiée/non): ")

        self.model.ajouter(student_id, date, status)
        print("✅ Absence ajoutée")

    def compter_absences(self):
        student_id = input("ID étudiant: ")
        total = self.model.compter_absences(student_id)
        print("Total absences:", total)