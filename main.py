
def showOptions():
  print("Options:\n1 - Show count\n2 - Increase count\n3 - Reset count\n0 - Exit")
  return None
def askChoice():
  choice = input("Your choice:")
  return choice
def main():
  showOptions()
  choice=askChoice()
  count=0
  while choice != "0":
    if choice == "1":
        print(count)
    elif choice == "2":
        count+=1
        print(count)
    elif choice == "3":
        count = 0
        print(count)
    else:
        print("Unknown option! try again.")
    showOptions()
    choice=askChoice()  
         
  print("Exiting program.")
print("Program starting.")
main()
print("Program Ending.")