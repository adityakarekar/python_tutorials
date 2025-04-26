a="AdityaKarekar123"
b="  "
print(a.lower())
print(a.upper())
print(a.rstrip("!"))    # removes the trailing characters
print(a.lstrip("!")) # removes the leading characters
print(a.replace("Aditya","ADITYA"))  # replaces the string with the new string
print(a.split(" ")) # splits the string into a list of strings
print(a.capitalize()) # capitalizes the first letter of the string
print(a.count("a")) # counts the number of occurrences of a character in the string
print(a.endswith("!")) # checks if the string ends with a character
print(a.endswith("ya",4,7)) # checks if the string ends with a character in the given range
print(a.find("a")) # finds the first occurrence of a character in the string
print(a.index("a")) # finds the first occurrence of a character in the string in the given range
print(a.isalnum()) # checks if the string is alphanumeric
print(a.isalpha()) # checks if the string is alphabetic
print(b.isspace()) # checks if the string is whitespace characters