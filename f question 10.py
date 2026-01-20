def palindrome(s):
    s = s.replace(" ", "").lower()  
    return s == s[::-1]
print(palindrome("A man a plan a canal Panama"))
