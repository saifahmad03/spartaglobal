from person import Person

class Player(Person):
    def __init__(self, name, age, nationality, salary, contract_end_date, position, squad_number):
        super().__init__(name, age, nationality, salary, contract_end_date)
        self.position = position
        self.squad_number = squad_number

    def get_role(self):
        return "Player"

    def calculate_weekly_wage(self):
        return self.get_salary() / 52 + 500