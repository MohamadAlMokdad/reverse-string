# 📥 Reverse String

This Python script implements a simple recursive function to reverse a string. The function builds the reversed string by taking the last character of the string and appending it to the reversed substring.

## 📜 Function: `reverse_string`

### 📝 Description
The `reverse_string` function recursively reverses the input string. It takes the last character and appends it to the reversed substring of the remaining string, until it reaches the base case where the string is empty or has one character.

# Sample string
s = "hello"

# Reverse the string using the function
reversed_string = reverse_string(s)

# Expected output
print("Reversed string:", reversed_string)
#output=olleh
