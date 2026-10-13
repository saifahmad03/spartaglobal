class Person:
    def __init__(self, name, age, nationality, salary, contract_end_date):
        self.name = name
        self.age = age
        self.nationality = nationality
        self.__salary = salary
        self.__contract_end_date = contract_end_date

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        if new_salary < 0:
            print("Salary cannot be negative")
        else:
            self.__salary = new_salary

    def get_contract_end_date(self):
        return self.__contract_end_date

    def get_role(self):
        return "Person"

    def calculate_weekly_wage(self):
        return self.get_salary() / 52