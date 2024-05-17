# Read in the times for swimming, cycling, and running
swim_time = float(input("Enter the time (in minutes) for swimming: "))
cycle_time = float(input("Enter the time (in minutes) for cycling: "))
run_time = float(input("Enter the time (in minutes) for running: "))

# Calculate the total time taken to complete the triathlon
total_time = swim_time + cycle_time + run_time

# Determine the award based on the total time taken
if total_time <= 100:
    print("Well done! You have won the Provincial Colours")
elif total_time <= 105:
    print("Well done! You have won the Provincial Half Colours")
elif total_time <= 110:
    print("Bravo! You have won the Provincial Scroll")
else:
    print("Better luck next time!")

