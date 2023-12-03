
# Half pyramid
num=int(input("Enter a number:"))
i=1
while i<=num:
    print(i*"*")
    i=i+1


# Inverted Half Pyaramid
num=int(input("Enter a number:"))
i=1
j=num
while i<=num:
    print(j*"*" +" "*i)
    i+=1
    j-=1

#Snow Flake
num=int(input("Enter a number:"))
i=1
j=num
while i<=num:
    print(" "*(j-1)+"*"*i)
    j-=1
    i+=1
i=num-1
j=1
while i>=1:
    print(" "*j +"*"*i)
    j+=1
    i-=1

# Fulll paramid
rows = int(input("Enter the number of rows for the pyramid: "))

for i in range(1, rows + 1):
    
    for j in range(1, rows - i + 1):
        
        print(" ", end="")
    
    for k in range(1, 2 * i):
        
        print("*", end="")
        
    # Hour Glass
    size = int(input("Enter the size of the hourglass: "))

for i in range(size):

    spaces = ' ' * i

    stars = '*' * (2 * (size - i) - 1)

    print(spaces + stars)

for i in range(size - 2, -1, -1):

    spaces = ' ' * i

    stars = '*' * (2 * (size - i) - 1)

    print(spaces + stars)

# Symmetrical Shape
def square_constellation(size):
for in range(size):
    print('* ' * size)
square_constellation(6)










    







