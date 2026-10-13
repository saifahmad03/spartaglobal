from player import Player
from manager import Manager
from coach import Coach


p1 = Player("Jude Bellingham", 24, "English", 520000, "2028-06-30", "Striker", 9)
m1 = Manager("Harry Kane", 32, "English", 2600000, "2027-06-30", 20)
c1 = Coach("Phil Jones", 45, "English", 90000, "2027-06-30", "Goalkeeping")

staff = [p1, m1, c1]


for member in staff:
    print(member.name, "-", member.get_role(), "-", round(member.calculate_weekly_wage(), 2))


print(p1.get_salary())
p1.set_salary(-100)
print(p1.get_salary())
print(p1.get_contract_end_date())


print(p1.name, p1.age, p1.nationality, p1.position, p1.squad_number)