'''A python program that calculates the area of specified polygon'''

print("Wlecome to area calculator")
print("---------------------------")
print("---------------------------")
print("\n")
print("Select your polygon\n Press 1 for square\n 2 for rectangle\n 3 for triangle\n 4 for circle")

def calc_area():
    user_inp = input("Enter your polygon choice: ")

    if user_inp == "1":
        square_side = int(input("Enter the measurement of square's side: "))
        area = square_side**2
        return f'The area of the polygon is {area}'

    elif user_inp == "2":
        rectangle_length = int(input("Enter the length of rectangle: "))
        rectangle_width = int(input("Enter the width of rectangle: "))
        area = rectangle_length*rectangle_width
        return f'The area of the polygon is {area}'

    elif user_inp == "3":
        triangle_height = int(input("Enter the height of triangle: "))
        triangle_base_length = int(input("Enter the base_length of triangle: "))
        area = 0.5*triangle_height*triangle_base_length
        return f'The area of the polygon is {area}'
    
    else:
        circle_radius = int(input("Enter the radius of circle: "))
        area = 3.14*(circle_radius**2)
        return f'The area of the polygon is {area}'

print(calc_area())