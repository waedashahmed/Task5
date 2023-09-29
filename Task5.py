name= input('Enter your name:')
age= input('Enter your age:')
street= input('Enter the street:')
city= input('Enter the city:')
country= input('Enter the country:')
print(f'"Name: {name}"')
print(f'"Age: {age}"')
print(f'"Adress: {street}, {city}, {country}"')
print(f'"Hello {{{name}}} Your age is {age} Years old, Your Adress is {street}, {city}, {country}."')
print(type(name), type(age))
print(type(street), type(city))
print(type(country))
print(f'"Hello {name}, How Are You? \\ """ Your Age Is "{age}"" + And Your country Is: {country}"')
print(f'"Hello {name}, How Are You? \\\n """ Your Age Is "{age}"" + And\n Your city Is: {city}"')
name= 'ITF Gsg Python'
print(f'First Letter Is "{name[0]}"')
print(f'Third Letter Is "{name[2]}"')
print(f'Last Letter Is "{name[-1]}"')
print(name[11:14])
print(name[0:3])
print(name[0:7:2])
print(name[-1:-7:-1])
name = "$&$&Mohammed$&$&"
print(name.strip("$&$&"))
msg= "I %7 Python And Although I %7 GSG with Zakaria"
print(msg.replace("%7","Love"))
num1= "4"
num2= "56"
num3= "963"
num4= "385"
num5= "8719"
num6= "87190"
print(num1.zfill(5))
print(num2.zfill(5))
print(num3.zfill(5))
print(num4.zfill(5))
# print(num5.zfill(5))
print(num6.zfill(5))
str1='hello world'
print(str1.title())
print(str1.capitalize())
first_name = "ًWaed"
print("***********" + first_name)
print("***********" + first_name + "***********")
print(first_name + "***********")
name_one= 'SaMER'
name_two= 'Abed'
print(name_one.swapcase())
print(name_two.swapcase())
print(name_one.lower())
print(name_two.upper())
print(name_one.isupper())
print(name_two.islower())
if name_one.startswith('S'):
    print("name_one starts with 'S'")
else:
    print("name_one does not start with 'S'")
if name_two.endswith('HD'):
    print("name_two ends with 'HD'")
else:
    print("name_two does not end with 'HD'")
msg = "I Love Python And Although I Love GSG with Zakaria"
print(f'Number of <Love> is {msg.lower().count("love")}')
print(f'Number of <t> is {msg.lower().count("t")}')
msg = "I %7 Python And Although I %7 GSG with Zakaria"
print(msg.replace("%7", "Love", 1))
