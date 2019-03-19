import json
import termcolor

# -- Open the json file
f = open("exercise1.json", 'r')

# Read the data from the file
# Now person is a dictionary with all the information
person1 = json.load(f)
print ("Total people in database:",(len(person1["Number of people"])))

for  person in person1["Number of people"]:

# Print the information of the object
    print()
    termcolor.cprint("Name: ", 'green', end="")
    print (person['Firstname'], person['Lastname'])
    termcolor.cprint("Age: ", 'green', end="")
    print(person['age'])

    for s,num in enumerate(person["phoneNumber"]):
        termcolor.cprint(" Phone  {}:".format(s+1), "blue")

        termcolor.cprint("   Type:", "red", end= "")
        print(num['type'])
        termcolor.cprint("   Number:", "red", end= "")
        print(num['number'])
