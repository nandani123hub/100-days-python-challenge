name = "Nandani"
print("Hello", name)
print('Hi, "I want to learn python properly"')
a = """Hi,
I am Nandani,
I am learning python."""
print(a)

#print the words of string
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])

#print all the words of string using for loop
for newa in a:
    print(newa)


#check string length
print(len(name))

#To check if a certain phrase or character is present in a string
txt = "The best things in life are free!"
print("free" in txt)


#Use it in an if statement:
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")


#To check if a certain phrase or character is NOT present in a string
txt = "The best things in life are free!"
print("expensive" not in txt)


#Use it in an if statement:
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")