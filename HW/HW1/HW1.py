def palindrome(s):
    # Convert the string to lowercase
    lowercase_string = s.lower()
    
    # Remove non-alphanumeric characters 
    alphanumeric_string = ''.join(char for char in lowercase_string if char.isalnum())
    
    # Check string 
    palindrome_check = alphanumeric_string == alphanumeric_string[::-1]
    
    # Print result
    if palindrome_check:
        print("Is the string a palindrome? Yes.")
    else:
        print("Is the string a palindrome? No.")

# Test the function
input_string = "Murder for a jar of red rum."
palindrome(input_string)

