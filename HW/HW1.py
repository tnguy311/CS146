def is_palindrome(s):
    # Convert the string to lowercase
    lowercase_string = s.lower()
    
    # Remove all non-alphanumeric characters in the string
    alphanumeric_string = ''.join(char for char in lowercase_string if char.isalnum())
    
    # Check if string is a palindrome
    palindrome_check = alphanumeric_string == alphanumeric_string[::-1]
    
    # Print the result
    if palindrome_check:
        print("Is the string a palindrome? Yes.")
    else:
        print("Is the string a palindrome? No.")

# Test the function
input_string = "A man, a plan, a canal: Panama"
is_palindrome(input_string)

