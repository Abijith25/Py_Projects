print("\n \n PALINDROME CHECKER ")
def is_palindrome(s):
    '''
        Remove spaces and convert to lowercase for case-insensitive
        comparison
    '''
    '''
        THE REPLACE FUNCTION TWO ARGUMENTS FIRST ONE IS CHARACTER TO
        BE REPLACED AND THE NEXT ONE IS REPLACEMENT CHARACTER 
    '''
    s = s.replace(" ", "").lower()
    
    # Compare the original string with its reverse
    return s == s[::-1]

# Input from the user
user_input = input("Enter a word or phrase: ")

if is_palindrome(user_input):
    print(f"{user_input} is a palindrome!")
else:
    print(f"{user_input} is not a palindrome.")
