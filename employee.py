class Employee:
    MONTHLY = "monthly"
    CONTRACT = "contract"

    def __init__(self, name, salary_type, bonus_type=None, salary=None, contract=None, contract_rate=None, bonus=None, hours=None, per_hour=None):
        self.name = name
        self.salary_type = salary_type
        self.bonus_type = bonus_type
        self.salary = salary
        self.contract = contract
        self.contract_rate = contract_rate
        self.bonus = bonus
        self.hours = hours
        self.per_hour = per_hour

    def get_pay(self):
        pay = 0

        if self.salary_type == self.MONTHLY:
            pay += self.salary
        elif self.salary_type == self.CONTRACT:
            pay += self.hours * self.per_hour

        if self.bonus_type == "contractCommision":
            pay += self.contract * self.contract_rate
        elif self.bonus_type == "bonusCommision":
            pay += self.bonus

        return pay

    def __str__(self):
        pay = self.get_pay()
        pay_info = f"{self.name} works on a "

        if self.salary_type == self.MONTHLY:
            pay_info += f"monthly salary of {self.salary}"
        elif self.salary_type == self.CONTRACT:
            pay_info += f"contract of {self.hours} hours at {self.per_hour}/hour"

        if self.bonus_type == "contractCommision":
            pay_info += f" and receives a commission for {self.contract} contract(s) at {self.contract_rate}/contract"
        elif self.bonus_type == "bonusCommision":
            pay_info += f" and receives a bonus commission of {self.bonus}"

        pay_info += f". Their total pay is {pay}."
        return pay_info

# The employee objects remain the same
billie = Employee('Billie', Employee.MONTHLY, None, 4000)
charlie = Employee('Charlie', Employee.CONTRACT, None, None, None, None, None, 100, 25)
renee = Employee('Renee', Employee.MONTHLY, "contractCommision", 3000, 4, 200)
jan = Employee('Jan', Employee.CONTRACT, "contractCommision", None, 3, 220, None, 150, 25)
robbie = Employee('Robbie', Employee.MONTHLY, "bonusCommision", 2000, None, None, 1500)
ariel = Employee('Ariel', Employee.CONTRACT, "bonusCommision", None, None, None, 600, 120, 30)
