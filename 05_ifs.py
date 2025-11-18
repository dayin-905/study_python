# if condition:
#     executed code
# elif condition2:
#     executed code
# else:
#     executed code  

first = 4

if first >= 5 :
    print("Welcome!")
    print("It's me.")

second = 6

first = int(input("input first number : "))
second = int(input("input second number : "))

if first >= second :
    print("Welcome!")
    print("It's me.")


print("End of program.")

## 다중 if-elif-else 예제
age = int(input("input your age : "))
if age < 4 :
    print("Your ticket is free!")
elif age < 18 :
    print("Your ticket is $5.")
else:
    print("Your ticket is $10.")

print("End of program.")

pass
fourth = "welcome to python!"
forth_world = "python"
if fourth in forth_world :
    print("Yes! 'python' is here.")