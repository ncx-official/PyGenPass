import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['1','2','3','4','5','6','7','8','9','0',]
symbols = ['!','@','#','$','%','^','&','*','(',')','=','+','?']
print("___<Welcome to the PyPassword generator>___")
letterCount = int(input("How much letters would you like in password? (1-50) -> "))
symbolCount = int(input("How many symbols would you like? (1-13) -> "))
numberCount = int(input("How many numbers would you like? (1-10) -> "))

new_list = [] # list for chose letters symbols and numbers
password = "" # string of password
for n in range(1,letterCount + 1): # loop for letters
  new_list.append(random.choice(letters)) # add every random letter to new_list
for n in range(1,symbolCount + 1): # loop for symbols
  new_list.append(random.choice(symbols)) # add every random symbol to new_list
for n in range(1,numberCount + 1): # loop for numbers
  new_list.append(random.choice(numbers)) # add every random number to new_list 
for n in range(1, len(new_list)+1): # Loop for adding symbol to string and deleting from list (new_list) 
  random_thing = random.choice(new_list) 
  password += random_thing
  new_list.remove(random_thing)
print(f"Your password is -  {password}") # Your password
input("Press Enter to exit")


# separate definition of letters or symbols or numbers ↓↓↓
# password - 4 letter, 2 symbol, 2 number = JduE &! 91
""" 
string, string1, string2  = "", "", ""
for n in range(1,letterCount):
  string += random.choice(letters)
print(string)
for n in range(1,symbolCount):
  string1 += random.choice(symbols)
print(string1)
for n in range(1,numberCount):
  string2 += random.choice(numbers)
print(string2)
print(f"All password: {string + string1 + string2}")
"""
# © NCX_corp 22.12.2020
