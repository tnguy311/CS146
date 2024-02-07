public class CheckPalindrome {
    public static void CheckPalindrome(String s) {
        // Convert the input string to lowercase
        String lowercaseString = s.toLowerCase();
        
        // Remove all non-alphanumeric characters from the string
        StringBuilder alphanumericString = new StringBuilder();
        for (char c : lowercaseString.toCharArray()) {
            if (Character.isLetterOrDigit(c)) {
                alphanumericString.append(c);
            }
        }
        
        // Check if string is a palindrome
        boolean palindromeCheck = alphanumericString.toString().equals(alphanumericString.reverse().toString());
        
        // Print the result
        if (palindromeCheck) {
            System.out.println("Is the string a palindrome? Yes.");
        } else {
            System.out.println("Is the string a palindrome? No.");
        }
    }

    public static void main(String[] args) {
        String inputString = "A man, a plan, a canal: Panama";
        isPalindrome(inputString);
    }
}

