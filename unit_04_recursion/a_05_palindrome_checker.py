def check_is_palindrome(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and check_is_palindrome(s[1:-1])

print(check_is_palindrome('kayak'))
print(check_is_palindrome('some'))