"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:

    def __init__(self, name, salaryType, bonusType, salary, contract, contractRate,bonus, hours, perHour):
        self.name = name
        self.salaryType = salaryType
        self.bonusType = bonusType
        self.salary = salary
        self.contract = contract
        self.contractRate = contractRate
        self.bonus = bonus
        self.hours = hours
        self.perHour = perHour      

    def get_pay(self):
        if self.salaryType == "monthly":
            if self.bonusType == "contractCommision":
                self.salary += self.contract * self.contractRate
            elif self.bonusType == "bonusCommision":
                self.salary += self.bonus

        elif self.salaryType == "contract":
            if self.bonusType == "contractCommision":
                self.salary += self.contract * self.contractRate
            elif self.bonusType == "bonusCommision":
                self.salary += self.bonus
        
        return self.salary

    def __str__(self):
        if self.salaryType == "monthly":
            if self.bonusType == "contractCommision":
                return self.name + " works on a monthly salary of " + str(self.salary) + " and recieves a commision for " + str(self.contract) + " contract(s) at " + str(self.contractRate) + "/contract" + ". Their total pay is " + str(self.salary)
            
            elif self.bonusType == "bonusCommision":
                return self.name + " works on a monthly salary of " + str(self.salary) + " and recieves a bonus commision of " + str(self.bonus) + ". Their total pay is " + str(self.salary)
            
            else:
                return self.name + " works on a monthly salary of " + str(self.salary) +  ". Their total pay is " + str(self.salary) 

        elif self.salaryType == "contract":
            if self.bonusType == "contractCommision":
                return self.name + " works on a contract of " + str(self.hours) + " hours at " + str(self.perHour) + "/hour" + " and recieves a commision for " + str(self.contract) + " contract(s) at " + str(self.contractRate) + "/contract" + ". Their total pay is " + str(self.salary)

            elif self.bonusType == "bonusCommision":
                return self.name + " works on a contract of " + str(self.hours) + " hours at " + str(self.perHour) + "/hour" + " and recieves a bonus commision of " + str(self.bonus) + ". Their total pay is " + str(self.salary) 

            else:
                return self.name + " works on a contract of " + str(self.hours) + " hours at " + str(self.perHour) + "/hour" + ". Their total pay is " + str(self.salary) 

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', "monthly", None, 4000, None , None, None, None, None )

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', "contract", None, (100 * 25), None, None, None, 100, 25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', "monthly", "contractCommision", 3000, 4, 200, None, None, None)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', "contract", "contractCommision", (150 * 25), 3, 220, None, 150, 25)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', "monthly", "bonusCommision", 2000, None, None, 1500, None, None)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', "contract", "bonusCommision", (120 * 30), None, None, 600, 120, 30)


