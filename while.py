numbers = [] # empty list to store the numbers entered by the user
while True: # start of loop that asks user to enter a number continually 
    num = int(input("Enter a number: "))
    if num == -1: # If the user enters -1, break out of the loop
        break
    numbers.append(num) # Add the number entered by the user to the end of the numbers list

if len(numbers) == 0: # Check if any numbers were entered
    print("No numbers entered.") # If no numbers were entered, print a message saying 
else:
    average = sum(numbers) / len(numbers) # Calculate the average of the numbers entered (excluding -1)
    print("Average of the numbers entered (excluding -1):", average)