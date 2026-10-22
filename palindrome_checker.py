
from collections import deque


def check_palindrome(text):
    # Ignore spaces, punctuation, and letter case
    cleaned = ''.join(
        char.lower() for char in text if char.isalnum()
    )

    stack = []
    queue = deque()

    # Insert each character into both structures
    for char in cleaned:
        stack.append(char)
        queue.append(char)

    # Compare characters in reverse and forward order
    while stack:
        stack_char = stack.pop()
        queue_char = queue.popleft()

        if stack_char != queue_char:
            return False

    return True


if __name__ == "__main__":
    text = input("Enter a word or phrase: ")

    if check_palindrome(text):
        print("Result: It is a palindrome.")
    else:
        print("Result: It is not a palindrome.")
