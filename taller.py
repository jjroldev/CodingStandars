class Student:
    def __init__(self, student_id, name):
        if not student_id or not name:
            raise ValueError("Error: ID y nombre no pueden estar vacíos.")
        self.id = student_id
        self.name = name
        self.grades = []
        self.is_passed = "No"
        self.honor = "No"

    def add_grade(self, grade):
        try:
            grade = float(grade)
            if 0 <= grade <= 100:
                self.grades.append(grade)
            else:
                print(f"Error: la nota {grade} está fuera del rango 0–100.")
        except ValueError:
            print(f"Error: '{grade}' no es un número válido.")

    def calc_average(self):
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def letter_grade(self):
        avg = self.calc_average()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

    def check_pass_fail(self):
        self.is_passed = "Yes" if self.calc_average() >= 60 else "No"

    def check_honor(self):
        self.honor = "Yes" if self.calc_average() >= 90 else "No"

    def delete_grade(self, value_or_index):
        try:
            if isinstance(value_or_index, int):
                del self.grades[value_or_index]
            else:
                self.grades.remove(float(value_or_index))
        except (ValueError, IndexError):
            print(f"Error: no se pudo eliminar '{value_or_index}'. No existe o índice inválido.")

    def report(self):
        avg = self.calc_average()
        self.check_pass_fail()
        self.check_honor()
        print("📘 STUDENT REPORT")
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Grades Count: {len(self.grades)}")
        print(f"Average Grade: {avg:.2f}")
        print(f"Letter Grade: {self.letter_grade()}")
        print(f"Passed: {self.is_passed}")
        print(f"Honor Roll: {self.honor}")
        print("-" * 25)


def start_run():
    s = Student("A001", "Justin")
    s.add_grade(95)
    s.add_grade(88)
    s.add_grade("fifty")  # inválido
    s.add_grade(100)
    s.delete_grade(1)  # eliminar por índice
    s.delete_grade(77.5)  # inexistente
    s.report()


start_run()
