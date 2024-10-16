def is_palindrome(value):
    # Convert to string and compare with its reverse
    return str(value) == str(value)[::-1]

# Example usage
if __name__ == "__main__":
    user_input = input("Enter a word or number: ")
    if is_palindrome(user_input):
        print(f"'{user_input}' is a palindrome!")
    else:
        print(f"'{user_input}' is not a palindrome.")
