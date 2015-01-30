#Lewis Travers
#30/01/2015
#Payslip Generator advanced

class Payslip:
    def __init__(self):
        self.name = None
        self.number = None
        self.hours = None
        self.pay = None

payslips = []

def enter_values():
    for count in range(15):
        payslip = Payslip()
        payslip.name = input("Please enter the name of the employee: ")
        payslip.number = int(input("Please enter the employee's employee number: "))
        payslip.hours = int(input("Please enter the number of hours worked by the employee: "))
        payslip.pay = int(input("Please enter the pay per hour of the employee(in pounds): "))
        payslips.append(payslip)

