# manager.py
from person import Person

class Manager(Person):
    def __init__(self, name, age, nationality, salary, contract_end_date, years_experience):
        super().__init__(name, age, nationality, salary, contract_end_date)
        self.years_experience = years_experience

    def get_role(self):
        return "Manager"

    def calculate_weekly_wage(self):
        return self.get_salary() / 52 + 2000   # management bonus