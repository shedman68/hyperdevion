hour = int(input("Enter the hour (0-23): "))

if hour < 18:
    greeting = "Good day"
elif hour < 20:
    greeting = "Good evening"
else:
    greeting = "Good night"

print(greeting)
