def right_angled_triangle(number_of_rows:int):#1
    for i in range(1,number_of_rows+1):
        print(i * "*")

def hollow_square(nm_rows,nm_columns):#2
    for row in range(1,nm_rows+1):
        for column in range(1,nm_columns+1):
            if row == 1 or row == nm_rows or column == 1  or column == nm_columns:
                print("*", end="")
            else:
                print(" ",end="")
        print()

def create_diamond(height):#3
    for i in range(height):
        print(" "*(height-i), "*"*(i*2+1))
    for i in range(height-2, -1, -1):
        print(" "*(height-i), "*"*(i*2+1))

def left_angled_triangle(number_of_rows):#4
    for i in range(number_of_rows ,0,-1):
        pattern = i * "*"
        print(pattern)

def create_pyramid(num):#5
    for rows in range( 0,num):
        for columns in range(0, num -rows - 1):
            print(" ", end="")
        for columns in range(0,rows +1 ):
            print("* ",end ="")
        print()

def reversed_pyramid(number):#6
    for row in range(number,0,-1):          #(5,0,-1) loop
        for column in range(0,number-row):  #(0,4) loop
            print(end=" ")                  #print 5 times " " on one line
        for column in range(0,row):         #(0,5)  loop
            print("*",end=" ")              # *****
        print()                             #new line

def rectangle(rows,columns):#7
    for row in range(1, rows + 1):
        for column in range(1, columns + 1):
            if row == 1 or row == rows or column == 1 or column == columns:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

# 🖼️ Python Pattern Drawing Project

# Step 1: Display a menu to the user
print("🌟 Welcome to the Python Pattern Drawing Program!")
print("Choose a pattern type:")
print("1. Right-angled Triangle")
print("2. Square with Hollow Center")
print("3. Diamond")
print("4. Left-angled Triangle")
print("5. Pyramid")
print("6. Reverse Pyramid")
print("7. Rectangle with Hollow Center")
print("8. Exit")

while True:
    choice = int(input("Choose number: "))
    if choice==8:
        break

    if choice ==1:
        rows = int(input("Number of rows: "))
        right_angled_triangle(rows)
    elif choice ==2:
        rows = int(input("Number of rows: "))
        columns = int(input("Number of columns:"))
        hollow_square(rows,columns)
    elif choice ==3:
        diamond_height = int(input("Height of Diamond: "))
        create_diamond(diamond_height)
    elif choice ==4:
        rows = int(input("Number of rows: "))
        left_angled_triangle(rows)
    elif choice ==5:
        height = int(input("Enter height of the pyramid: "))
        create_pyramid(height)
    elif choice ==6:
        height = int(input("Enter height of the reversed pyramid: "))
        reversed_pyramid(height)
    elif choice ==7:
        rows = int(input("Number of rows: "))
        columns = int(input("Number of columns: "))
        while rows == columns:
            print("Number of rows and columns cannot be the same")
            print("It should be a rectangle not a square")
            rows = int(input("Number of rows: "))
            columns = int(input("Number of columns: "))
        rectangle(rows,columns)


print("Program has stopped! Thank you for playing.")