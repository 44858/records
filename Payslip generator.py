#Lewis Travers
#30/01/2015
#Payslip generator

class Payslip:
    def __init__(self):
        self.name = None
        self.number = None
        self.hours = None
        self.pay = None

def details():
    payslip = Payslip()
    print("Playslip Generator")
    payslip.name = input("Please enter the name of the employee: ")
    payslip.number = int(input("Please enter the employee number: "))
    payslip.hours = int(input("Please enter the amount of hours worked by the employee: "))
    payslip.pay = int(input("Please enter the pay per hour of the employee(in pounds): "))
    return payslip

def display_payslip(payslip):
    print("*"*35)
    print("* Payslip" " "*23 "*")
    print("* Name: {0}".format(payslip.name)" "*27-len(payslip.name)"*")
    print("* Employee Number: {0}".format(payslip.number)" "*16-len(payslip.number)"*")
    print("* Hours Worked: {0}".format(payslip.hours)" "*19-len(payslip.hours)"*")
    print("* Rate of Pay: £{0}".format(payslip.pay)" "*19-len(payslip.pay)"*")
    total = payslip.hours * payslip.pay
    print("*Total Pay: £{0}".format(total)" "*22-len(total)"*")
    print("*"*35)


#-----------------------------------------------------------------------#
#main program

payslips = details()
table = display_payslip(payslip)
print(table)

