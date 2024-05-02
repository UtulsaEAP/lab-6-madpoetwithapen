def check_palindrome(user_input):

    cleaned_input = ''.join(char.lower() for char in user_input if char.isalnum())

    if cleaned_input == cleaned_input[::-1]:
        print(f"palindrome:{user_input}")

    else:
        print(f"not a palindrome:{user_input}")




 #type your code here
if __name__ == "__main__":
    user_input = input("Enter a word or phrase: ")
    check_palindrome(user_input)
