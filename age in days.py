name = input ("what is your name?")
age = input ("how old are you?")
age = int(11)
your_age = input ("you are " + str( int(age) * 365) + " days old")

password = input ("what is the password?").strip().lower()
if name == "25593":
    print ("awsome!")
else:
    print("DENIED! intruder found.")
    exit()
print (" hello there " + name)
print (" you are " + name + " and you are " + age + " years old")

