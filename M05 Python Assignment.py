#This program will ask the user for 15 numbers and will determine which are even or odd

numbers = []
count = 0

while count < 15:
    numbers.append(int(input("Enter a number:")))
    count = count + 1

count = 0
while count < 15:
    if(numbers[count] %2 == 0):
        print(numbers[count]," is even")

    else:
        print(numbers[count]," is odd")
    count = count + 1
