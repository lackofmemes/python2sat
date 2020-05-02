from Person import *
from Office import *

done = False
my_office = Office("Rona", "Doctor")
print("Welcome!")

while(not done):
    print("Enter command: ")
    user_input = input()

    if user_input == "Exit":
        done = True
    elif user_input.split(" ")[0] == "Add":
        temp = user_input.split(" ")
        patient_to_add = Person(temp[1], temp[2], temp[3], temp[4])
        my_office.add_patient(patient_to_add)
        print("Patient has been added")
    elif user_input == "All":
        print(my_office)   
    elif user_input == "Get":
        result = my_office.get_next_patient()
        if result == -1:
            print("There is no body in line")
        else:
            print("The next patient is --> " + str(result))
    else:
        print("The command you entered is invalid")
    
