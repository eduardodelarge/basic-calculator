def add(a, b):
	ret = a + b
	print(str(a) + " + " + str(b) + " = " + str(ret))

def sub(a, b):
	ret = a + b
	print(str(a) + " - " + str(b) + " = " + str (ret))

def div(a, b):
	ret = a + b
	print(str(a) + " / " + str(b) + " = " + str (ret))

def mult(a, b):
	ret = a + b
	print(str(a) + " * " + str(b) + " = " + str (ret))

print("a. Addtion")
print("b. Subtraction")
print("c. Multiplication")
print("d. Division")
print("e. Exit")

choice = input("What operation you need? ")

if choice == "a" or choice == "A":
    print("Addition")
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    add(a, b)
elif choice == "b" or choice == "B":
    print("Subtraction")
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    sub(a, b)
elif choice == "c" or choice == "C":
    print("Division")
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    div(a, b)
elif choice == "d" or choice == "D":
    print("Multiplication")
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    mult(a, b)
elif choice == "e" or choice == "E":
    print("Exiting")
    quit()