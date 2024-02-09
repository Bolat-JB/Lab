def ispalindrome(st):
    if st[::-1] == st:
        return True
    return False

w = "madam"
print(ispalindrome(w))