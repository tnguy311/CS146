def is_palindrome(s):
    # Convert the input string to lowercase
    lowercase_string = s.lower()
    
    # Remove all non-alphanumeric characters from the string
    alphanumeric_string = ''.join(char for char in lowercase_string if char.isalnum())
    
    # Check if the modified string is a palindrome
    return alphanumeric_string == alphanumeric_string[::-1]

# Testing function
input_string = "A man, a plan, a canal: Panama"
is_palindrome_result = is_palindrome(input_string)
print("Is the string a palindrome?", is_palindrome_result)
