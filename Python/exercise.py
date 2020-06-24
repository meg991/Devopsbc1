# while statment
#i = 1
#while i < 6:
#    print(i)

# ONLINE RESERCHES

# Temperature converter
temp = input("Input the  temperature you like to convert? (e.g., 45F, 102C etc.) : ")
degree = int(temp[:-1])
i_convention = temp[-1]

if i_convention.upper() == "C":
  result = int(round((9 * degree) / 5 + 32))
  o_convention = "Fahrenheit"
elif i_convention.upper() == "F":
  result = int(round((degree - 32) * 5 / 9))
  o_convention = "Celsius"
else:
  print("Input proper convention.")
  quit()
print("The temperature in", o_convention, "is", result, "degrees.")

# BMI calculater
# getting input from the user and assigning it to user

height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kg: "))

# the formula for calculating BMI

bmi = weight/(height**2)
# ** is the power of operator i.e height*height in this case

print("Your BMI is: {0} and you are: ".format(bmi), end='')

#conditions
if ( bmi < 16):
   print("severely underweight")

elif ( bmi >= 16 and bmi < 18.5):
   print("underweight")

elif ( bmi >= 18.5 and bmi < 25):
   print("Healthy")

elif ( bmi >= 25 and bmi < 30):
   print("overweight")

elif ( bmi >=30):
   print("severely overweight")