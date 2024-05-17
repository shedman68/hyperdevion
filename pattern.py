star = "*"
# Set the maximum number of stars to print in a row
max_stars = 5

# Loop through each row of stars
for i in range(1, max_stars * 2):
    # Calculate the number of stars to print in this row
    if i <= max_stars:
        num_stars = i
    else:
        num_stars = max_stars * 2 - i

    # Print the stars for this row
    for j in range(num_stars):
        print("*", end="")
    print()
