def isPalindrome(string):
    if len(string) == 0:
        return True
    if string[0] != string[len(string)-1]:
        return False
    return isPalindrome(string[1:len(string) -1])

print(isPalindrome("awesome"))
print(isPalindrome("foocat"))
print(isPalindrome("tacocat"))
# print(isPalindrome("awesome"))
# print(isPalindrome("awesome"))
