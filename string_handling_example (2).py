def alternate_case(input_str):
  result = ''
  for i, char in enumerate(input_str):
      if i % 2 == 0:
          result += char.upper()
      else:
          result += char.lower()
  return result

# Read input string from the user
user_input = input("Enter a string: ")

# Apply alternate case transformation
result_string = alternate_case(user_input)

# Print the result
print("Original String (1): ", user_input)
print("Alternate Case String (1): ", result_string)


def alternate_case_words(input_str):
  words = input_str.split()  # Split the string into a list of words
  result_words = []

  for i, word in enumerate(words):
      if i % 2 == 0:
          result_words.append(word.lower())
      else:
          result_words.append(word.upper())

  result_str = ' '.join(result_words)  # Join the modified words back into a string
  return result_str

# Example usage
input_string = input("Enter a new string: ")
result_string = alternate_case_words(input_string)
print("Original String (2): ", input_string)
print("Alternate Case String (2): ", result_string)
