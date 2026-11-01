
def showOptions():
    print("Options:\n1 - Show count\n2 - Increase count\n3 - Reset count\n0 - Exit")
    return None

def askChoice():
    choice = input("Your choice: ")
    if choice.isnumeric():
        return int(choice)
    else:
        return -1

def main():
    count = 0
    showOptions()
    choice = askChoice()

    while choice != 0:
        if choice == 1:
            print(f"Current count - {count}")
        elif choice == 2:
            count += 1
            print("Count increased!")
        elif choice == 3:
            count = 0
            print("Cleared count!")
        else:
            print("Unknown option! try again.")

        print()
        showOptions()
        choice = askChoice()

    print("Exiting program.")

print("Program starting.")
main()
print("Program ending.")
