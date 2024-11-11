from __future__ import annotations
from enum import Enum

class Gender(Enum):
    MALE = "male"
    FEMALE = "female"


class Person:
    def __init__(self, name: str) -> None:
        self.name = name
    
    def __str__(self):
        return f'{self.name} is alive!!!'


# inheretance
class Man(Person):
    gender = Gender.MALE  # assosiation


# inheretance
class Woman(Person):
    gender = Gender.FEMALE  # assosiation


class Company:
    """
    compamy is composition of employees
    **company owns employees**
    """
    def __init__(self, name: str) -> None:
        self.name = name
        self.employees = []

    def __str__(self) -> str:
        return f"company {self.name} with employees: {len(self.employees)}"

    def hire_employee(self, person: Person, position: str) -> None:
        employee = Employee(person=person, company=self, position=position)
        self.employees.append(employee)
        return
    
    def liquidate(self) -> None:
        self.employees = []
        return


class Employee:
    """
    employee is aggregation of person and company
    **employee is composed of person and company**
    """
    def __init__(self, person: Person, company: Company, position: str):
        self.person = person    # aggregation
        self.company = company  # aggregation
        self.position = position
    
    def __str__(self):
        return f"{self.person.name} works at {self.company.name} at position {self.position}"
    

if __name__ == "__main__":
    jonh = Man("John")
    mike = Man("Mike")
    lily = Woman("Lily")
    company = Company("CocaCola")

    company.hire_employee(jonh, "developer")
    company.hire_employee(mike, "analyst")
    company.hire_employee(lily, "qa")

    company.liquidate() # company is deleted, but people still exists (aggregation property)