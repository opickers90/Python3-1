def username_generator(first_name, last_name):
  username = first_name[:3]+last_name[:4]
  return username
  
def  password_generator(username):
  password = ""
  for char in range(0, len(username),1):
    password += username[char-1]
  return password

abeuser = username_generator("Abe", "Simpson")
jauser = username_generator("Ja", "Snail")

abepass = password_generator(abeuser)
japass = password_generator(jauser)

print("Username for Mr. Simpon is :",abeuser)
print("Password is",abepass)
print("Username for Mr. Snail is :",jauser)
print("Password is",japass)
