def reverse_string(s):
    # Base case: if the string is empty or has one character, return it
    if len(s) <= 1:
        return s
    # Recursive case: last character + reverse of the rest
    else:
        return s[-1] + reverse_string(s[:-1])

# Test the function
print(reverse_string("hello"))  # Output should be "olleh"
