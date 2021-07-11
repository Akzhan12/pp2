def isPalindrome(s):
    if s == s[::-1]:
        return 'String is a palindrome'
    else:
        return 'String is not a palindrome'
s = input()
print(isPalindrome(s))