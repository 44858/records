#Lewis Travers
#27/01/2015
#Student Marks

class StudentMarks:
    def __init__(self):
        self.name =  None
        self.marks = None

def details():
    for count in range(3):
        new_record = StudentMarks()
        new_record.name = input("Please enter the name of the student: ")
        new_record.marks = int(input("Please enter the amount of marks earned by the student: "))
        records.append(new_record)

def table(records):
    print("-"*23)
    print("|   Name   |   Mark   |")       
    for record in records:
        print("|   {0:<2}   |   {1:<2}   |".format(record.name, record.marks))
    print("-"*23)
#------------------------------------------------------------------------------#
#main  program
        
records = []
record = details()
table = table(records)
print(table)
