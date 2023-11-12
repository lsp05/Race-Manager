

# Defining the check qualifers function and passing 3 lists through the parameters
def check_qualifiers(racerA, racerB, qualifiers):
    # There are only 3 qualifiers so i loop 3 times
    for i in range(3):
        print("Qualifier #" + str(i+1))
        # Checking to see if a racer has qualified or not
        if racerA[i] <= qualifiers[i]:
            print("Racer A Qualifies!")
        if racerB[i] <= qualifiers[i]:
            print("Racer B Qualifies!")
        if racerA[i] > qualifiers[i] and racerB[i] > qualifiers[i]:
            print("Neither racer qualified.")

# Defining the compare times function and passing 2 lists through the parameters
def compare_times(racerA, racerB):
    # checking to see if both of the lists have values in them
    if len(racerA) > 0 and len(racerB) > 0:
        # checking to see if the racers have same ammount of races or uneven ammount of races
        if len(racerA) != len(racerB):
            print("Racer A has data for ",len(racerA)," races.")
            print("Racer B has data for ",len(racerB)," races.")

            # Checking to see if the ammount of races that racer A has is less than the ammount that racer B has
            if len(racerA) < len(racerB):
                print("We will compare the first ",len(racerA)," races.")

                # looping through the number of lists that can be compared given the smaller number of races
                for i in range(len(racerA)):
                    if racerA[i] < racerB[i]:
                        print("racer A has won race #" + str(i+1))
                    elif racerA[i] > racerB[i]:
                        print("racer B has won race #" + str(i+1))
                    else: 
                        print("The racers tie race #" + str(i+1))
            else:
                print("We will compare the first ",len(racerB)," races.")

                for i in range(len(racerB)):
                    if racerB[i] < racerA[i]:
                        print("racer B has won race #" + str(i+1))
                    elif racerB[i] > racerA[i]:
                        print("racer A has won race #" + str(i+1))
                    else:
                        print("The racers tie race #" + str(i+1))
        else:
            # This code down here is ran if the length of the races is the same and not different
            print("We will compare the ",len(racerA)," races")

            # since the length of the lists is the same it does not matter if len(racerA) or len(racerB) is used
            for i in range(len(racerA)):
                if racerA[i] < racerB[i]:
                    print("racer A has won race # " + str(i+1))
                elif racerA[i] > racerB[i]:
                    print("racer B has won race # " + str(i+1))
                else:
                    print("The racers tie race # " + str(i+1))
    else:
        print("At least one racer has no times!")

# Defining the delete time variable and passing 2 lists in the parameters
def delete_time(racerA, racerB):
    racer = input("What racer is deleting a time?\n")

    # Using the same logic to know what racer is adding or deleting time
    if racer == "A":
        decision = input("Delete a time or delete a race?\n")
        if decision == "time":
            time = float(input("What time should be deleted?\n"))
            # Checking to see if the time that should be deleted is in the list if it is it is removed
            if time in racerA:
                # remove is used instead of pop because we are removing by a value instead of a index
                racerA.remove(time)
            # if the time is not in the list the code below is printed out
            else:
                print("Time is not in list")
        elif decision == "race":
            race = int(input("What race should be deleted?\n"))
            # Since here we are removing by race we use pop since the race is an index value, i use -1 since if they want to remove the 1st race they want to remove the 0th index
            racerA.pop(race-1)
        else:
            print("Could not interpret deletion. Please use time or race.")
    # Same logic for racer A but for racer B
    elif racer == "B":
        decision = input("Delete a time or a race?\n")
        if decision == "time":
            time = float(input("What time should be deleted?\n"))
            if time in racerB:
                racerB.remove(time)
            else:
                print("Time is not in list")
        elif decision == "race":
            race = int(input("What race should be deleted?\n"))
            racerB.pop(race-1)
        else:
            print("Could not interpret deletion. Please use time or race.")
    else:
        print("Could not interpret racer. Please use A or B.")

# defining the add time function and passing 2 lists as the parameters
def add_time(racerA, racerB):
    # asking the user what racer is adding time
    racer = input("What racer is adding time?\n")

    # Logic for what racer is adding time, once the racer is known the time is asked and then appended to the list 
    if racer == "A":
        time = float(input("What is the time to be added?\n"))
        racerA.append(time)
    elif racer == "B":
        time = float(input("What is the time to be added?\n"))
        racerB.append(time)
    else:
        print("Could not interpret racer. Please use A or B.")

# Defining the menu function
def menu():

    print("What would you like to do?")
    print("1 - Add a time")
    print("2 - Delete a time")
    print("3 - Compare times")
    print("4 - Check qualifiers")
    print("5 - Quit")

    # Setting decision as a int variable and then returning it so that the main function can know what function to execute
    decision = int(input("\n"))
    return decision

# Defining the main function
def main():
    # Creating the 3 different lists
    racerA = []
    racerB = []
    qualifiers = []

    # The code below prompts the user to enter in the times for the different racers and then appends their time to their own list
    print("Enter times for Racer A:")
    for i in range(3):
        time = float(input("Race #" + str(i+1) + ": "))
        racerA.append(time)
    print()

    print("Enter times for Racer B:")
    for i in range(3):
        time = float(input("Race #" + str(i+1) + ": "))
        racerB.append(time)
    print()

    print("Enter times for the qualifiers: ")
    for i in range(3):
        time = float(input("Race #" + str(i+1) + ": "))
        qualifiers.append(time)
    print()

    # Calling the menu function 
    choice = menu()

    # if choice is equal to 5 the program ends otherwise it will run the other functions
    while (choice != 5):
        if choice == 1:
            add_time(racerA, racerB)
        elif choice == 2:
            delete_time(racerA, racerB)
        elif choice == 3:
            compare_times(racerA, racerB)
        elif choice == 4:
            check_qualifiers(racerA, racerB, qualifiers)
        else:
            print("That was not a valid option\n") 
        # This print statement is for formatting
        print()     
        # Looping through the menu again once a choice is completed
        choice = menu()

main()
