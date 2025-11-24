password = "12345" # make a variable to store the password
attempt = 0 # make a variable for the count of attempts
max_attempts = 5 # set a maximum number of attempts
while attempt < max_attempts: # make a while loop to run until attempts is eaqual to max attempts
    user_input = input("Enter the password: ") # add a variable to store user input
    if user_input == password: # if user input is the same as password it will print access granted
        print("Access granted.")
        break
    else:
        attempt += 1 # make the attempt vairable increase by 1 if the password is wrong
        print(f"Incorrect. Enter the right password {max_attempts - attempt} attempts left.") # if its wrong it will print incorrect and how many attempts are left
        if attempt == max_attempts: # make an if statement to see if attempts is eaqual to max attempts
            print("You have reached the maximum attempts. locked out of access.") # if it is it will print locked out of access