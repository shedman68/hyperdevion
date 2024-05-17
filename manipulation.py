stri_manip = input("Enter a sentence: ") #Ask the user to enter a sentence using the input() method. Save the user’s response in a variable called str_manip
print(len(stri_manip)) # Calculate and display the length of str_manip
last_stri_manip = stri_manip[-1] # Find the last letter in str_manip sentence
print(last_stri_manip) # Print this last letter
rep_word = stri_manip.replace(last_stri_manip,"@") # replace this last letter with @
print(rep_word) # print this last letter
last_three_charac = stri_manip[-1:-4:-1]
print(last_three_charac) # Print the last 3 characters in str_manip backwards
first_three = stri_manip[0:3] # first three charac
print(first_three)
last_two = stri_manip[-2:] # last two charac
print(last_two)
five_charac = first_three + last_two #combine first three and last two
print(five_charac)



