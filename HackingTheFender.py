import csv
import json

print("1st step: Read csv file")
print("--------------------------------------------")
with open("passwords.csv") as password_file:
  print (password_file.read())
print("--------------------------------------------")
print("Alternative 1: split username and password in different file")
print("2nd step: Transfer the csv file data to own dictinary and list")
print("--------------------------------------------")
compromised_user = []
compromised_password = []
with open("passwords.csv") as password_file:
  password_csv = csv.DictReader(password_file, delimiter=",")
  for password_row in password_csv:
    compromised_user.append(password_row["Username"])
    compromised_password.append(password_row["Password"])
print ("This is Username list: \n",compromised_user)  
print ("\nThis is Password list: \n",compromised_password)  
print("--------------------------------------------")
print("3rd step: Write username the result to new txt file")
print("--------------------------------------------")
with open("compromised_users.txt", "w") as compromised_user_file:
  for username_row in compromised_user:
    compromised_user_file.write("Username = ["+username_row+"]\n")
with open("compromised_users.txt") as compromised_user_file:
  print(compromised_user_file.read())
print("--------------------------------------------")
print("4th step: Write password the result to new txt file")
print("--------------------------------------------")
with open("compromised_password.txt", "w") as compromised_password_file:
  for password_row in compromised_password:
    compromised_password_file.write("Password = ["+password_row+"]\n")
with open("compromised_password.txt") as compromised_password_file:
  print(compromised_password_file.read())
print("--------------------------------------------")
print("Alternative 2: put username and password in same file")
print("2nd step: Transfer the csv file data to own dictinary and list")
print("--------------------------------------------") 
compromised_user_and_password = {}
with open("passwords.csv") as password_file:
  password_csv = csv.DictReader(password_file, delimiter=",")
  for password_row in password_csv:
    compromised_user_and_password[password_row["Username"]]=password_row["Password"]
print("Dictinary Username and Password: \n", compromised_user_and_password)
#for username,password in compromised_user_and_password.items():
#  print ("This is username : [{username}] \nPassword : [{password}] \n".format(username = username, password= password))    
print("--------------------------------------------")
print("3rd step: Write username and password the result to new txt file")
print("--------------------------------------------")
with open("compromised_users_password.txt", "w") as compromised_user_and_password_file:
  for username, password in compromised_user_and_password.items():
    compromised_user_and_password_file.write("Username = ["+username+"]\nPassword = ["+password+"]\n\n")
    
with open("compromised_users_password.txt") as compromised_user_and_password_file:
  print(compromised_user_and_password_file.read())
print("--------------------------------------------")
print("--------------------------------------------")
print("5th step: Notifying The Boss")
print("--------------------------------------------")
with open("boss_message.json","w") as boss_message:
  boss_message_dict = {
    "Recipient":"The Boss", 
    "Message":"Mission Success"
  }
  json.dump(boss_message_dict, boss_message)
  
with open("boss_message.json") as boss_message:
   print(json.load(boss_message))
print("--------------------------------------------")
print("6th step: Scramble the Password")
print("--------------------------------------------")
with open("new_password.csv","w") as new_password_obj:
  slash_null_sig = """
   _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
  """
  new_password_obj.write(slash_null_sig)

with open("new_password.csv") as new_password_obj: 
  print(new_password_obj.read())
  


















    
