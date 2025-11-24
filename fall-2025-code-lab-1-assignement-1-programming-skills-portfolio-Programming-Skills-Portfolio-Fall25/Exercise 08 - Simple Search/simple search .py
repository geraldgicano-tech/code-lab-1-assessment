list = ["Jake" "Zac", "Ian", "Ron", "Sam", "Dave"] # make the list of names
def simple_search(name, list): # make a function that takes in a name and a list
    for i in range(len(list)): # make a for loop that goes through the length of the list
        if list[i] == name: # add an if statement to check if the name is in the list
            return i # return the index of the name if found
    return -1 # return -1 if the name is not found
name = input("Enter a name to search for: ").capitalize() # get user input for the name to search
index = simple_search(name, list) # call the function and store the result in index
if index != -1: # check if the index is not -1
    print(f"{name} found at index {index}.") # print the name and index if found
else:
    print(f"{name} not found in the list.") # print that the name is not found
