public class CheckPalindrome {
    public static void isPalindrome(String s) {
        // Convert input string to lowercase
        String lowercaseString = s.toLowerCase();
        
        // Remove non-alphanumeric
        StringBuilder alphanumericString = new StringBuilder();
        for (char c : lowercaseString.toCharArray()) {
            if (Character.isLetterOrDigit(c)) {
                alphanumericString.append(c);
            }
        }
        
        // Check string
        boolean palindromeCheck = alphanumericString.toString().equals(alphanumericString.reverse().toString());
        
        // Print the result
        if (palindromeCheck) {
            System.out.println("Is the string a palindrome? Yes.");
        } else {
            System.out.println("Is the string a palindrome? No.");
        }
    }

    public static void main(String[] args) {
        String inputString = "Murder for a jar of red rum.";
        isPalindrome(inputString);
    }
}

