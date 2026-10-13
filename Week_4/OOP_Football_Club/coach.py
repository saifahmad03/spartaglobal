# coach.py
from person import Person

class Coach(Person):
    def __init__(self, name, age, nationality, salary, contract_end_date, specialism):
        super().__init__(name, age, nationality, salary, contract_end_date)
        self.specialism = specialism

    def get_role(self):
        return "Coach"

    def calculate_weekly_wage(self):
        return self.get_salary() / 52