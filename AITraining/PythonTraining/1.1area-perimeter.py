
#Rectangle
length = float(input("Enter length : "))
breadth = float(input("Enter breadth : "))

a_rec = length * breadth;
a_per = 2 * (length + breadth);

print(f"Area of rec is : {a_rec}")
print(f"Perimeter of rec is : {a_per}")


# Square
side = float(input("\nEnter side of square : "))

a_sq = side * side
p_sq = 4 * side

print(f"Area of square is : {a_sq}")
print(f"Perimeter of square is : {p_sq}")

# Circle
radius = float(input("\nEnter radius of circle : "))

a_cir = 3.14 * radius * radius
p_cir = 2 * 3.14 * radius

print(f"Area of circle is : {a_cir}")
print(f"Perimeter of circle is : {p_cir}")

# Rhombus
d1 = float(input("\nEnter first diagonal : "))
d2 = float(input("Enter second diagonal : "))
side = float(input("Enter side of rhombus : "))

a_rho = (d1 * d2) / 2
p_rho = 4 * side

print(f"Area of rhombus is : {a_rho}")
print(f"Perimeter of rhombus is : {p_rho}")