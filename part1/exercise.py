from office import Office
from person import Person


def print_emplopyees():
    print('List of employees:')
    for employee in ecorus.people_working:
        print(f' - {employee.name}, {employee.age}')


ecorus = Office('Ecorus')

eduardo = Person('Eduardo', 38)
levi = Person('Levi', 19)

ecorus.start_working_for(levi)
ecorus.start_working_for(eduardo)

print_emplopyees()

ecorus.finished_working_for(eduardo)
print('\nremoved Eduardo from working.\n')

print_emplopyees()
