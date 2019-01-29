#Write your function here
def add_greetings(names):
  greet = []
  for name in names:
    hello = ("Hello, {0}".format(name))
    greet.append(hello)
  return greet  

#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))
