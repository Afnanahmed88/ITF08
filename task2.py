name = input("Enter your fullname: ")
mobile_no = input("Enter your mobile number (in this format 05x-xxxx-xxx): ")
year_of_birth = int(input("Enter your year of birth: "))
current_year = 2023
age = current_year - year_of_birth
mobile__no = mobile_no.split("-")
print(name)
print(age)
print(mobile__no)
