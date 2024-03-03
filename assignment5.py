#1.Write a program to print numbers from  to 0, but stop if the number is 5.

for number in range(6):
    print(number)
    if number == 5:
        break

#2.Write a program to iterate through a list and stop when encountering a specific element.

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

stop_element = 5

for element in my_list:
    print(element)
    if element == stop_element:
        break

#3.Write a program to skip printing even numbers from  to 0.

end_number = 10

for number in range(end_number + 1):
    if number % 2 == 0:
        continue
    print(number)

#4.Write a program to print numbers from 0 to 9 using rangeXF.

def rangeXF(start, end):
    return range(start, end)

for i in rangeXF(0, 10):
    print(i)

#5.Write a program to print multiplication tables from  to 5, but stop after the first table is printed for each number

end_number = 5

    
for i in range(1, end_number + 1):
    
    print(f"Multiplication table for {i}:")
    
    
    for j in range(1, 11):
        
        print(f"{i} x {j} = {i * j}")
    

    print()
    

    break

#6.Write a program to skip printing even numbers using a while loop.


end_number = 9  

number = 0

while number <= end_number:
    if number % 2 != 0:
        print(number)
    number += 1