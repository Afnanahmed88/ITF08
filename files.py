user_name = input("Enter your name: ")
age = input("Enter your age: ")
dob = input("Enter your date of birth: ")

user_info = {
    "User Name": user_name,
    "Age": age,
    "Date of Birth": dob
}

file_name = "user_info.txt"
with open(file_name, "w") as file:
    # Write each key-value pair from the dictionary to the file
    for key, value in user_info.items():
        file.write(f"{key}: {value}\n")

print("User information has been written to", file_name)
