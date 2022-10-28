# Store the months of the year as strings. Determine the month in the data structure in which National Pi Day exists and print that month to the console. 
# HINT: The number for Pi, when converted to an Integer, is related to the stored location of the correct month.

months_in_year = ('January', 'February', 'March', 'April',' May', 'June', 'July',' August',' September',' October', 'November', 'December')

print('National Pi day is celebrated on the 14th of '+ months_in_year[2])



# Store five fruits or vegetables.
# Add two of your favorite fruits and two of your favorite vegetables to the collection.
# Iterate over the collection and print each one to the console. 



fruits_list = {'apples', 'pear', 'orange', 'banana', 'grape'}
my_list = {'coconut', 'mango'}

def iterate_list():
    new_list = fruits_list.union(my_list)
    print(new_list)
    for x in new_list:
        print(x)

second_task = iterate_list()






# Store information about a user profile. Use literal string interpolation to print the user’s profile information to the console. The profile should consist of the following information:
# First Name
# Last Name
# Email Address
# Phone Number

player = {
    "first_name" : "Sean",
    "last_name" : "Boateng",
    "email address" : "seanboateng2@gmail.com",
    "Phone Number" : "646-917-1718"
}

def inter_polation():
    for key, value in player.items():
        print("")
        print(f"The Key {key} has a value of {value}")
        print("")


third_task = inter_polation()   





# Task 2: List of Dictionaries
# Use a list to store the dictionary of your immediate family members, with each index of the list storing its own dictionary. 
# Dictionary should contain the following keys:
# First name
# Last name
# Relation to you

# Once you have stored the List of Dictionary items,
#  write a function/method that will iterate over the List and print off the First Name and Relation of each person in the List.



mom = {
    "first_name" : "Gifty",
    "last_name" : "Gyamfi",
    "relation" : "Mother"    
}
dad = {
    "first_name" : "Sam",
    "last_name" : "Boateng",
    "relation" : "Father"
}
sis = {
    "first_name" : "Sybil",
    "last_name" : "Boateng",
    "relation" : "Sister"
}
 
def task2():
    print(mom["first_name"])
    print(mom["relation"])
    print(dad["first_name"])
    print(dad["relation"])
    print(sis["first_name"])
    print(sis["relation"])


last_task = task2()
























