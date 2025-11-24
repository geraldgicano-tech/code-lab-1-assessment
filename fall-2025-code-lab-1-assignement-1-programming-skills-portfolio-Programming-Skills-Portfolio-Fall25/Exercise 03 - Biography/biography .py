full_name = input("what is your your full name: ")
hometown = input("where is your hometown: ")
age = input("how old are you: ")
    # adding values to the variables above with user input
biography = { # making a dictionary to store the biography information
    "Full Name": full_name,
    "Hometown": hometown,
    "Age": age
    }
    # printing each variable with a description on separate lines using key and value
for key, value in biography.items():
    print(f"{key}: {value}")
