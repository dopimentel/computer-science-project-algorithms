def is_palindrome_recursive(word, low_index, high_index):
    """Check if a word is a palindrome using recursion."""
    if not word:
        return False
    if low_index >= high_index:
        return True
    if word[low_index] != word[high_index]:
        return False
    return is_palindrome_recursive(word, low_index + 1, high_index - 1)


if __name__ == "__main__":
    print(is_palindrome_recursive("ANA", 0, 2))
    print(is_palindrome_recursive("AGUA", 0, 3))
    print(is_palindrome_recursive("SOCOS", 0, 4))
    print(is_palindrome_recursive("REVIVER", 0, 6))
    print(is_palindrome_recursive("I", 0, 0))
