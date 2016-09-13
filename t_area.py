# Introduce yourself
name = input('Enter your name: ')
print('Hello', name)

# Define our variables, starting with the base measurement

x = float(input("Please enter the numerical value of the base of the triangle:"))

# Make sure a negative number isn't given

if x < 0:
    print('base cannot be less than 0')

# Same thing, but now the height
    
y = float(input("Please enter the numerical value of the height of the triangle:"))

if y < 0:
    print('height cannot be less than 0')

# Now have the previous notes equal our area

a = (x * y )* 0.5

print('The area of the triangle is' ,a)
