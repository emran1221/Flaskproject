import math

print("ronahiosama")

def calculate_circle_area(radius):
    return math.pi * radius * 2

def main():
    print("Welcome  the  Calculator!")
    try:
        radius = float(input("Enter the pashbesh of  : "))
        if radius < 0:
            print(" cannot be negative.")
        else:
            area = calculate_circle_area(radius)
            print(f"The area of  circle  radius {radius} is {area:.2f}")
    except ValueError:
        print("Invalid input. Plllease enter a valid .")

if __name__ == "__main__":
    main()
