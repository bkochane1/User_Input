employee_id = input("Please enter an employee ID: ") # set employe id as input

try: # if there is an error( employee id is 7 or less digit long) inside the try then go to the exept
    int(employee_id)
    if len(employee_id) > 7:    
        exit()
except:
    exit() # if information eneter incorrectly terminate 


invalid_characters_name = ["!", '"', "@", "#",'$','%','^', '&', '*',"(", ")","_",'+','=',',', '<', '>', '/', '?', ';', ':', '[', ']', '{', '}', '\\'] # name cannot contain these characters


employee_name = input("Please enter an employee name: ") # 

for letter in employee_name: # loop through all the letters in the employees name 
    for invalid_char in invalid_characters_name:
        if letter == invalid_char: # if the letters in the employees names match any invalid then exit
            exit()

invalid_characters_email = ["!", '"', "'", "#",'$','%','^', '&', '*',"(", ")", '+','=',',', '<', '>', '/', '?', ';', ':', '[', ']', '{', '}', '\\']

employee_email = input("Please enter an employee email: ")

for letter in employee_email: # loop through all the letters in the employee email
    for invalid_char in invalid_characters_email:
        if letter == invalid_char: #if the letters in the employees names match any invalid then exit
            exit()

invalid_characters_address = ["!", '"', "'", "@", '$','%','^', '&', '*',"_",'+','=', '<', '>', '?', ';', ':', '[', ']', '{', '}', '\\'] # invalid characters in address

employee_address = input("Please enter an employee address: ") 

for letter in employee_address: # loop through all the letters in the employee address
    for invalid_char in invalid_characters_address:
        if letter == invalid_char: ##if the letters in the employees names match any invalid then exit
            exit()

print("Hello, " + employee_name + ". Your Employee ID is " + employee_id + ", and your email address is " + employee_email + ". ")

if len(employee_address) == 0: # if employees don't provides address print message
    print("You did not provide an address.")
else:
    print("Your address is " + employee_address) # if employee provides address print message
